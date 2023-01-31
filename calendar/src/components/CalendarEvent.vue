<template>
  <div id="calendar-event">
    <div class="alert text-center" :class="alertColor">
      <div>
        <slot name="eventPriority" :priorityDisplayName="priorityDisplayName">
          <strong> {{ priorityDisplayName }}</strong>
        </slot>
      </div>

      <slot :event="event"> <!-- wir haben den wert "event" zur Verfügung in den unten angegeben Props-->
        <div>{{ event.title }}</div><!-- Fallback Content of Slot -->
      </slot>
      <!-- standard name of a slot: 'default'-->

      <div>
        <i class="fas fa-edit me-2" role="button"></i>
        <i class="far fa-trash-alt" role="button" @click="deleteEvent()"></i>
      </div>
    </div>
  </div>
</template>

<script>
import Store from '../store';
export default {
  name: "CalendarEvent",
  props: {
    event: Object,
    day: Object,
  },
  computed: {
    priorityDisplayName() {
      switch (this.event.priority) {
        case 1:
          return "Tief";
        case 0:
          return "Mittel";
        case -1:
          return "Hoch";
      }
      return "Unbekannte Priorität";
    },
    alertColor() {
      return "alert-" + this.event.color;
    },
  },

  methods: {
    deleteEvent() {
      Store.mutations.deleteEvent(this.day.id, this.event.title);
    },
  }
};
</script>

<style scoped></style>
