// const square = function(a) {
//     return a*a
// }

// const square = (a) => {
//     return a*a
// }

// const square = (a) => a*a2
// // all ways are the same => just more elegant
// console.log(square(6))


const car = {
    model: "Fiesta",
    manufacturer: "Ford",
    fullName_arrow: () => `${this.manufacturer} ${this.model}`, // prints: undefined undefined
    // when writing fullName as arrow function -> bindet sich das 'this' nicht
    // an das äußere Objekt in der das ganze aufgerufen wird
    // d.h. wenn man eine Fkt. schreibt, die auf Attribute des Objekts zugreift
    // => kann man diese Fkt. nur als normale Fkt. & nicht als arrow func schreiben
    fullName() { // this works
        return `${this.manufacturer} ${this.model}`
    }
}

// also arrow functions, dann benutzen: wenn man keine abhängigkeit hat zu
// anderen Attributen hat

console.log(car.fullName())
