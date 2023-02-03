<template>
  <div id="calendar-event">
    <div class="alert text-center" :class="alertColor">
      <!-- Template für wenn das Event nicht bearbeitet wird -->
      <template v-if="!event.edit">
        <div>
          <slot name="eventPriority" :priorityDisplayName="priorityDisplayName">
            <strong> {{ priorityDisplayName }}</strong>
          </slot>
        </div>

        <slot :event="event">
          <!-- wir haben den wert "event" zur Verfügung in den unten angegeben Props-->
          <div>{{ event.title }}</div>
          <!-- Fallback Content of Slot -->
        </slot>
        <!-- standard name of a slot: 'default'-->

        <div>
          <i class="fas fa-edit me-2" role="button" @click="editEvent()"></i>
          <i class="far fa-trash-alt" role="button" @click="deleteEvent()"></i>
        </div>
      </template>
      <template v-else>
        <!--from-control is a class from bootstrap -->
        <input
          type="text"
          class="form-control"
          :placeholder="event.title"
          v-on:input="setNewEventTitle($event)"
        />
        <div>{{ newEventTitle }}</div>
        <hr />
        <!--  -->
        <i class="fas fa-check" role="button" @click="updateEvent()" ></i>
      </template>
    </div>
  </div>
</template>

<script>
import Store from "../store";
export default {
  name: "CalendarEvent",
  props: {
    event: Object,
    day: Object,
  },
  data() {
    return {
      newEventTitle: "",
    };
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
    editEvent() {
      Store.mutations.editEvent(this.day.id, this.event.title);
    },
    updateEvent() {
      Store.mutations.updateEvent(this.day.id, this.event.title, this.newEventTitle);
    },
    setNewEventTitle(event) {
      this.newEventTitle = event.target.value;
    }
  },
};
</script>

<style scoped></style>
