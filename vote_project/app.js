const app = Vue.createApp({ // creates the Vue Root Instance
    // Options
    data: function() {
        return {
          submissions: submissions, // from seed.js

        };
    },
}); 

// Liefert die Instanz zur Root-Component zurück
const vm = app.mount('#app') // mount to div with id="app" in DOM