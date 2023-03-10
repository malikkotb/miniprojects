const app = Vue.createApp({
    data() {
        return {
            userInput: '',
            tasks: [],
            showList: true,
            buttonText: 'Hide List',
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