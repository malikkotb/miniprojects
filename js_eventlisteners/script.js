const grandparent = document.querySelector('.grandparent')
const parent = document.querySelector('.parent')
const child = document.querySelector('.child')

// addEventListener(typeOfEvent, callback=functions that runs everytime that we do the event)
// Events happen in the order they are defined in!!

// Event-Bubbling: Process of going from the closest to the furthest away element
// if we click on the child object: first Child 1 will be printed
// then Parent 1, then Grandparent 1
// because parent is behind child and grandparent behind parent

// Capturing: Process of going from thing furthest away and moves up to the things thats closest.
// if we want a Capture -> we can set the 3rd parameter of eventlistener: { capture: true }


// To Stop Event Propagation: e.stopPropagation()

// To make event only run once:
// as third parameter add: { once: true }

/*
grandparent.addEventListener('click', e => {
    //console.log(e.target) // target is the thing the event happened on
    console.log("Grandparent Capture");
}, { capture: true })

grandparent.addEventListener('click', e => {
    console.log("Grandparent Bubble");
})

// parent.addEventListener('click', e => {
//     //e.stopPropagation()
//     console.log("Parent Capture");
// }, { capture: true })

parent.addEventListener('click', e => {
    console.log("Parent Bubble");
}, { once: true })

parent.addEventListener('click', printHi)

setTimeout(() => {
    parent.removeEventListener('click', printHi)
}, 2000)

child.addEventListener('click', e => {
    console.log("Child Capture");
}, { capture: true })

child.addEventListener('click', e => {
    console.log("Child Bubble");
})

function printHi() {
    console.log("Hi");
}

*/

// Event Delegation

const divs = document.querySelectorAll('div')

// divs.forEach(div => {
//     div.addEventListener('click', e => {
//         console.log('hi');
//     })
// })

// Event delegation:
addGlobalEventListener('click', 'div', e => {
    console.log('hi');
})

function addGlobalEventListener(type, selector, callback) {
    document.addEventListener(type, e => {
        if (e.target.matches(selector)) {
            callback(e)
        }
    })
}

const newDiv = document.createElement('div')
newDiv.id = "new-div"
newDiv.style.width = '200px'
newDiv.style.height = '200px'
newDiv.style.backgroundColor = 'purple'
document.body.append(newDiv)