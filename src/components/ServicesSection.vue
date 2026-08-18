<template>
  <section id="services" class="section services">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">核心业务</span>
        <h2 class="section-title">四大核心服务，<span class="accent">一站式</span>搞定巴西经营</h2>
        <p class="section-desc">从公司设立、财税合规到进出口与商标，巴达通深耕中巴贸易领域，专业团队为你省心省力</p>
      </div>

      <div class="services__grid">
        <article v-for="(s, i) in services" :key="s.title" class="card service" :class="{ 'service--featured': i === 0 }" v-reveal :style="{ transitionDelay: i * 0.08 + 's' }">
          <div class="service__icon" :style="{ background: s.bg, color: s.color }">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path v-for="p in s.icon" :key="p" :d="p" />
            </svg>
          </div>
          <h3 class="service__title">{{ s.title }}</h3>
          <p class="service__desc">{{ s.desc }}</p>
          <ul class="service__list">
            <li v-for="f in s.features" :key="f">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
              {{ f }}
            </li>
          </ul>
          <a href="#contact" class="service__link">
            立即咨询
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  {
    title: '巴西本土公司注册',
    desc: '代办巴西本土公司（CNPJ）设立，简易税制、预估利润制、中国法人店等方案可选，法人配合度高，主体 1-1.5 个月交付。',
    icon: ['M3 21h18', 'M5 21V7l7-4 7 4v14', 'M9 9h1', 'M9 13h1', 'M9 17h1', 'M14 9h1', 'M14 13h1', 'M14 17h1'],
    bg: 'linear-gradient(135deg, #e6f7ee, #d2f0e0)',
    color: '#00793f',
    features: ['简易税制 / 预估利润制 / 中国法人店', '法人均为工厂员工及家属，配合度高', '主体 1-1.5 个月交付', '最高 20 万元质保赔付']
  },
  {
    title: '巴西公司财税方案',
    desc: '财税一体化管理，税务实缴申报、完税证明齐全，根据经营体量定制最划算的合规报税方案。',
    icon: ['M12 2v20', 'M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6', 'M12 2l5 3', 'M12 22l-5-3'],
    bg: 'linear-gradient(135deg, #fff7d6, #ffefb3)',
    color: '#a87b00',
    features: ['税务实缴申报，完税证明齐全', '简易税制梯度 / 预估利润制统筹', '月度记账报税、PIS/COFINS 核算', '财税一体化合规管理']
  },
  {
    title: '巴西进出口资质',
    desc: '协助取得巴西进出口资质（无限额度），自行清关，含清关服务的海外仓支持，货物高效流转。',
    icon: ['M3 6h13l4 4 1 4H9l-6-3z', 'M9 18h12', 'M5 18h2', 'M3 2v4', 'M7 2v4', 'M5 4h2'],
    bg: 'linear-gradient(135deg, #e8eefb, #d9e4f8)',
    color: '#0b2a6b',
    features: ['进出口资质办理（无限额度）', '自行清关，自主掌控时效', '海外仓含清关服务，快速上架', '货盘系统与逆向物流支持']
  },
  {
    title: '巴西商标注册',
    desc: '全类目商标申请注册，专业团队办理，快速保护品牌权益，让品牌在巴西市场立足无忧。',
    icon: ['M9 3h6l1 7-4 4-4-4z', 'M9 14v7', 'M15 14v7', 'M7 21h10'],
    bg: 'linear-gradient(135deg, #fdeef0, #fadfe3)',
    color: '#c2405a',
    features: ['巴西全类目商标注册', '专业查询与雷同规避', 'R 标申请一站式代办', '品牌权益全方位保护']
  }
]
</script>

<style scoped>
.services {
  background: var(--surface);
}

.services__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.service {
  padding: 34px 30px;
  display: flex;
  flex-direction: column;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
}

.service::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--green), var(--yellow));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.service:hover::before,
.service--featured::before {
  opacity: 1;
}

.service--featured {
  border-color: rgba(0, 162, 91, 0.25);
  background: linear-gradient(180deg, #f8fdf9 0%, #fff 40%);
}

.service--featured::after {
  content: '热门';
  position: absolute;
  top: 16px;
  right: 16px;
  font-size: 11px;
  font-weight: 700;
  color: var(--green-dark);
  background: var(--green-light);
  padding: 3px 10px;
  border-radius: 999px;
}

.service__icon {
  width: 62px;
  height: 62px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  margin-bottom: 22px;
}

.service__title {
  font-size: 21px;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 10px;
}

.service__desc {
  font-size: 14.5px;
  color: var(--text-2);
  line-height: 1.7;
}

.service__list {
  margin-top: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex: 1;
}

.service__list li {
  display: flex;
  align-items: flex-start;
  gap: 9px;
  font-size: 14px;
  color: var(--text-2);
}

.service__list svg {
  color: var(--green);
  margin-top: 4px;
  flex-shrink: 0;
}

.service__link {
  margin-top: 24px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  font-weight: 600;
  color: var(--green-dark);
  transition: gap 0.2s ease;
}

.service__link:hover {
  gap: 10px;
}

@media (max-width: 960px) {
  .services__grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
  }

  .service {
    padding: 28px 24px;
  }
}

@media (max-width: 640px) {
  .services__grid {
    grid-template-columns: 1fr;
    max-width: 520px;
    margin: 0 auto;
  }

  .service__title {
    font-size: 19px;
  }
}
</style>
