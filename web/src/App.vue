<template>
  <header>
  </header>
  <magic-menu v-if="$route.name !== 'login'"></magic-menu>
  <div v-else style="height: 100%;">
    <login></login>
  </div>
</template>

<script lang="ts" setup>
import MagicMenu from './components/magicMenu/index.vue'
import Login from './views/auth/LoginView.vue'
</script>
<style>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

.h-screen-header {
  height: calc(100vh - 70px);
}
.h-screen-2header {
  height: calc(100vh - 150px);
}
</style>
