updateCartInfo();

function getCartData(){
    return JSON.parse(localStorage.getItem('cart'));
}

function updateCartInfo() {
    let cartData = getCartData() || {};
    let cart = document.getElementById('items_count');
    cart.innerHTML = Object.keys(cartData).length;
}

function setCartData(o){
    localStorage.setItem('cart', JSON.stringify(o));
    updateCartInfo();
}

function clearCartData() {
    localStorage.removeItem('cart');
    updateCartInfo();
}

function addItem(itemID, itemTitle, itemPrice) {
    let cartData = getCartData() || {};
    if(!cartData.hasOwnProperty(itemID)) {
        cartData[itemID] = {
            title: itemTitle,
            price: itemPrice.replace(/,/, '.'),
            count: 1,
        };
    }
    setCartData(cartData);
}