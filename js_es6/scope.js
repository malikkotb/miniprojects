if (true) {
    var varVariable = 'This is true'
}

// var is Function-scoped
// let,const is BLOCK-SCOPED

// var can be reassigned
// let can not be redeclared

// const can not be redeclared
// let can be

console.log(varVariable)

if(true) {
    let letVariable = 'This is true'
    letVariable = 'yurr'

    const constVar = 21
    constVar = 12 // THIS DOESNT WORK with const
}

console.log(letVariable) // will thorugh error -> not defined

// so use let if variable can be changed -> e.g. in for loops
// const is just for constants that won't be changed