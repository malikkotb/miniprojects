import { calendarWeekData } from "./seed";
import { reactive, readonly } from "vue";

// die methode: reactive von vue: Daten selbst in das Reactivity system reinzunehmen
const state = reactive({
  // wollen das state object explizit zum Reactivity system von vue.js hinzufügen
  calendarWeekData, // 'calendarWeekData' = calendarWeekData
  activeView: "CalendarWeek", // same name as component
  activeOrdering: "title",
});

const getters = {
  activeDay: () => state.calendarWeekData.find((day) => day.active),
  activeView: () => state.activeView,
  activeOrdering: () => state.activeOrdering,
};

const mutations = {
  addNewEvent(newEvent) {
    const activeDay = getters.activeDay();
    activeDay.events.push({
      title: newEvent.title,
      edit: false,
      color: newEvent.color,
      priority: Number(newEvent.priority),
    });
  },

  setActiveView(view) { 
    state.activeView = view;
  },

  setActiveOrdering(ordering) {
    state.activeOrdering = ordering;
  },

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
  updateEvent(dayId, oldEventTitle, newEvent) {
    if (newEvent.title.length < 1) {
      newEvent.title = oldEventTitle;
    }
    const dayObj = state.calendarWeekData.find((day) => day.id === dayId);
    const eventObj = dayObj.events.find(
      (event) => event.title === oldEventTitle
    );
    eventObj.title = newEvent.title;
    eventObj.priority = Number(newEvent.priority);
    eventObj.edit = false;
  },
  deleteEvent(dayId, eventTitle) {
    const dayObj = state.calendarWeekData.find((day) => day.id === dayId);
    const eventIndex = dayObj.events.findIndex(
      (event) => event.title === eventTitle
    );
    dayObj.events.splice(eventIndex, 1);
  },
  changeActiveDay(nowActiveDayId) {
    // Alle active-attribute der tage auf false setzen
    state.calendarWeekData.forEach((day) => {
      day.active = false;
    });
    // dann geclickter Tag active attribute auf true setzen
    const newActiveObj = state.calendarWeekData.find(
      (day) => day.id === nowActiveDayId
    );
    newActiveObj.active = true;
  },
};

// readonly() sorgt dafür, dass wir nur Daten lesen, aber nicht ändern können
export default {
  state: readonly(state),
  getters,
  mutations,
};
