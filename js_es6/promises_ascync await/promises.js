// JS is asynchronous programming language
// setTimeout(() => {
//     console.log("Hallo nach 2 sekunden")
// }, 2000)

// console.log("Hallo")

// Promises:
const greeting = new Promise((resolve, reject) => {
  // promise hat 2 Aufgaben
  // wir können hier drinnen code ausführen & wenn dieser code fertig ist
  // und wir mit dem Ergebnis zufrieden sind; dann rufen wir die resolve function auf

  // wenn was schief geht => reject function aufrufen

  setTimeout(() => {
    console.log("Hallo nach 2 sekunden");
    resolve("Erledigt"); // wenn log eintrag geschrieben wurde nach 2 Sekunden
    // sollte was schief laufen:
    //reject()
  }, 2000);
});

// const startGreeting = () => {
//     greeting
//         .then((result) => { // Promise starten & mit 'then' auf resolve() reagieren
//             console.log(result)
//             console.log("Hallo")
//         })
//         .catch(() => {}) // mit catch auf reject() reafieren
// }

// startGreeting()

// async await syntax

const startGreeting = async () => {
  try {
    const result = await greeting;
    console.log(result);
    console.log("Hallo");
  } catch (error) { // wenn reject() function aufgerufen wird im Promise
    // Fehlerbehandlung
  }
};

startGreeting();
