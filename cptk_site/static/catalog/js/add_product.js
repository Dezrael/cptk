const vm = new Vue({
    delimiters: ['{*', '*}'],
    el: '#productApp',
    data: {
        attributes: null
    },
    mounted () {
        let cat_selector = document.getElementById("id_category");
        cat_selector.addEventListener('change', this.getAttributes)
    },
    methods: {
        getAttributes: function(event) {
            fetch('api/get_attributes?category='+event.target.value)
            .then(response => response.json())
            .then(data => this.attributes = data);
        }
    }
})