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
      <transition name="fade" mode="out-in">
        <div v-if="day.events.length">
          <!-- prüfen ob dessen events array überhaupt existiert-->
          <transition-group name="list">
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
          </transition-group>
        </div>
        <div v-else>
          <div class="alert alert-light text-center">
            <i>Keine Termine</i>
          </div>
        </div>
      </transition>
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
      Store.mutations.changeActiveDay(this.day.id);
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

<style scoped>
/* die css-klassen wirken sich auf die einzelnen Elemente in der transition-group aus
nicht auf die ganze gruppe als ganzes */
.list-enter-from, .list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

/* .list-enter-to, .list-leave-from {
  opacity: 1;
  transform: translateY(0);
} */

.list-enter-active, .list-leave-active {
  transition: all 1s ease;
}

</style>
