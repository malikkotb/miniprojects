// Promises allow you to write clean non-callback-centric code without ever having to worry about callback hell.

let p = new Promise((resolve, reject) => {
    let a = 1 + 2 // our promise, if this failed we would reject it
    if (a == 2) { // resolve it
        resolve('Success')
    } else {
        reject('Failed')
    }
}) 

 // anything inside a .then is goint to run for -> resolve 
p.then((message) => { // do this when the promise succeeds
    console.log('This is in the then ' + message)
}).catch((message) => { // will catch any errors; do this when the promise fails
    console.log('This is in the catch ' + message);
}) 

// Promises are really great when u need to do sth. thats gonna take a long time in the background
// such as downloading an image from a different server & u just want to do something
// after its complete, instead of making everything else wait for it
// and also u can catch it if its failed, to maybe retry or give the user an error message
// if it did fail

function watchTutorialCallback(callback, errorCallback) {
    let userLeft = false
    let userWatchingCatMeme = false
  
    if (userLeft) {
      errorCallback({
        name: 'User Left', 
        message: ':('
      })
    } else if (userWatchingCatMeme) {
      errorCallback({
        name: 'User Watching Cat Meme',
        message: 'WebDevSimplified < Cat' 
      })
    } else {
      callback('Thumbs up and Subscribe')
    }
  }
  
  function watchTutorialPromise() {
    let userLeft = false
    let userWatchingCatMeme = false
    return new Promise((resolve, reject) => {
      if (userLeft) {
        reject({
          name: 'User Left', 
          message: ':('
        })
      } else if (userWatchingCatMeme) {
        reject({
          name: 'User Watching Cat Meme',
          message: 'WebDevSimplified < Cat' 
        })
      } else {
        resolve('Thumbs up and Subscribe')
      }
    })
  }
  
  watchTutorialCallback(message => {
    console.log(message)
  }, error => {
    console.log(error.name + ' ' + error.message)
  })
  
  watchTutorialPromise().then(message => {
    console.log(message)
  }).catch(error => {
    console.log(error.name + ' ' + error.message)
  })
  
  const recordVideoOne = new Promise((resolve, reject) => {
    resolve('Video 1 Recorded')
  })
  
  const recordVideoTwo = new Promise((resolve, reject) => {
    resolve('Video 2 Recorded')
  })
  
  const recordVideoThree = new Promise((resolve, reject) => {
    resolve('Video 3 Recorded')
  })
  
  Promise.all([
    recordVideoOne,
    recordVideoTwo,
    recordVideoThree
  ]).then(messages => {
    console.log(messages)
  })
  
  Promise.race([
    recordVideoOne,
    recordVideoTwo,
    recordVideoThree
  ]).then(message => {
    console.log(message)
  })