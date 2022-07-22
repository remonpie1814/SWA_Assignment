var carttxt = document.getElementById("cart");
var cartcount2=JSON.parse(localStorage.getItem("cartcount"));
carttxt.innerHTML =cartcount2;