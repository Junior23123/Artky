import { defineStore } from "pinia";

import { Notify } from "quasar";

export const useStoreCart = defineStore("cart", {
  state: () => ({
    products: [],
  }),
  getters: {
    getProducts: (state) => state.products,
    getCountProducts: (state) => state.products.length,
  },
  actions: {
    addOneProduct(payload) {
      this.products.push(payload);
      Notify.create({
        message: "Se agrego el producto al carrito de compras",
        type: "success",
        position: "top-right",
      });
    },
    deleteOneProduct(payload) {
      this.products.filter((product) => product?.id != payload);
      Notify.create({
        message: "Se elimino el producto del carrito de compras",
        type: "negative",
        position: "top-right",
      });
    },
    deleteAllProducts() {
      this.products = [];
      Notify.create({
        message: "Se elimino todos los productos del carrito de compras",
        type: "negative",
        position: "top-right",
      });
    },
  },
});
