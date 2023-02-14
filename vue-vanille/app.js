Vue.createApp({
    data() {
        return {
            goals: [],
            enteredValue: '',
        };
    },
    methods: {
        addGoal() {
            this.goals.push(this.enteredValue)
            this.enteredValue = ''
        }
    }
}).mount('#app');


// Vanilla
// const inputField = document.querySelector("input");
// const buttonEl = document.querySelector("button");
// const listEl = document.querySelector('ul');

// function addGoal() {
//     const enteredValue = inputField.value;
//     const listItemEl = document.createElement('li');
//     listItemEl.textContent = enteredValue;
//     listEl.append(listItemEl);
//     inputField.value = '';
// }

// buttonEl.addEventListener('click', addGoal);