<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-dark text-white">
      <q-toolbar>
        <q-toolbar-title>
          Artky
        </q-toolbar-title>
        <q-btn label="Inicio" flat to="/"></q-btn>
        <q-btn label="Catálogo" flat to="/catalogo"></q-btn>
        <q-btn label="Inicio Sesión" flat to="/login"></q-btn>
        <q-btn label="Registrarse" flat to="/register"></q-btn>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { defineComponent } from "@vue/runtime-core";

export default defineComponent({
name: "MainLayout"

});

</script>