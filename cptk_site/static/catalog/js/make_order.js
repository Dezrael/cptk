let productsVal = document.getElementById('productsVal');
let totalVal = document.getElementById('totalVal');
let cart = getCartData();
let products = Array();
let total = 0;
Object.keys(cart).forEach(key => {
    let product = cart[key];
    products.push({
        title: product.title,
        count: product.count,
        price: product.price,
    });
    total += product.count * product.price;
});
productsVal.value = JSON.stringify(products);
totalVal.value = total;