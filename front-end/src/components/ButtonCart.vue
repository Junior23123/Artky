<template>
  <q-btn icon="shopping_cart" flat fab-mini  @click="handleClickCart">
    <q-badge rounded color="red" floating>{{
      cartStore.getCountProducts
    }}</q-badge>
  </q-btn>
</template>

<script>
import { defineComponent } from "vue";
import { useStoreCart } from "@/store/cart";
import { Notify } from "quasar";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ButtonCart",
  setup() {
    const cartStore = useStoreCart();
    const router = useRouter()

    const handleClickCart = () => {
        
      if (cartStore.getCountProducts === 0) {
        Notify.create({
          message: "No hay productos en el carrito de compras",
          type: "warning",
          position:'top-right',
          timeout:1000
        });

        return;
      }

      router.push('/cart-shopping')
    };

    return { cartStore, handleClickCart };
  },
});
</script>
