<template>
  <q-btn  flat label="Cerrar sesión" color="blue" icon-right="logout" @click="handleLogout" />
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ButtonLogout",
  setup() {
    const handleLogout = () => {
       window.location.href = '/'
    };
    return { handleLogout };
  },
});
</script>
