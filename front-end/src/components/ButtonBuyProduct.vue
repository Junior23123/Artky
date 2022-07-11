<template>
  <q-btn v-bind="$attrs" @click="handleBuyProduct" />
</template>

<script>
import { defineComponent } from "vue";
import { useStoreSession } from "@/store/session";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ButtonLogout",
  props: {
    path: {
      type: String,
      default: "/catalogo",
    },
  },
  setup(props) {
    const sessionStore = useStoreSession();
    const router = useRouter();

    const handleBuyProduct = () => {
      if (sessionStore.getIsLogin) {
        router.push({ path: props.path });
      } else {
        router.push({ path: "/login" });
      }
    };
    return { handleBuyProduct };
  },
});
</script>

