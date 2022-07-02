<template>
    <div class="login-view">
        <q-form class="login-view-form">
            <h1 class="text-h2 text-center">Iniciar Sesión</h1>
            <h2 class="text-h4 text-center">Ingresa para comprar</h2>
            <q-input label="Correo" class="margin-bottom"></q-input>
            <q-input label="Contraseña" class="margin-bottom"></q-input>        
            <q-btn label="Login" class="button-center" color="teal"></q-btn>
        </q-form>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: "LoginView",
});
</script>

<style scoped>
.login-view{
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to left, #FFFFFF, #FFEFBA)
}

.login-view-form{
    min-width: 600px;
}

.margin-bottom{
    margin-bottom: 10px;
}

.button-center{
    margin: 0 auto;
    display: flex;
}
</style>