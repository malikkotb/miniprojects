<template>
  <div class="card border-start" :class="cardClasses">
    <div
      class="card-header text-center"
      :class="cardHeaderClasses"
      role="button"
      @click="changeActiveDay()"
    >
      <strong>{{ day.fullName }}</strong>
    </div>
    <div class="card-body">
      <CalendarEvent
        v-for="event in day.events"
        :key="event.title"
        :event="event"
        :day="day"
      >
       <!-- statt v-slot: kann man auch nur schreiben: # -->
        <template #eventPriority="slotProps">
          <h5>{{ slotProps.priorityDisplayName }}</h5>
        </template>
        <!-- mit destructuring: aus slotprops das event holen: -->
        <template v-slot="{ event }"
          ><i>
            {{ event.title }}
          </i></template
        >
        <!--same as v-slot:default -->
      </CalendarEvent>
    </div>
  </div>
</template>

<script>
import CalendarEvent from "./CalendarEvent.vue";
import Store from "../store";
export default {
  name: "CalendarDay",
  components: {
    CalendarEvent,
  },
  // Objekt-Schreibweise für props
  props: {
    // possible types: primitives, and Array, Object, Function
    // day: Object
    day: {
      type: Object,
      required: true,
      // with primitive datatypes: default: 100
      default: function () {
        return {
          id: -1,
          fullName: "Fehlender Wochentag",
          events: [],
        };
      },
      validator: function (value) {
        if (Object.keys(value).includes("id")) {
          return true;
        }
      },
    },
  },

  methods: {
    changeActiveDay() {
      // evt. fehlerbehandlung: make method not activate if the clicked card-header is the active day already
      //console.log(this.day.id)
      Store.mutations.changeActiveDay(this.day.id)
    },
  },

  computed: {
    cardClasses() {
      return this.day.id === Store.getters.activeDay().id
        ? ["border-primary"]
        : null;
    },

    cardHeaderClasses() {
      return this.day.id === Store.getters.activeDay().id
        ? ["bg-primary", "text-white"]
        : null;
    },
  },
};
</script>

<style scoped></style>
