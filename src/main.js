import { createApp } from 'vue'
import App from './App.vue'
import './assets/styles/main.css'

// 滚动出现动画指令
const revealDirective = {
  mounted(el) {
    el.classList.add('reveal')
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            el.classList.add('is-visible')
            observer.unobserve(el)
          }
        })
      },
      { threshold: 0.12 }
    )
    observer.observe(el)
  }
}

createApp(App).directive('reveal', revealDirective).mount('#app')
