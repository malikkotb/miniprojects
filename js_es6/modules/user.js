// modules allow u to import and export different sections of code
// from different files into other files 
// -> which allows you to break up apart your code into
// more smaller grained files -> more understable

export default class User {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
}

export function printName(user) {
    console.log(`User's name is ${user.name}`);
}

export function printAge(user) {
    console.log(`User is ${user.age} years old`);
}

// you can only default export one thing (usually a class that you're defining)

// export { printName, printAge }