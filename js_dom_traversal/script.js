// Traverse the DOM

function changeColor(element) {
    element.style.backgroundColor = "#333"
}

/*
// Select elements in the DOM from the document

const grandparent = document.getElementById("grandparent-id")
const parents = Array.from(document.getElementsByClassName("parent"))

parents.forEach(changeColor)
//changeColor(grandparent)

*/

// Selecting with querySelector
// just use the css-selector
// # -> refers to id
// . -> refers to class

// const grandparent = document.querySelector('#grandparent-id')
//const grandparent = document.querySelector(".grandparent")
//changeColor(grandparent)

//const parent = document.querySelector(".parent")
// this will only select the first element it finds, not all of them 
//changeColor(parent)  

//const parents = document.querySelectorAll('.parent')
//parents.forEach(changeColor)

// converting to array: Array.from() lets u use forEach method

// Get children of a parent
//const parents = Array.from(grandparent.children)
//parents.forEach(changeColor)

//const parentOne = parents[0]
//const children = parentOne.children

//changeColor(children[0])


// Selecting descendants
//const childOne = grandparent.querySelector('.child')
//changeColor(childOne)

//const children = grandparent.querySelectorAll('.child')
//children.forEach(changeColor)


// Selecting parents
const childOne = document.querySelector('#child-one')
const parent = childOne.parentElement
//const grandparent = parent.parentElement


// Selecting Ancestors
const grandparent = childOne.closest('.grandparent')
changeColor(grandparent)


// Moving side to side -> selecting sibling elements 
const childTwo = childOne.nextElementSibling
changeColor(childTwo.previousElementSibling) // changes colour of childOne