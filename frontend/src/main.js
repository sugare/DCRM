import Vue from 'vue'
import App from './App.vue'

import store from './store/store'
import router from './router'
import axios from './http'
import jsonp from 'jsonp'

// bootstrap
import './static/bootstrap-3.3.7/css/bootstrap.min.css';

// echarts
import echarts from 'echarts';
Vue.prototype.$echarts = echarts

//iview ui
import Iview from 'iview'
import 'iview/dist/styles/iview.css'
Vue.use(Iview);

Vue.prototype.$iview = Iview;

Vue.prototype.$axios = axios;

Vue.prototype.$jsonp = jsonp;
new Vue({
  el: '#app',
  axios,
  router,
  store,
  jsonp,
  render: h => h(App)
})
