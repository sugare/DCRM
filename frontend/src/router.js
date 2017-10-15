import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store/store'
import * as types from './store/types'

import Layout from './components/Layout.vue'
import Root from './components/root.vue'
import Dashboard from './components/dashboard.vue'
import Customers from './components/customers.vue'
import Login from './components/login.vue'
import Test from './components/test.vue'
import Error404 from './components/error404.vue'
import Uploadhead from './components/uploadHead.vue'
import Settings from './components/settings.vue'

Vue.use(VueRouter)

import iView from 'iview';

const routes = [
        {  
          path: '/',
          component: Layout,
          redirect: '/dashboard',
          children: [
            {
                path: '/dashboard',
                component: Dashboard,
                meta: {
                    requireAuth: true,
                }
            },
            {
                path: 'settings',
                component: Settings,
                meta: {
                    requireAuth: true,
                }
            },
            {
                path: 'customers',
                component: Customers,
                meta: {
                    requireAuth: true,
                }
            }
          ]
        },
        {
            path: '/login',
            component: Login
        }
];


// 页面刷新时，重新赋值token
if (window.localStorage.getItem('token')) {
    store.commit(types.LOGIN, window.localStorage.getItem('token'));
    store.commit(types.USER, JSON.parse(window.localStorage.getItem('user')));
}

const router = new VueRouter({
    mode: 'history',
    routes

});

// router.addRoutes([{
//     path: '/add',
//     component: Vue.extend({
//         template: '<div>add</div>'
//     })
// }]);

router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    if (to.matched.some(r => r.meta.requireAuth)) {
        if (store.state.token) {
            next()
        }
        else {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            })
        }
    }
    else {

        if (store.state.token) {
            if (to.path === '/login') {
                next({ path: '/' })
            }
        } else {
            next()
        }
    }
});

router.afterEach((to, from, next) => {
    iView.LoadingBar.finish();
});
export default router;