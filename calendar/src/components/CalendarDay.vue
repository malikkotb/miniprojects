<template>
  <div class="card">
    <div class="card-header text-center" role="button">
      <strong>Montag</strong>
    </div>
    <div class="card-body">
      <CalendarEvent />
    </div>
  </div>
</template>

<script>
import CalendarEvent from "./CalendarEvent.vue";
export default {
  name: "CalendarDay",
  components: {
    CalendarEvent,
  },
};
</script>

<style scoped></style>
