import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Meta from 'vue-meta'

Vue.use(Router);
Vue.use(Meta)

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [{
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/myinteresting",
      name: "myinteresting",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/MyInteresting.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Login.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/SignUp.vue")
    },
    {
      path: "/signupquestion",
      name: "signupquestion",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/SignUpQuestion.vue")
    },
    {
      path: "*",
      name: "Error",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Error.vue")
    },
    {
      path: "/map",
      name: "map",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Map.vue")
    },

  ]
});
