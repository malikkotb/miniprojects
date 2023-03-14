<template>
    <!-- submit.prevent is needed to make the page not reload after the form has been submitted-->
  <form @submit.prevent="addContact">
    <div>
      <label>Name</label>
      <input type="text" v-model="newName"/>
    </div>
    <div>
      <label>Phone</label>
      <input type="tel" v-model="newPhone"/>
    </div>
    <div>
      <label>E-mail</label>
      <input type="email" v-model="newEmail" />
    </div>
    <div>
        <button>Add Contact</button>
    </div>
  </form>
</template>

<script>
export default {
  props: [],
  emits: ['add-contact'],
  data() {
    return {
      newName: "",
      newPhone: "",
      newEmail: "",
    };
  },
  methods: {
    addContact() {
        this.$emit('add-contact', this.newName, this.newPhone, this.newEmail);
    },
  }
};
</script>

<style></style>
