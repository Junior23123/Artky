<template>
  <div class="login-view">
    <q-form class="login-view-form">
      <div class="text-h2 text-center text-bold q-mb-md">Iniciar Sesión</div>
      <div class="text-h4 text-center q-mb-md">Ingresa para comprar</div>
      <q-input label="Correo" class="margin-bottom" type="email" v-model="email"></q-input>
      <q-input
        label="Contraseña"
        class="margin-bottom"
        v-model="password"
        type="password" 
      ></q-input>
      <q-btn
        label="Login"
        class="button-center"
        color="teal"
        @click="handleLogin"
      ></q-btn>
    </q-form>
  </div>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { useStoreSession } from "@/store/session";
import { TYPE_USER_ADMIN } from "@/constants";

export default defineComponent({
  name: "LoginView",
  setup() {
    const email = ref("");
    const password = ref("");

    const storeSession = useStoreSession();
    const router = useRouter();

    const handleLogin = async () => {
      const responseLogin = await storeSession.fetchLogin({
        correo: email.value,
        contrasena: password.value,
      });

      if (responseLogin) {
        router.push({
          name:
            responseLogin.typeUser == TYPE_USER_ADMIN
              ? "AdminLayout"
              : "Mainlayout",
        });
      }
    };

    return {
      password,
      email,
      handleLogin,
    };
  },
});
</script>

<style scoped>
.login-view {
  height: 100vh;
  width: 100%;
  display: flex;
  padding-top: 150px;
  justify-content: center;
}

.login-view-form {
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
