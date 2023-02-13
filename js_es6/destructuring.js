// old way:
const arr = [1,2,3]
const one = arr[0]
const two = arr[1]

// new: with destructuring
const [one_,two_] = [1,2,3]
// -> makes code more concise and readable

// to ignore values / omit a variable -> add comma without variable name

const [one__, ,three] = arr
console.log(one__)
console.log(three)

// using spread with destructuring
let food = ['🥓', '🍕', '🍟']
let [speck, ...therest] = food
console.log(therest); // [ '🍕', '🍟' ]

// using a deafult value
food = [undefined, '🍕', '🍟']
const [bacon = "🥓", ...rest] = food
console.log(bacon);

const obj = {
    shroom: '🍄',
    banana: '🍌',
    pepper: '🌶️'
}

// old way
const shroom_ = obj.shroom
const banana_ = obj.banana
const pepper_ = obj.pepper

// can also used default value if a property of an object is undefined

// New Way: with Object Destructuring
// Rename Properties with: const { propertyName: newVariableName }
const { shroom: mushroom, banana, pepper } = obj
console.log(mushroom, banana, pepper);

// Access Nested Properties of Objects with Colon
const objEx = {
    parent: {
        child:'👶'
    },
}

const { parent: { child } } = objEx
console.log(child); // 👶

// can be used in for-loop when you have an array of objects
const users = [
    { id: 1 },
    { id: 2 },
    { id: 3 }
]

for (const { id } of users) {
    console.log(id); // 1 2 3
}

// Function Args
const user = { id: 0, username: 'jeff' }

function haveFun( { id, username } ) {
    console.log(`hi ${username}`);
}

haveFun(user)

// swapping variables
let a = 'foo'
let b = 'bar'

[a, b] = [b, a]
console.log(a);