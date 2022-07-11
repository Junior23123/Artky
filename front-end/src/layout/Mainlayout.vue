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
        <q-toolbar-title class="cursor-pointer" @click="handleClickLogo" > Artky </q-toolbar-title>
        <div v-if="$q.screen.width > 600">
          <q-btn
            v-for="link in links"
            :key="link.path"
            :label="link.label"
            flat
            :to="link.path"
            class="q-ml-sm"
          />
          <ButtonCart/>
          <ButtonLogout v-if="sessionStore.getIsLogin" />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-if="$q.screen.width < 600"
      show-if-above
      v-model="leftDrawerOpen"
      side="left"
      bordered
    >
      <q-list padding class="menu-list">
        <q-item
          v-for="link in links"
          :key="link.path"
          clickable
          v-ripple
          :to="link.path"
          :active="link.path === $route.path"
        >
          <!-- <q-item-section avatar>
            <q-icon name="inbox" />
          </q-item-section> -->

          <q-item-section> {{ link.label }} </q-item-section>
        </q-item>
        <ButtonCart class="q-ml-sm"/>
        <ButtonLogout v-if="sessionStore.getIsLogin" />
      </q-list>
    </q-drawer>

    <q-page-container class="container">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { computed, defineComponent, ref } from "@vue/runtime-core";
import ButtonLogout from "@/components/ButtonLogout.vue";
import ButtonCart from "@/components/ButtonCart.vue";
import { useStoreSession } from "@/store/session";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "MainLayout",
  components: {
    ButtonLogout,
    ButtonCart
  },
  setup() {
    const linksTopBar = [
      {
        label: "Inicio",
        path: "/",
      },
      {
        label: "Catálogo",
        path: "/catalogo",
      },
      {
        label: "Inicio Sesión",
        path: "/login",
      },
      {
        label: "Registrarse",
        path: "/register",
      },
    ];

    const leftDrawerOpen = ref(false);
    const sessionStore = useStoreSession();
    const router = useRouter();

    const links = computed(() => {
      if (sessionStore.getIsLogin) {
        return linksTopBar.filter((link) => link.path !== "/login");
      }

      return linksTopBar;
    });

    const handleClickLogo = () => {
      router.push({ name: "Mainlayout" });
    };

    return {
      links,
      sessionStore,
      leftDrawerOpen,
      handleClickLogo,
    };
  },
});
</script>

<style>
.container {
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(to left, #ffffff, #ffefba);
}
</style>
