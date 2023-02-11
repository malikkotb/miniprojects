<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <div class="col-12">
        <!-- Anfang: Template für die Calendar-Week-Component -->
        <!-- <CalendarWeekAsList />
        <CalendarWeek /> -->
        <!-- mit keep-alive sorgt Vue dafür, dass der State erhalten blei-->
        <!-- <keep-alive> -->
          <transition name="fade" mode="out-in" appear>
            <component :is="activeView" /> <!-- 'is' attribut an die computed property: activeView gebunden -->
          </transition>
        <!-- </keep-alive> -->
        <!-- Ende: Template für die Calendar-Week-Component -->
      </div>
    </div>
    <div class="row mt-3">
      <div class="col-4 offset-4">
        <!-- Anfang: Template für die Calendar-Entry-Component -->
        <CalendarEntry />
        <!-- Ende: Template für die Calendar-Day-Component -->
      </div>
      <div class="col-2 offset-2">
        <div class="float-end">
          <!-- Mit dem Button blenden wir die Calendar-Settings-Component ein bzw. aus. -->
          <button class="btn btn-lg mb-2" :class="buttonSettingsClasses" @click="showSettings()">
            <i class="fas fa-cogs"></i>
          </button>
        </div>
        <!-- Anfang: Template für die Calendar-Settings-Component -->
        <transition name="fade">
          <CalendarSettings v-if="showSettingsToggle" />
        </transition>
        <!-- Ende: Template für die Calendar-Day-Component -->
      </div>
    </div>
  </div>
</template>

<script>
// import { defineAsyncComponent } from "vue";
import Store from "./store.js";
import CalendarWeek from "./components/CalendarWeek.vue";
import CalendarEntry from "./components/CalendarEntry.vue";
import CalendarWeekAsList from "./components/CalendarWeekAsList.vue"
import CalendarSettings from "./components/CalendarSettings.vue";
export default {
  name: "App",
  components: {
    // long way to write it
    //'CalendarWeek': CalendarWeek
    // Short way to write the same thing:
    CalendarWeek,
    CalendarWeekAsList,
    CalendarEntry,
    CalendarSettings,
    // CalendarSettings Component -> asynchron laden:
    // CalendarSettings: defineAsyncComponent(() => {
    //   // callback function
    //   import(/*webpackChunkName: 'CalendarSettingsComponent'*/"./components/CalendarSettings.vue")
    // }),
  },

  data() {
    // muss immer eine Fkt. sein, welches ein Objekt zurückgibt
    return {
      showSettingsToggle: false,
    };
  },

  computed: {
    buttonSettingsClasses() {
      return this.showSettingsToggle ? ["btn-success"] : ["btn-outline-success"]
    },
    activeView() {
      return Store.getters.activeView();
    }
  },

  methods: {
    showSettings() {
      this.showSettingsToggle
        ? (this.showSettingsToggle = false)
        : (this.showSettingsToggle = true);
    },
  },
};
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.min.css";
@import "~@fortawesome/fontawesome-free/css/all.min.css";

.square {
  width: 40px;
  height: 40px;
}

/* Hat die Transition kein name-Attribut, ist der 
Name automtisch "v", also z.b. v-enter-from */

/* Transition: Fade */
/* .NAME_von_Transition-enter-from = anfangszustand*/
.fade-enter-from,
.fade-leave-to { 
  opacity: 0;
}
/* Endzustand: name-enter-to*/
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}

/* Wie die Transtion passieren soll, mit name-enter-active  */
.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease-out;
}

/* .fade-leave-from {
  opacity: 1;
}

.fade-leave-to {
  opacity: 0;
}

.fade-leave-active {
  transition: all 0.25s ease-out;
} */

</style>
