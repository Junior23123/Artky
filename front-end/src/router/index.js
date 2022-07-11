import { createRouter, createWebHistory } from "vue-router";
import Mainlayout from "../layout/Mainlayout.vue";
import AdminLayout from "../layout/AdminLayout.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import HomeView from "../views/HomeView.vue";
import CatalogueView from "../views/CatalogueView.vue";
import UsuarioView from "../views/UsuarioView.vue";

import { useStoreSession } from "@/store/session";
const routes = [
  {
    path: "/",
    name: "Mainlayout",
    component: Mainlayout,
    redirect: () => ({ name: "Home" }),
    children: [
      {
        path: "",
        name: "Home",
        component: HomeView,
      },
      {
        path: "Login",
        name: "Login",
        component: LoginView,
      },
      {
        path: "Register",
        name: "Register",
        component: RegisterView,
      },
      {
        path: "catalogo",
        name: "catalogo",
        component: CatalogueView,
      },
    ],
  },
  {
    path: "/admin",
    name: "AdminLayout",
    component: AdminLayout,
    redirect: () => ({ name: "HomeAdmin" }),
    children: [
      {
        path: "",
        name: "HomeAdmin",
        component: UsuarioView,
      },
      {
        path: "register",
        name: "RegisterAdmin",
        component: RegisterView,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const storeSession = useStoreSession();

  if (to.path === "/login" && storeSession.getIsLogin) {
    next({ path: "/" });
    return;
  }

  if (
    !storeSession.getIsAdmin &&
    ["AdminLayout", "HomeAdmin", "RegisterAdmin"].includes(to.name)
  ) {
    next({ path: "/" });
  }

  next();
});

export default router;
