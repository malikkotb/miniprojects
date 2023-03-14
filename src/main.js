import { createApp } from 'vue';

// import ... from './' <- point at file which you want to import from

// what you import can be a named export
// or a default export

import App from './App.vue';
import FriendContact from './components/FriendContact.vue'; // just points at the js object which we're exporting in the FriendContact.vue file
import NewFriend from './components/NewFriend.vue';

const app = createApp(App)

app.component('friend-contact', FriendContact);
app.component('new-friend', NewFriend);

app.mount('#app');
