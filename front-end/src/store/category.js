import { defineStore } from "pinia";
import { Notify } from "quasar";
import { createCategory, getCategories } from "@/api/category";

export const useStoreCategory = defineStore("category", {
  state: () => ({
    categories: [],
  }),
  getters: {
    getCategories: (state) => state.categories,
  },
  actions: {
    async fetchCreateCategory(payload) {
      try {
        await createCategory(payload);
        Notify.create({
          message: "Se agrego la categoria",
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

    async fetchGetCategories() {
      try {
        const response = await getCategories();
        this.categories = response?.data;
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
