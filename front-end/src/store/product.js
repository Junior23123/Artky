import { defineStore } from "pinia";
import { Notify } from "quasar";
import { createProduct, deleteProduct, getProducts } from "@/api/product";

export const useStoreProduct = defineStore("product", {
  state: () => ({
    products: [],
  }),
  getters: {
    getProducts: (state) => state.products,
  },
  actions: {
    async fetchCreateProduct(payload) {
      try {
        await createProduct(payload);
        Notify.create({
          message: "Se agrego el producto",
          type: "positive",
          position: "top-right",
        });

        return true;
      } catch (error) {
        Notify.create({
          message: "Ocurrio un error",
          type: "negative",
          position: "top-right",
        });
      }
    },

    async fetchGetProducts() {
      try {
        const response = await getProducts();
        this.products = response?.data;
      } catch (error) {
        Notify.create({
          message: "Ocurrio un error",
          type: "negative",
          position: "top-right",
        });
      }
    },

    async fetchDeleteProduct(id) {
      try {
        await deleteProduct(id);
        Notify.create({
          message: "Producto eliminado",
          type: "positive",
          position: "top-right",
        });
      } catch (error) {
        Notify.create({
          message: "Ocurrio un error",
          type: "negative",
          position: "top-right",
        });
      }
    },
  },
});
