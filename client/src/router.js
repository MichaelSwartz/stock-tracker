import Vue from 'vue';
import Router from 'vue-router';
import Stocks from './components/Stocks.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Stocks',
      component: Stocks,
    },
  ],
});
