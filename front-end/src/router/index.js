import { createRouter, createWebHashHistory } from 'vue-router';
import Mainlayout from '../layout/Mainlayout.vue';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
const routes = [
    {
      path:'/',
      name:'Mainlayout',
      component:Mainlayout,
      children:[
        {
          path: 'Login',
          name: 'Login',
          component: LoginView,
        },
        {
          path: 'Register',
          name: 'Register',
          component: RegisterView,
        },
      ]
    },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
