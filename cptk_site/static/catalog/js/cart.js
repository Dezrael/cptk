const vm = new Vue({
    delimiters: ['{*', '*}'],
    el: '#cartApp',
    data: {
        cart: {},
        cartCount: 0,
    },
    mounted() {
        this.cart = getCartData() || {};
        this.cartCount = Object.keys(this.cart).length;
    },
    updated() {
        setCartData(this.cart);
    },
    methods: {
        checkCount: function(product) {
            if (+product.count < 1) {
                product.count = 1;
                return;
            }
        },
        clearCart: function() {
            this.cart = {};
            this.cartCount = 0;
        }
    }
})