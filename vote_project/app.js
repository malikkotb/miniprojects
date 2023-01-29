const app = Vue.createApp({
  // creates the Vue Root Instance
  // Options
  data: function () {
    return {
      submissions: submissions, // from seed.js
      // totalVotes: 0
    };
  },
  // methods sind nicht der optimale Weg, um Daten, die auf anderen Daten basieren, zu verwalten.
  // dafür gibts in Vue, in Options das Attribut: computed property
  computed: {
    totalVotes() {
      // console.log("Computed property ausgefuehrt")
      return this.submissions.reduce((totalVotes, submission) => {
        return totalVotes + submission.votes;
      }, 0); // startwert: 0
    },
    sortedSubmissions()  {
      return this.submissions.sort((a, b) => {
        return b.votes - a.votes;
      })
    },
    cardHeaderBackgroundColor() {
      //   Objekt Variante
        // return {
        //   'bg-primary': this.totalVotes >= 50,
        //   'text-white': this.totalVotes >= 50,
        //   Alternative: als 1 Zeiler:
        //   "bg-primary text-white": this.totalVotes >= 50,
        // };
      // Array Variante
        if (this.totalVotes >= 50) {
          return ['bg-primary', 'text-white']
          // Bei dieser Variante geben wir ein Array aus CSS Klassen an das Tempalte zurück, 
          // welche hinzugefügt werden sollen 
        }
    },
    cardTitleFontSize() { // dieses computed proprety liefert ein Objekt mit den Styles zurück
      return { fontSize: this.totalVotes+'px' }
    }
  },

  methods: {
    // wir können hier keine arrow-functions nutzen
    // denn in einer arrow-function ist das 'this' ungebunden
    // upvote: function () {},
    // upvote(submission_id) {
    //   this.submissions.find(submission => submission.id === submission_id).votes++;
    // },
    // logConsole(text) {
    //   console.log(text);
    // },
  },

  watch: {
    // innerhalb watch attribute kann man Daten beobachten
    // Wir wollen submissions beobachten (vom Data Attribut); wenn die sich ändern -> code ausführen
    // daher definiert man die Daten die man beobachten will als Funktion:
    /*
    submissions: {
      handler(newValue, oldValue) {
        this.totalVotes = this.submissions.reduce((totalVotes, submission) => {
          return totalVotes + submission.votes;
        }, 0)
      },
      deep: true, // die Option: deep (standardmäßig auf false gesetzt) und mit deep: true
      // teilen wir Vue mit, dass auch Daten innerhab des Arrays oder Objektes beobachtet werden
      immediate: true, // hiermit wird Wactheer sofort ausgeführt, nachdem die Component erstellt wurde
    },
    totalVotes(newValue, oldValue) {
      console.log(newValue)
      console.log(oldValue)
    }, */

  },

});

// Globale Component
app.component("SubmissionListItem", {
  // Options
  // Props: um Daten vom elternelement an das Kindelement weiterzugeben
  props: ["submission"], // müssen im template mit v-bind -> submission binden
  methods: {
    // upvote(submission_id) {
    //   this.submissions.find(submission => submission.id === submission_id).votes++;
    // }
    upvote() {
      this.submission.votes++;
    }, 
  },
  template: `
    <div class="d-flex">
    <div class="d-shrink-0">
      <img v-bind:src="submission.img" alt="" />
    </div>
    <div class="flex-grow-1 ms-3">
      <!-- <h5 v-once> v-once makes this section only render once (even if you change the underlying data) -->
      <h5>
        {{ submission.title }}
        <!-- <span 
                                  class="float-end text-primary" 
                                  style="cursor: pointer"
                                  v-on:click.right="upvote(), logConsole('User voted')"> -->
        <!--  v-on:click="upvote" -->
        <!-- upvote wird hier ohne Klammern aufgerufen
                                  und es wird implizit von Vue ein event objekt
                                  mitübergegeben, auf welches wir in app.js
                                  zugreifen können.
                                  Um selber argumente zu übergeben und zstzl. Zugriff
                                  zu haben auf das event Objekt, können wir die so schreiben:
                                  v-on:click="upvote('User voted!', $event)"
                                  !!! Achtung: bei mehreren event listenern
                                  muss die explizite schreibweise genutzt werden
                                  also nur upvote - geht nicht
                                  es geht nur: upvote() also mit klammern-->
        <!-- Event modifier: nur rechte maustaste: @click.right -->
        <span
          class="float-end text-primary"
          style="cursor: pointer"
          v-on:click="upvote()"
        >
          <i class="fa fa-chevron-up" aria-hidden="true"></i>
          <strong>{{ submission.votes }}</strong>
        </span>
      </h5>
      <!-- <div>{{ submission.desc }}</div> -->
      <div v-html="submission.desc"></div>
      <!-- <ul> <!-- durch objekt zu iterieren:
              <li v-for="(value, key, index) in submission">
                  {{ index }} - {{ key }} - {{ value }}
              </li>                        
          </ul> -->
      <!-- <div v-pre>{{ submission.desc }}</div> -->
      <small class="text-muted"
        >Submitted by: {{ submission.author }}</small
      >
    </div>
  </div>
  
  `
})

// Liefert die Instanz zur Root-Component zurück
const vm = app.mount("#app"); // mount to div with id="app" in DOM
