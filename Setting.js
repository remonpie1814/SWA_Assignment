String.prototype.format = function() {
    var formatted = this;
    for (var i = 0; i < arguments.length; i++) {
        var regexp = new RegExp('\\{'+i+'\\}', 'gi');
        formatted = formatted.replace(regexp, arguments[i]);
    }
    return formatted;
    };

    function counter(names){
        const result = names.reduce((acc, cur) => {
            acc[cur] = (acc[cur] || 0) + 1;
            return acc;
        }, {});
        return result;
    }
    
    var item1={name:"연필",price:1000,url:"item01.html"};
    var item2={name:"지우개",price:500,url:"item02.html"};
    var item3={name:"리코더",price:6000,url:"item03.html"};
    var item4={name:"트라이앵글",price:5000,url:"item04.html"};
    var item5={name:"스케치북",price:3000,url:"item05.html"};
    var item6={name:"공책",price:1000,url:"item06.html"};
    var item7={name:"돋보기",price:1500,url:"item07.html"};
    var item8={name:"실내화",price:3000,url:"item08.html"};

    var item_arr=[item1,item2,item3,item4,item5,item6,item7,item8];


    if (localStorage.getItem("ItemCartIn")){
        var CartinItem=JSON.parse(localStorage.getItem("ItemCartIn"));
    }
    else{
        CartinItem=[];
    }
    if (localStorage.getItem("cartcount")){
        var cartcount2=JSON.parse(localStorage.getItem("cartcount"));
    }
    else{
        cartcount2=0;
    }

    function addcart(item_id){
        item_id--;
        var carttxt = document.getElementById("cart");
        if (localStorage.getItem("cartcount")){
        var cartcount2=JSON.parse(localStorage.getItem("cartcount"));
        }
        else{
            cartcount2=0;
        }
        cartcount2++;
        carttxt.innerHTML =cartcount2;
        localStorage.setItem("cartcount",JSON.stringify(cartcount2));

        console.log(cartcount2);

        if (localStorage.getItem("ItemCartIn")){
        var CartinItem=JSON.parse(localStorage.getItem("ItemCartIn"));
        }
        else{
            CartinItem=[];
        }
        CartinItem.push(item_id)
        localStorage.setItem("ItemCartIn",JSON.stringify(CartinItem));
                    }
function cartitem_add(item_id){
    // cart을 가져온다
    CartItem=JSON.parse(localStorage.getItem("ItemCartIn"));
    // 추가
    CartItem.push(item_id);
    // localstorage에 저장
    localStorage.setItem("ItemCartIn",JSON.stringify(CartItem));
    localStorage.setItem("cartcount",JSON.stringify(CartItem.length));

    // 수정한 값 표시
    Cartin=counter(CartItem);
    var cartitem_name="item_count_"+item_id;
    console.log(cartitem_name)
    var cart_item_count = document.getElementById(cartitem_name);
    if(Cartin[item_id]){
        cart_item_count.innerHTML = Cartin[item_id];
    }
    else{
        cart_item_count.innerHTML=0;
    }

    var carttxt = document.getElementById("cart");
    if(localStorage.getItem("cartcount")){
        carttxt.innerHTML =JSON.parse(localStorage.getItem("cartcount"));
    }
    else{
        carttxt.innerHTML =0;
    }
}

function cartitem_sub(item_id){
    // cart을 가져온다
    CartItem=JSON.parse(localStorage.getItem("ItemCartIn"));
    // 제거
    index=CartItem.findIndex(i => i==item_id);
    if (index<0){
        return
    }
    CartItem.splice(index,1);
    // localstorage에 저장
    localStorage.setItem("ItemCartIn",JSON.stringify(CartItem));
    localStorage.setItem("cartcount",JSON.stringify(CartItem.length));

    // 수정한 값 표시
    Cartin=counter(CartItem);
    var cartitem_name="item_count_"+item_id;
    console.log(cartitem_name)
    var cart_item_count = document.getElementById(cartitem_name);
    if(Cartin[item_id]){
        cart_item_count.innerHTML = Cartin[item_id];
    }
    else{
        cart_item_count.innerHTML=0;
    }

    var carttxt = document.getElementById("cart");
    if(localStorage.getItem("cartcount")){
        carttxt.innerHTML =JSON.parse(localStorage.getItem("cartcount"));
    }
    else{
        carttxt.innerHTML =0;
    }
    
}


function cartitem_del(item_id){
    // cart을 가져온다
    CartItem=JSON.parse(localStorage.getItem("ItemCartIn"));
    // 전부 제거
    filtered=CartItem.filter((i) => i != item_id);
    // localstorage에 저장
    localStorage.setItem("ItemCartIn",JSON.stringify(filtered));
    localStorage.setItem("cartcount",JSON.stringify(filtered.length));

    // 수정한 값 표시
    var cartitem_name="item_"+item_id;
    var cart_item = document.getElementById(cartitem_name);
    cart_item.innerHTML=""
    cartitem_name="item_button_"+item_id;
    var cart_item_button=document.getElementById(cartitem_name);
    cart_item_button.innerHTML=""

    var carttxt = document.getElementById("cart");
    if(localStorage.getItem("cartcount")){
        carttxt.innerHTML =JSON.parse(localStorage.getItem("cartcount"));
    }
    else{
        carttxt.innerHTML =0;
    }
}