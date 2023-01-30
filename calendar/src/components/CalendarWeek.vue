<template>
  <div id="calender-week">
    <div class="card-group">
      <!-- Anfang: Template für die Calendar-Day-Component -->
      <CalendarDay  v-for="i in 7" :key="i" />
      <!-- Ende: Template für die Calendar-Day-Component -->
    </div>
  </div>
</template>

<script>
import CalendarDay from "./CalendarDay.vue";
export default {
  name: "CalendarWeek",
  components: {
    CalendarDay,
  },
};
</script>

<style scoped></style>
