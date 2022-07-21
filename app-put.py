from flask import Flask,jsonify,request

app=Flask(__name__)

menus=[
    {"id":1,"name":"Espresso","price":3800},
    {"id":2,"name":"Americano","price":4100},
    {"id":3,"name":"CafeLatte","price":4600},
]



@app.route('/')
def hello_flask():
    return "Hello world!"

# GET/menus
@app.route("/menus")
def get_menus():
    return jsonify({"menus":menus})

# POST/menus
@app.route("/menus",methods=["POST"])
def create_menu():
    request_data=request.get_json()
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
    return jsonify(new_menu)

@app.route("/menus/<int:id>",methods=["PUT"])
def put_menu(id):
    request_data=request.get_json()
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
    return jsonify(modified)

@app.route("/menus/<int:id>",methods=["DELETE"])
def delete_menu(id):
    for i in range(len(menus)):
        if menus[i]["id"]==id:
            del menus[i]
            break
    menus.sort(key=lambda x:x["id"])

    return "ID{} is DELETE!".format(id)

if __name__=="__main__":
    app.run()
