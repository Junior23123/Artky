<template>
  <div class="item-product">
    <img class="item-product-image" :src="img" :alt="name" />
    <div class="item-product-information">
      <div class="text-h4">
        {{ name }}
      </div>
      <div class="text-h6">
        {{ `Tamaño: ${size} | ${build}` }}
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ItemProduct",
  props: {
    name: {
      type: String,
      default: "",
    },
    size: {
      type: String,
      default: "",
    },
    build: {
      type: String,
      default: "",
    },
    img: {
      type: String,
      default: "",
    },
  },
});
</script>

<style scoped>
.item-product {
  display: flex;
  gap: 20px;
  border-bottom: 1px dashed grey;
  align-items: center;
  padding: 20px 0;
  margin-bottom: 30px;
}

.item-product-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
</style>
