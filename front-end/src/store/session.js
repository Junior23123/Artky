import { defineStore } from "pinia";
import { login, create } from "@/api/login";
import { Notify } from "quasar";

export const useStoreSession = defineStore("session", {
  state: () => ({
    user: null,
  }),
  getters: {
    getIsLogin: (state) => state.user !== null,
    getUser: (state) => state.user,
  },
  actions: {
    async fetchLogin(params) {
      try {
       const userReponse = await login(params);
        this.user = userReponse.data?.data;

        return true;
      } catch (error) {
        if (error.response.status == 404) {
          Notify.create({
            type: "negative",
            message: "Usuario o contraseña incorrecta",
            position: "top-right",
          });
          return;
        }

        Notify.create({
          type: "negative",
          message: "Ocurrio un error en el servidor",
          position: "top-right",
        });
      }
    },

    async fetchCreateUser(params) {
      try {
        await create(params);
        return true
      } catch (error) {
        Notify.create({
          type: "negative",
          message: "Ocurrio un error en el servidor",
          position: "top-right",
        });
      }
    },
  },
});
