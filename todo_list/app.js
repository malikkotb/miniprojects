const app = Vue.createApp({
    data() {
        return {
            userInput: '',
            tasks: [],
            showList: true,
        }
    },
    computed: {
        buttonText() {
            return this.showList ? 'Hide List' : 'Show List';
        }
    },
    methods: {
        addTask() {
            this.tasks.push(this.userInput);
        },
        toggleList() {
            this.showList = !this.showList;
        }
    }
});

app.mount('#assignment')