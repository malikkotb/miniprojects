<template>
  <div class="container-fluid mt-5">
    <div class="row">
      <div class="col-12">
        <!-- Anfang: Template für die Calendar-Week-Component -->
        <CalendarWeek />
        
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
          <button @click="showSettings()" class="btn btn-lg mb-2">
            <i class="fas fa-cogs"></i>
          </button>
        </div>
        <!-- Anfang: Template für die Calendar-Settings-Component -->
        <CalendarSettings v-show="showSettingsToggle" />
        <!-- Ende: Template für die Calendar-Day-Component -->
      </div>
    </div>
  </div>
</template>

<script>
import CalendarWeek from './components/CalendarWeek.vue';
import CalendarEntry from './components/CalendarEntry.vue';
import CalendarSettings from './components/CalendarSettings.vue';
export default {
  name: "App",
  components: {
    // long way to write it
    //'CalendarWeek': CalendarWeek
    // Short way to write the same thing:
    CalendarWeek,
    CalendarEntry,
    CalendarSettings,

  },

  data() { // muss immer eine Fkt. sein, welches ein Objekt zurückliefert
    return {
      showSettingsToggle: false,
    }
  },

  methods: {
    showSettings() {
      this.showSettingsToggle ? this.showSettingsToggle = false : this.showSettingsToggle = true;
    }, 
  }

};
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.min.css";
@import "~@fortawesome/fontawesome-free/css/all.min.css";

.square {
  width: 40px;
  height: 40px;
}
</style>
