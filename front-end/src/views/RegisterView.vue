<template>
  <div class="Register-view">
    <q-form class="Register-view-form" @submit.prevent="handleFormRegister">
      <div class="text-h2 text-center text-bold q-mb-md">Registro</div>
      <div v-if="!isAdmin" class="text-h4 text-center q-mb-md">
        Registrate para comprar
      </div>
      <q-input
        v-model="name"
        required
        label="Nombre"
        class="margin-bottom"
      ></q-input>
      <q-input
        v-model="lastName"
        label="Apellido"
        class="margin-bottom"
        required
      ></q-input>
      <q-input
        v-model="email"
        label="Correo"
        type="email"
        required
        class="margin-bottom"
      ></q-input>
      <q-input
        v-model="password"
        label="Contraseña"
        class="margin-bottom"
        type="password"
        required
      ></q-input>
      <q-select
        v-if="isAdmin"
        v-model="typeUser"
        label="Tipo de Usuario"
        class="margin-bottom"
        :options="typeUserOptions"
      />
      <q-btn
        label="Register"
        type="submit"
        class="button-center"
        color="teal"
      ></q-btn>
    </q-form>
  </div>
</template>

<script>
import { computed, defineComponent, ref } from "vue";
import { useStoreSession } from "@/store/session";
import { useRouter } from "vue-router";
import { TYPE_USER_ADMIN, TYPE_USER_CLIENT } from "@/constants";

export default defineComponent({
  name: "RegistroView",
  setup() {
    const sessionStore = useStoreSession();
    const router = useRouter();

    const name = ref();
    const lastName = ref();
    const email = ref();
    const password = ref();
    //1 -> cliente
    //0 -> Admin
    const typeUser = ref({ label: "Cliente", value: TYPE_USER_CLIENT });
    const typeUserOptions = ref([
      { label: "Cliente", value: TYPE_USER_CLIENT },
      { label: "Administrador", value: TYPE_USER_ADMIN },
    ]);

    const handleFormRegister = async () => {
      const responseCreateUser = await sessionStore.fetchCreateUser({
        nombres: name.value,
        apellidos: lastName.value,
        correo: email.value,
        contrasena: password.value,
        tipo_usuario: typeUser.value.value,
      });

      if (responseCreateUser) {
        router.push({ path: "/login" });
      }
    };

    const isAdmin = computed(() => {
      return sessionStore.getIsAdmin;
    });

    return {
      handleFormRegister,
      name,
      lastName,
      email,
      password,
      typeUser,
      isAdmin,
      typeUserOptions,
    };
  },
});
</script>

<style scoped>
.Register-view {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  padding-top: 150px;
}

.Register-view-form {
  min-width: 600px;
}

.margin-bottom {
  margin-bottom: 10px;
}

.button-center {
  margin: 0 auto;
  display: flex;
}
</style>
