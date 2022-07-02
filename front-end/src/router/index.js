import { createRouter, createWebHashHistory } from 'vue-router'
import Mainlayout from '../layout/Mainlayout.vue'
import LoginView from '../views/LoginView.vue';
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
        }
      ]
    },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
