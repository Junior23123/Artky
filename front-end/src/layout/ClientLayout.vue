<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-dark text-white">
      <q-toolbar>
        <q-btn
          v-if="$q.screen.width < 600"
          flat
          round
          dense
          icon="menu"
          class="q-mr-sm"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />
        <q-toolbar-title class="cursor-pointer" @click="handleClickLogo">
          Artky
        </q-toolbar-title>
        <div v-if="$q.screen.width > 600">
          <ButtonLogout />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      persistent
      v-model="leftDrawerOpen"
      side="left"
      bordered
      class="bg-grey-3"
    >
      <q-list padding class="menu-list">
        <q-item
          clickable
          v-ripple
          to="/client"
          :active="$route.path == '/client'"
        >
          <q-item-section avatar>
            <q-icon name="home" />
          </q-item-section>
          <q-item-section> Panel</q-item-section>
        </q-item>
      
      </q-list>
    </q-drawer>

    <q-page-container class="container-admin">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "@vue/runtime-core";
import ButtonLogout from "@/components/ButtonLogout.vue";
import { useStoreSession } from "@/store/session";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ClientLayout",
  components: {
    ButtonLogout,
  },
  setup() {
    const leftDrawerOpen = ref(true);
    const sessionStore = useStoreSession();

    const router = useRouter();

    const handleClickLogo = () => {
      router.push({ name: "ClientLayout" });
    };

    return {
      sessionStore,
      leftDrawerOpen,
      handleClickLogo,
    };
  },
});
</script>

<style>
.container-admin {
  min-height: 100vh;
  width: 100%;
}
</style>
