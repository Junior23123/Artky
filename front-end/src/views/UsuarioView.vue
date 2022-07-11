<template>
  <div class="usuario">
    <div class="usuario-title">Interfaz de compra</div>

    <div class="usuario-message-welcome">
      Bienvenid@, {{ storeSession.getUser?.name || "" }}
    </div>

    <div class="usuario-category">
      <img
        v-for="(image, index) in images"
        :key="index"
        class="usuario-category-item"
        :src="image"
        alt="image-category"
      />
    </div>

    <div class="usuario-table">
      <q-table :columns="columns"></q-table>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { useStoreSession } from "@/store/session";

export default defineComponent({
  name: "UsuarioView",
  setup() {
    const images = [
      "https://greenhouse.com.pe/1228-large_default/torito-de-pucara-negro-con-suculenta.jpg",
      "https://gestion.pe/resizer/uGATgJL3yYS8LcrBIExf4jDrtFA=/1200x1200/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/ZBKVBH3SZVH3NGXZUHY4PBAS4E.JPG",
      "https://pbs.twimg.com/media/ElXRwMMX0AAoM96.png",
    ];

    const columns = [
      {
        name: "id",
        field: "id",
        label: "#",
      },
      {
        name: "product",
        field: "product",
        label: "Producto",
      },
      {
        name: "price",
        field: "price",
        label: "Precio",
      },
      {
        name: "buy",
        field: "buy",
        label: "Comprar",
      },
    ];

    const storeSession = useStoreSession();
    return { images, storeSession,columns };
  },
});
</script>

<style scoped>
.usuario {
  padding: 30px;
}
.usuario-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.usuario-message-welcome {
  font-size: 1rem;
  margin-bottom: 20px;
}

.usuario-category {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.usuario-category-item {
  height: 200px;
  width: 100%;
  background-size: auto;
  background-position: center;
}
</style>
