<template>
    <div class="Register-view">
        <q-form class="Register-view-form">
            <h1 class="text-h2 text-center">Registro</h1>
            <h2 class="text-h4 text-center">Registrate para comprar</h2>
            <q-input label="Nombre" class="margin-bottom"></q-input>
            <q-input label="Apellido" class="margin-bottom"></q-input>        
            <q-input label="Correo" class="margin-bottom"></q-input>
            <q-input label="Contraseña" class="margin-bottom"></q-input>   
            <q-btn label="Register" class="button-center" color="teal"></q-btn>
        </q-form>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: "RegistroView",
});
</script>

<style scoped>
.Register-view{
    height: 100vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to left, #FFFFFF, #FFEFBA)
}

.Register-view-form{
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