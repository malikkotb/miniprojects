import { calendarWeekData } from "./seed";
import { reactive, readonly } from "vue";

// die methode: reactive von vue: Daten selbst in das Reactivity system reinzunehmen
const state = reactive({
  // wollen das state object explizit zum Reactivity system von vue.js hinzufügen
  calendarWeekData, // 'calendarWeekData' = calendarWeekData
});

const getters = {
  activeDay: () => state.calendarWeekData.find((day) => day.active),
};

const mutations = {
  editEvent(dayId, eventTitle) {
    // Alle edit-Attribute auf false setzten, sodass immer nur ein Event bearbeitet werden kann
    state.calendarWeekData.map((dayObj) => {
      dayObj.events.map((event) => (event.edit = false));
    });
    // Setzte das entsprechende Edit-Attribut auf true
    const dayObj = state.calendarWeekData.find((day) => day.id === dayId);
    const eventObj = dayObj.events.find((event) => event.title === eventTitle);
    eventObj.edit = true;
  },
  updateEvent(dayId, oldEventTitle, newEventTitle) {
    if (newEventTitle.length < 1) {
      newEventTitle = oldEventTitle;
    }
    const dayObj = state.calendarWeekData.find((day) => day.id === dayId);
    const eventObj = dayObj.events.find(
      (event) => event.title === oldEventTitle
    );
    eventObj.title = newEventTitle;
    eventObj.edit = false;
  },
  deleteEvent(dayId, eventTitle) {
    const dayObj = state.calendarWeekData.find((day) => day.id === dayId);
    const eventIndex = dayObj.events.findIndex(
      (event) => event.title === eventTitle
    );
    dayObj.events.splice(eventIndex, 1);
  },
};

// readonly() sorgt dafür, dass wir nur Daten lesen, aber nicht ändern können
export default {
  state: readonly(state),
  getters,
  mutations,
};
