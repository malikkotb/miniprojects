// Spread/Rest Operator: ...
// allows expressions to be expanded in places where multiple
// arguments, elements or variables are expected

// spread operator -> um elemente aus einem array rauszuziehen

const arr1 = [1,2,3]
const arr2 = [4,5,6]

const both = [...arr1, ...arr2] // concatenate arrays 
console.log(both)

// Spread
// add the elements of an existing array into a new array
// pass elements of an array as arguments to a function
// copy arrays
let arr = [1, 2, 3]
let arr3 = [...arr]
arr3.push(4)
console.log(arr)
console.log(arr3)



// rest operator -> für funktions-argumente
// REST: condense multiple elements into an array

function sum(...theArgs) {
    return theArgs.reduce((previous, current) => {
        return previous + current;
    });
}

console.log(sum(1,2,3))