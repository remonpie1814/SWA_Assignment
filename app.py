from flask import Flask,jsonify,request
import cx_Oracle

app=Flask(__name__)

# 연결
connection = cx_Oracle.connect(user="ADMIN", password="비밀번호", dsn="cnudb_high")
cursor = connection.cursor()

# menus를 가져온다
sql="""SELECT * FROM MENUS"""
cursor.execute(sql)
menuslist=cursor.fetchall()
menus=[]
for i in menuslist:
    menus.append({"id":i[0],"name":i[1],"price":i[2]})


@app.route('/')
def hello_flask():
    return "Hello world!"

# GET/menus
@app.route("/menus")
def get_menus():
    
    #GET을 하면 서버에서 다시 가져옴
    sql="""SELECT * FROM MENUS"""
    cursor.execute(sql)
    global menuslist
    menuslist=cursor.fetchall()
    global menus
    menus=[]

    for i in menuslist:
        menus.append({"id":i[0],"name":i[1],"price":i[2]})
    return jsonify({"menus":menus})

# POST/menus
@app.route("/menus",methods=["POST"])
def create_menu():
    request_data=request.get_json()

    # python 측 데이터
    menus.sort(key=lambda x:x["id"])
    menuid=len(menus)+1
    for i in range(len(menus)):
        if i+1!=menus[i]["id"]:
            menuid=i+1
            break

    new_menu={
        "id":menuid,
        "name":request_data["name"],
        "price":request_data["price"]
    }
    menus.append(new_menu)

    #서버에 전송
    sql="""INSERT INTO MENUS(ID,NAME,PRICE)
                        VALUES {}""".format((menuid,request_data["name"],request_data["price"]))
    cursor.execute(sql)
    connection.commit()

    return jsonify(sql)

@app.route("/menus/<int:id>",methods=["PUT"])
def put_menu(id):
    request_data=request.get_json()

    #python 측 데이터
    modified={
        "id":id+1,
        "name":request_data["name"],
        "price":request_data["price"]
    }
    count=0
    for i in menus:
        if i["id"]==id:
            break
        count+=1
    menus[count]=modified

    # 서버에 전송
    sql="""UPDATE MENUS
        SET ID={},NAME='{}',PRICE={}
        WHERE ID={}""".format(id,request_data["name"],request_data["price"],id)
    cursor.execute(sql)
    connection.commit()

    get_menus()
    return jsonify(sql)

@app.route("/menus/<int:id>",methods=["DELETE"])
def delete_menu(id):
    # python 데이터
    for i in range(len(menus)):
        if menus[i]["id"]==id:
            del menus[i]
            break
    menus.sort(key=lambda x:x["id"])

    # 서버 전송
    sql="""DELETE FROM MENUS
            WHERE ID={}""".format(id)
    cursor.execute(sql)
    connection.commit()
    get_menus()
    return "ID{} is DELETE!".format(id)

if __name__=="__main__":
    app.run()

