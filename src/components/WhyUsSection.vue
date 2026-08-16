<template>
  <section id="why-us" class="section why-us">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">服务优势</span>
        <h2 class="section-title">为什么选择<span class="accent">巴达通</span>？</h2>
        <p class="section-desc">巴西籍华人老板直营，家族深耕巴西 50 年，法人配合快、财税真实合规、质保兜底</p>
      </div>

      <div class="why-us__grid">
        <article v-for="(w, i) in reasons" :key="w.title" class="card why" v-reveal :style="{ transitionDelay: i * 0.07 + 's' }">
          <div class="why__num">0{{ i + 1 }}</div>
          <h3 class="why__title">{{ w.title }}</h3>
          <p class="why__desc">{{ w.desc }}</p>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
const reasons = [
  { title: '巴西籍华人老板直营', desc: '创始人林晓懋，巴西籍华人、巴西第一代华人，家族生意深耕巴西市场 50 余年，本人一线经营本土服装电商与工厂，一手资源、无中间商。' },
  { title: '法人配合快，KYC 12h-7 天', desc: '法人均为工厂员工及家属，配合程度高，除周末外 KYC 平均配合时效 12 小时至 7 天以内，认证不卡壳、不误事。' },
  { title: '最高 20 万元质保兜底', desc: '质保期内公司与税务出问题，Pago、公户钱包与 Full 仓货物协助拿回，拿不回最高赔付 20 万元/次，合同白纸黑字。' },
  { title: '税务实缴 · 完税证明齐全', desc: '财税一体化管理，税务实缴申报、完税证明齐全；进出口资质无限额度、自行清关，合规看得见。' }
]
</script>

<style scoped>
.why-us__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.why {
  padding: 30px 26px;
  border-radius: 18px;
  position: relative;
  overflow: hidden;
}

.why::before {
  content: '';
  position: absolute;
  right: -30px;
  top: -30px;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: var(--green-light);
  opacity: 0.6;
}

.why__num {
  font-size: 34px;
  font-weight: 800;
  color: var(--green);
  opacity: 0.35;
  margin-bottom: 16px;
  font-family: Georgia, serif;
}

.why__title {
  font-size: 18px;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 10px;
}

.why__desc {
  font-size: 14px;
  color: var(--text-2);
  line-height: 1.75;
}

@media (max-width: 960px) {
  .why-us__grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 560px) {
  .why-us__grid {
    grid-template-columns: 1fr;
  }
}
</style>
