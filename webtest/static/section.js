
var host = document.getElementById("site");
for(var i=0;i<8;i++){
    str='<div class="col mb-5"><div class="card h-100"><button type="button" onclick="location.href='+"'item0{0}.html'".format(i+1)+'"><img class="card-img-top" src="{%get_static_prefix%}shopitem-0{{i}}.png" alt="..."></button><div class="card-body p-4"><div class="text-center"><h5 class="fw-bolder">{1}</h5>{2}원</div></div><div class="card-footer p-4 pt-0 border-top-0 bg-transparent"><div class="text-center"><button type="button" class="btn btn-outline-dark mt-auto" onclick="addcart({0})">카트에 담기</button></div></div></div></div>'.format(i+1,item_arr[i].name,item_arr[i].price,item_arr[i].url);
    host.innerHTML +=str;
                            }