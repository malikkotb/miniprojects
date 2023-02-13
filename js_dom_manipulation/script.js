// Adding elements to the page

// 1. select element (document.body) which we can append elements to
//const body = document.body;
//body.append("Hello World", "nice to meet you");
// appendChild() can not append strings only elements, like divs or spans or anchor tags etc. 

// Creating Elements
//const div = document.createElement('div') // create the element
//body.append(div) // add id to the body


// Modifying Element Text
//div.innerText = "Hi Bro"
// or use:
//div.textContent = "Bye Bro"

//const div = document.querySelector("div")

//console.log(div.textContent) // prints out exact text content
//console.log(div.innerText) // prints only the text thats visible on our page 



// Modifying Element HTML
// const body = document.body
// const div = document.createElement("div")
// div.innerHTML = "<strong>Hello World 2</strong>"

// or you can do the same like this:

// const strong = document.createElement("strong")
// strong.innerText = "Hello World 3"
// div.append(strong)
// body.append(div)


// Removing Elements
const body = document.body
const div = document.querySelector("div")
const spanHi = document.querySelector("#hi")
const spanBye = document.querySelector("#bye")

//spanBye.remove() // removes it from html (but can add it back later with append())

// Modiyfying Element Attributes

//console.log(spanHi.getAttribute('title'))
// simpler:
console.log(spanHi.id)
console.log("---")
console.log(spanHi.title)

spanHi.setAttribute("id", "sdfefs")
// or
spanHi.title = "fwfew"

spanHi.removeAttribute("id") // remove an attribute 


// Modifying Data Attributes
// console.log(spanHi.dataset)
// console.log(spanHi.dataset.test)
// console.log(spanHi.dataset.longerName)

// set a new data attribute (custom attributes)
spanHi.dataset.newName = "hi"

// Modifying Element Classes
console.log(spanHi.classList)
// spanHi.classList.add('new-class')
// spanHi.classList.remove("hi1")
// spanHi.classList.toggle("hi3", true)

// Modifying Element Style
spanHi.style.color = 'red'
// if css sytle name has a hyphen -> convert it to camelCase
spanHi.style.backgroundColor = 'yellow'