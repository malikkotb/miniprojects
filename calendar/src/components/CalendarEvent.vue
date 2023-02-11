<template>
  <div id="calendar-event">
    <div class="alert text-center" :class="alertColor">
      <transition name="fade" mode="out-in">
        <!-- Template für wenn das Event nicht bearbeitet wird -->
        <div v-if="!event.edit">
          <div>
            <slot
              name="eventPriority"
              :priorityDisplayName="priorityDisplayName"
            >
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
            <i
              class="far fa-trash-alt"
              role="button"
              @click="deleteEvent()"
            ></i>
          </div>
        </div>
        <div v-else>
          <!--from-control is a class from bootstrap -->
          <input
            type="text"
            class="form-control"
            ref="newEventTitleInput"
            :placeholder="event.title"
            v-on:input="setNewEventTitle($event)"
          />
          <!-- dass v-on:input kann man genau so mit v-model machen-->
          <!-- v-model sorgt für 2-way binding, bedeutet die Änderungen im Template
        werden direkt an das Skript weitergegeben und umgekehrt -->
          <select class="form-select mt-2" v-model="newEventPriority">
            <option value="-1">Hoch</option>
            <option value="0">Mittel</option>
            <option value="1">Tief</option>
          </select>
          <hr />
          <!--  -->
          <i class="fas fa-check" role="button" @click="updateEvent()"></i>
        </div>
      </transition>
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
      newEventPriority: this.event.priority,
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
      // um auf den Input-tag zu fokussieren
      // auf template refs zugreifen
      Store.mutations.editEvent(this.day.id, this.event.title);
      // ein Tick vergeht, wenn das Template neu gerendered wurde
      this.$nextTick(() => {
        this.$refs.newEventTitleInput.focus();
      }); // nimmt als parameter eine Funktion, welche dann asugeführt wird, wenn der nächste Tick erreicht wird
    },
    updateEvent() {
      Store.mutations.updateEvent(this.day.id, this.event.title, {
        title: this.newEventTitle,
        priority: this.newEventPriority,
      });
    },
    setNewEventTitle(event) {
      this.newEventTitle = event.target.value;
    },
  },
};
</script>

<style scoped></style>
