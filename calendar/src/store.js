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
