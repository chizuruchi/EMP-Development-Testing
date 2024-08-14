import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/emp',
    name: 'emp',
    component: () => import('../views/tlias/EmpView.vue')
  },
  {
    path: '/dep',
    name: 'dep',
    component: () => import('../views/tlias/DepView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/tlias/LoginView.vue')
  },
  {
    path: '/',
    redirect: '/login'
  },
]

const router = new VueRouter({
  routes
})

export default router
