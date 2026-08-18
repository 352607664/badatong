<template>
  <a
    v-show="visible"
    href="#contact"
    class="floating-cta btn btn--primary"
    aria-label="免费咨询方案"
  >
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
    免费咨询
  </a>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const visible = ref(false)

const onScroll = () => {
  visible.value = window.scrollY > 480
}

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
.floating-cta {
  display: none;
  position: fixed;
  right: 16px;
  bottom: calc(20px + var(--safe-bottom));
  z-index: 90;
  padding: 14px 22px;
  font-size: 14px;
  box-shadow: 0 8px 28px rgba(0, 162, 91, 0.45);
  animation: slideUp 0.4s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .floating-cta {
    display: inline-flex;
  }
}
</style>
