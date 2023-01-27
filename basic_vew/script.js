const app = Vue.createApp({
    data: function() {
      return {
        title: "Welcome to Vue App",
        unsavedChangesCounter: 0
      }
    },
    computed: { // eine computed proprty
      upperCaseTitle() {
        return this.title.toUpperCase()
      }
    },
    methods: {
      resetInput() {
        this.title = ""
      }
    },
    watch: { // mit watch attribute kann man ein Data-Attribut beobachten
      title() {
        // funktionsname selber wie datenattribut um das es sich handelt
        // jedes mal wenn sich das Datenattribut ändert wird die funktion title() ausgeführt
        this.unsavedChangesCounter++
      }
    }
  })

  // verbindung zu html template
  app.mount("#app") // erwartet id von dem element an das wir uns binden wollen