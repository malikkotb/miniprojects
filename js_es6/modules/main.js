//import User from "./user.js"
import U, { printAge, printName as printUserName } from "./user.js"
// we can also change the name of our import statement to U
// and the U('Bob', 11) would still work, because it imports the default module in user.js

// to import non-default things -> put them inside of curly brackets

// we need to tell index.html that we're using modules
// in script tag add: type="module"

const user = new U('Bob', 11)
console.log(user)
printUserName(user)
printAge(user)