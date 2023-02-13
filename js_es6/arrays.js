const items = [
    { name: 'Bike', price: 100},
    { name: 'TV', price: 200},
    { name: 'Album', price: 10},
    { name: 'Book', price: 5},
    { name: 'Phone', price: 500},
    { name: 'Computer', price: 1000 },
    { name: 'Keyboard', price: 25}
]

// All the methods don't change the underlying object - good :)

// filter
const cheapItems = items.filter((item) => item.price <= 100)
console.log(cheapItems)

// map - convert into new array 
const itemNames = items.map((item) => item.name)
console.log(itemNames);

// find - finds a single (the first item) object in the array 
const foundItem = items.find((item) => item.name === 'Book')
console.log(foundItem);

// forEach - does sth. for every single element in the array
items.forEach((item) => console.log(item.name))

// some() - will return true or false
// check i.e. if some of the items in the array
// have a price of less than 100 dollars
const hasInexpensiveItems = items.some((item) => item.price <= 100)
console.log(hasInexpensiveItems); // true

// every() - will return true or false
// check if all of the items in the array adhere to some condition
const allInexpensiveItems = items.every((item) => item.price <= 100)
console.log(allInexpensiveItems); // false

// reduce() - doing an operation on the array & returning a combination of all those different combinations 
const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal
}, 0) // we wanna start at 0 = currentTotal

console.log(total);

// includes 
const nums = [1,2,3,4,5]
const includesTwo = nums.includes(2)
console.log(includesTwo);