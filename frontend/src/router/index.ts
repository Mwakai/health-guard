import { createRouter, createWebHistory } from 'vue-router'
import Landingpage from '../components/Landingpage.vue'
import Register from '../views/auth/Register.vue'
import Login from '../views/auth/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Landingpage',
    component: Landingpage
  },
  {
    path: '/auth/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/auth/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
