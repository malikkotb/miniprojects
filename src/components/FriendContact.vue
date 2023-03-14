<template>
  <li>
    <h2>{{ name }} {{ isFavorite ? "(Favorite)" : "" }}</h2>
    <button @click="toggleFavorite">Toggle Favorite</button>
    <button @click="toggleDetails">
      {{ detailsAreVisible ? "Hide" : "Show" }} Details
    </button>
    <ul v-if="detailsAreVisible">
      <li>
        <strong>Phone: </strong>
        {{ phoneNumber }}
      </li>
      <li>
        <strong>Email: </strong>
        {{ emailAdress }}
      </li>
    </ul>
    <!-- emit can also be called directly like here or with a method-->
    <button @click="$emit('delete-contact', id)">Delete</button>
  </li>
</template>

<script>
export default {
  // props used for parent child communication
  // props: custom html attributes
  // props: ["name", "phoneNumber", "emailAdress", "isFavorite"],
  props: {
    id: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    phoneNumber: {
      type: String,
      required: true,
    },
    emailAdress: {
      type: String,
      required: true,
    },
    isFavorite: {
      type: Boolean,
      required: true,
      // defualt value which will be used if the prop is missing
      default: false, // if not required -> add a default key
      //   validator: function (value) { // value = value provided for the prop
      //     // validation logic of my choice to find out whether value is valid or not
      //     return value === '1' || value === '0';
    },
  },
  // emits = counter part to props
  // in emits you define which custom events your component will at somepoint emit
  emits: ["toggle-favorite", "delete-contact"],
  //   emits: {
  //     'toggle-favorite': function(id) {
  //         if (id) {
  //             return true;
  //         } else {
  //             console.warn('Id is missing!');
  //             return false;
  //         }
  //     }
  //   },
  data() {
    return {
      detailsAreVisible: false,
    };
  },
  methods: {
    toggleDetails() {
      this.detailsAreVisible = !this.detailsAreVisible;
    },
    toggleFavorite() {
      // allows you to emit own custom event, from which
      // you can listen inside the parent component
      this.$emit("toggle-favorite", this.id);
      // first argument should be the name
      // following arguments will simply be data that you pass together with your event
    },
  },
};
</script>

<style></style>
