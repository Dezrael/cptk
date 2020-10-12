const vm = new Vue({
    delimiters: ['{*', '*}'],
    el: '#productApp',
    data: {
        attributes: null,
        sel_attributes: null,
        files: {}
    },
    mounted () {
        let cat_selector = document.getElementById("id_category");
        cat_selector.addEventListener('change', this.getAttributes);
        cat_selector.addEventListener('change', this.getSelAttributes);
    },
    methods: {
        getAttributes: function(event) {
            fetch('api/get_attributes?category='+event.target.value)
            .then(response => response.json())
            .then(data => this.attributes = data);
        },
        getSelAttributes: function(event) {
            fetch('api/get_sel_attributes?category='+event.target.value)
            .then(response => response.json())
            .then(data => this.sel_attributes = data);
        },
        filesUploaded: function(event) {
            this.files = event.target.files;
        }
    }
})