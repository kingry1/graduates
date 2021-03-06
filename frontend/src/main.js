// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import axios from 'axios'
import VueAxios from 'vue-axios'
import Card from './components/Card'
import _ from 'lodash';

Object.defineProperty(Vue.prototype, '_', { value: _ });

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App, Card },
  template: '<App/>'
});
