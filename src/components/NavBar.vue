<template>
  <header class="navbar" :class="{ 'navbar--scrolled': scrolled }">
    <div class="container navbar__inner">
      <a href="#home" class="navbar__brand">
        <img src="/logo.png" alt="巴达通 BADATONG" class="navbar__logo" />
        <span class="navbar__brand-text">
          <strong>巴达通</strong>
          <small>BADATONG · 巴西电商服务</small>
        </span>
      </a>

      <nav class="navbar__menu" :class="{ 'is-open': menuOpen }">
        <a v-for="item in menus" :key="item.href" :href="item.href" class="navbar__link" @click="closeMenu">
          {{ item.label }}
        </a>
        <a href="#contact" class="btn btn--primary navbar__cta" @click="closeMenu">
          立即咨询
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </nav>

      <button class="navbar__toggle" :class="{ 'is-active': menuOpen }" @click="menuOpen = !menuOpen" aria-label="菜单">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'

const menus = [
  { label: '首页', href: '#home' },
  { label: '核心业务', href: '#services' },
  { label: '方案报价', href: '#plans' },
  { label: '服务优势', href: '#why-us' },
  { label: '关于我们', href: '#about' },
  { label: '常见问题', href: '#faq' }
]

const scrolled = ref(false)
const menuOpen = ref(false)

const onScroll = () => {
  scrolled.value = window.scrollY > 20
}

const closeMenu = () => {
  menuOpen.value = false
}

const onResize = () => {
  if (window.innerWidth > 900) closeMenu()
}

watch(menuOpen, (open) => {
  document.body.classList.toggle('no-scroll', open)
})

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('resize', onResize, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('resize', onResize)
  document.body.classList.remove('no-scroll')
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  height: calc(var(--nav-h) + var(--safe-top));
  padding-top: var(--safe-top);
  background: rgba(255, 255, 255, 0.82);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid transparent;
  transition: all 0.3s ease;
}

.navbar--scrolled {
  background: rgba(255, 255, 255, 0.96);
  border-bottom-color: var(--line);
  box-shadow: 0 4px 24px rgba(11, 42, 107, 0.06);
}

.navbar__inner {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.navbar__brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.navbar__logo {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  flex-shrink: 0;
}

.navbar__brand-text {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}

.navbar__brand-text strong {
  font-size: 20px;
  font-weight: 800;
  color: var(--navy);
  letter-spacing: 1px;
}

.navbar__brand-text small {
  font-size: 10px;
  color: var(--text-3);
  letter-spacing: 0.6px;
  margin-top: 2px;
}

.navbar__menu {
  display: flex;
  align-items: center;
  gap: 6px;
}

.navbar__link {
  padding: 8px 14px;
  font-size: 15px;
  font-weight: 500;
  color: var(--text-2);
  border-radius: 8px;
  transition: all 0.2s ease;
}

.navbar__link:hover {
  color: var(--green-dark);
  background: var(--green-light);
}

.navbar__cta {
  margin-left: 12px;
  padding: 10px 22px;
  font-size: 14px;
  animation: ctaGlow 3s ease-in-out infinite;
}

@keyframes ctaGlow {
  0%, 100% { box-shadow: 0 4px 16px rgba(0, 162, 91, 0.28); }
  50% { box-shadow: 0 6px 22px rgba(0, 162, 91, 0.45); }
}

.navbar__toggle {
  display: none;
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: var(--green-light);
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
}

.navbar__toggle span {
  width: 18px;
  height: 2px;
  border-radius: 2px;
  background: var(--green-dark);
  transition: all 0.3s ease;
}

.navbar__toggle.is-active span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}
.navbar__toggle.is-active span:nth-child(2) {
  opacity: 0;
}
.navbar__toggle.is-active span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

@media (max-width: 900px) {
  .navbar__toggle {
    display: flex;
  }

  .navbar__brand-text small {
    display: none;
  }

  .navbar__menu {
    position: fixed;
    top: calc(var(--nav-h) + var(--safe-top));
    left: 0;
    right: 0;
    bottom: 0;
    flex-direction: column;
    align-items: stretch;
    gap: 4px;
    padding: 16px 24px calc(24px + var(--safe-bottom));
    background: #fff;
    border-bottom: 1px solid var(--line);
    box-shadow: var(--shadow-md);
    transform: translateY(-12px);
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }

  .navbar__menu.is-open {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }

  .navbar__link {
    padding: 14px 14px;
    font-size: 16px;
    min-height: 44px;
    display: flex;
    align-items: center;
  }

  .navbar__cta {
    margin: 10px 0 0;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .navbar__logo {
    width: 36px;
    height: 36px;
  }

  .navbar__brand-text strong {
    font-size: 17px;
  }
}
</style>
