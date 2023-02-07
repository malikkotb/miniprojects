<template>
  <div id="calender-entry">
    <div class="card">
      <div class="card-header text-center">
        <h5>
          Neuer Termin für: <strong>{{ activeDayName }}</strong>
        </h5>
      </div>
      <div class="card-body">
        <!-- {{ event }} -->
        <div class="alert alert-danger" v-if="error">Der Titel darf nicht leer sein.</div>
        <input
          type="text"
          class="form-control"
          placeholder="Neuer Eintrag"
          v-model="event.title"
          ref="neuerEintragInputFeld"
        />
        <select class="form-select mt-2" v-model="event.priority">
          <option value="-1">Hoch</option>
          <option value="0">Mittel</option>
          <option value="1">Tief</option>
        </select>
        <div class="text-center mt-3">
          <span
            v-for="color in eventColors"
            :key="color"
            class="d-inline-block alert m-0 me-2 square"
            :class="eventColorClasses(color)"
            role="button"
            @click="setEventColor(color)"
          >
          </span>
        </div>
        <hr />
        <div class="d-grid gap-2">
          <button class="btn btn-primary" type="reset" @click="addNewEvent()">Eintragen</button>
          <button class="btn btn-danger">Inhalt löschen</button>
        </div>
      </div>
    </div>
  </div>
</template>

// Eintragen clcken, Eingaben an den Store gegeben werden &
// dort zum Tag hinzugefügt werden

<script>
import Store from "../store";
export default {
  name: "CalendarEntry",
  // data has to be a function & has to return an object
  data() {
    return {
      eventColors: ["primary", "success", "info", "warning", "danger"],
      event: {
        // das event objekt, welches wir dynamisch binden & an Store weitergeben
        title: "",
        color: "primary",
        priority: 0,
      },
      error: false,
    };
  },
  computed: {
    activeDayName() {
      return Store.getters.activeDay().fullName;
    },
  },

  methods: {
    eventColorClasses(eventColor) {
      // das wird zurückgeg. an das Template,
      // CSS/Bootstrap Klassen werden durch array zurückgegeben,
      return [
        "alert-" + eventColor,
        this.event.color === eventColor
          ? "border border-" + this.event.color
          : "",
      ];
    },

    setEventColor(eventColor) {
      this.event.color = eventColor;
    },

    addNewEvent() {
      if(this.event.title === "") return (this.error = true);
      Store.mutations.addNewEvent(this.event);
      this.event = {
        title: "",
        color: "primary",
        priority: 0,
      }
      // event übergeben und activeDayId
    }

  },
};
</script>

<style scoped></style>
