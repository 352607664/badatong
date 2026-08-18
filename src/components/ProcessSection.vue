<template>
  <section id="process" class="section process">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">服务流程</span>
        <h2 class="section-title">四步开启你的<span class="accent">巴西生意</span></h2>
        <p class="section-desc">流程清晰、节点明确，全程有人跟进，你只需安心做产品</p>
      </div>

      <div class="process__track">
        <template v-for="(p, i) in steps" :key="p.title">
          <div class="process__step" v-reveal :style="{ transitionDelay: i * 0.1 + 's' }">
            <div class="process__node">
              <span>{{ i + 1 }}</span>
            </div>
            <h3 class="process__title">{{ p.title }}</h3>
            <p class="process__desc">{{ p.desc }}</p>
            <span class="process__time">{{ p.time }}</span>
          </div>
          <div v-if="i < steps.length - 1" class="process__line" v-reveal :style="{ transitionDelay: i * 0.1 + 0.05 + 's' }">
            <svg width="26" height="14" viewBox="0 0 26 14" fill="none"><path d="M0 7h22M19 2l5 5-5 5" stroke="#00a25b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </div>
        </template>
      </div>
    </div>
  </section>
</template>

<script setup>
const steps = [
  { title: '需求沟通', desc: '了解你的经营类目与体量，定制注册方案（简易税制 / 预估利润制 / 中国法人店）与报价。', time: '第 1 天' },
  { title: '资料办理', desc: '协助准备护照、地址等材料，完成公证、翻译与海牙认证，全程指导。', time: '1 - 2 周' },
  { title: '主体注册', desc: '递交巴西公司注册申请，办理 CNPJ、法人及税务登记，法人配合 KYC 时效 12h-7 天。', time: '1 - 1.5 个月' },
  { title: '财税交付', desc: '交付公司资料与完税证明，按方案启动财税申报、进出口与商标等后续服务，长期陪跑。', time: '1 - 3 个工作日' }
]
</script>

<style scoped>
.process {
  background:
    radial-gradient(600px 300px at 50% 0%, rgba(0, 162, 91, 0.06), transparent 70%),
    var(--surface);
}

.process__track {
  display: flex;
  align-items: stretch;
  gap: 12px;
}

.process__step {
  flex: 1;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 30px 26px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: all 0.3s ease;
  position: relative;
}

.process__step:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-md);
  border-color: rgba(0, 162, 91, 0.35);
}

.process__node {
  width: 54px;
  height: 54px;
  margin: 0 auto 18px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #00b867, #00793f);
  color: #fff;
  font-size: 20px;
  font-weight: 800;
  box-shadow: 0 8px 18px rgba(0, 162, 91, 0.35);
  position: relative;
}

.process__node::after {
  content: '';
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px dashed rgba(0, 162, 91, 0.4);
  animation: spin 14s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.process__title {
  font-size: 17px;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 8px;
}

.process__desc {
  font-size: 13.5px;
  color: var(--text-2);
  line-height: 1.7;
  margin-bottom: 14px;
}

.process__time {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  color: var(--green-dark);
  background: var(--green-light);
  padding: 4px 12px;
  border-radius: 999px;
}

.process__line {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  flex-shrink: 0;
}

@media (max-width: 960px) {
  .process__track {
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }

  .process__step {
    width: 100%;
    max-width: 520px;
    padding: 24px 22px;
  }

  .process__line {
    transform: rotate(90deg);
    height: 26px;
  }
}

@media (max-width: 560px) {
  .process__step:hover {
    transform: none;
  }
}
</style>
