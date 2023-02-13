// Arrow Functions

/*

// normal 
function sum(a, b) {
    return a + b
}

// arrow (like lambda functions in python)
let sum2 = (a,b) => a + b

// normal 
function isPositive(number) {
    return number >= 0
}

// arrow (like lambda functions in python)
let isPositive2 = number => number >= 0

// normal 
function randomNumber() {
    return Math.random
}

// arrow (like lambda functions in python)
let randomNumber2 = () => Math.random


// normal 
document.addEventListener('click', function() {
    console.log('click')
})

// arrow (like lambda functions in python)
document.addEventListener('click', e => console.log('click'))

*/

// arrow functions redefine the 'this' keyword inside of them
// as opposed to normal functions

class Person {
    constructor(name) {
        this.name = name
    }

    printNameArrow() {
        setTimeout(() => {
            console.log('Arrow: ' + this.name)
        }, 100)
    }

    printNameFunction() {
        setTimeout(function() {
            console.log('Arrow: ' + this.name)
        }, 100)
    }
}
let person = new Person('Bob')
person.printNameArrow()
person.printNameFunction()

// standard JS way: it defines 'this' based on where the function is called
// when using an arrow function -> 'this' is not redefined
console.log(this.name) // will print nothing