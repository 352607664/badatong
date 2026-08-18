<template>
  <div class="trust-bar">
    <div class="container trust-bar__inner">
      <span class="trust-bar__label">全平台代开</span>
      <div class="trust-bar__track">
        <div class="trust-bar__scroll">
          <span v-for="(p, i) in platforms" :key="i" class="trust-bar__item">{{ p }}</span>
          <span v-for="(p, i) in platforms" :key="'dup-' + i" class="trust-bar__item" aria-hidden="true">{{ p }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const platforms = [
  'Mercado Libre 美客多',
  'Amazon 亚马逊',
  'Shopee',
  'TEMU',
  'SHEIN',
  'TikTok Shop',
  'Kwai',
  'AliExpress 速卖通'
]
</script>

<style scoped>
.trust-bar {
  background: var(--surface);
  border-bottom: 1px solid var(--line);
  padding: 18px 0;
  overflow: hidden;
}

.trust-bar__inner {
  display: flex;
  align-items: center;
  gap: 24px;
}

.trust-bar__label {
  flex-shrink: 0;
  font-size: 12px;
  font-weight: 700;
  color: var(--green-dark);
  background: var(--green-light);
  padding: 6px 14px;
  border-radius: 999px;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.trust-bar__track {
  flex: 1;
  overflow: hidden;
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.trust-bar__scroll {
  display: flex;
  gap: 32px;
  width: max-content;
  animation: marquee 28s linear infinite;
}

.trust-bar__item {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-2);
  white-space: nowrap;
  opacity: 0.85;
}

@keyframes marquee {
  to { transform: translateX(-50%); }
}

@media (max-width: 768px) {
  .trust-bar {
    padding: 14px 0;
  }

  .trust-bar__inner {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .trust-bar__track {
    width: 100%;
  }

  .trust-bar__item {
    font-size: 13px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .trust-bar__scroll {
    animation: none;
    flex-wrap: wrap;
    width: auto;
    gap: 12px 20px;
  }

  .trust-bar__scroll span[aria-hidden="true"] {
    display: none;
  }

  .trust-bar__track {
    mask-image: none;
    -webkit-mask-image: none;
  }
}
</style>
