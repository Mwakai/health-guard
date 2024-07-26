import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

document.body.classList.add('light-mode')
createApp(App).use(router).mount('#app')
