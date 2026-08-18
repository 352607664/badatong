<template>
  <section id="home" class="hero">
    <div class="hero__deco hero__deco--1"></div>
    <div class="hero__deco hero__deco--2"></div>
    <div class="hero__deco hero__deco--3"></div>

    <div class="container hero__inner">
      <div class="hero__content">
        <span class="hero__badge">
          <span class="hero__badge-dot"></span>
          巴西籍华人老板直营 · 家族深耕巴西 50 年 · 一站式合规服务
        </span>

        <h1 class="hero__title">
          助你合规<span class="hero__title-accent">掘金巴西</span><br />
          电商万亿市场
        </h1>

        <p class="hero__desc">
          巴达通由<strong>巴西籍华人老板</strong>创办，家族深耕巴西市场 50 余年，
          提供<strong>巴西本土公司注册</strong>（简易税制 / 预估利润制 / 中国法人店）、
          <strong>财税方案</strong>、<strong>进出口资质</strong>（无限额度 · 自行清关）与<strong>商标注册</strong>、<strong>三大认证（ANVISA、INMETRO、ANATEL）</strong>全链路服务。
          法人配合快、税务实缴合规，法人或者税务问题<strong>最高 20 万元质保赔付</strong>。
        </p>

        <div class="hero__actions">
          <a href="#contact" class="btn btn--primary">
            免费咨询方案
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a href="#services" class="btn btn--ghost">了解核心业务</a>
        </div>

        <div class="hero__stats">
          <div class="hero__stat">
            <strong>50<em>年+</em></strong>
            <span>家族深耕巴西市场</span>
          </div>
          <div class="hero__stat hero__stat--highlight">
            <strong>20<em>万</em></strong>
            <span>最高质保赔付（元）</span>
          </div>
          <div class="hero__stat">
            <strong>1-1.5<em>个月</em></strong>
            <span>主体店交付时效</span>
          </div>
        </div>
      </div>

      <div class="hero__visual">
        <div class="hero__card hero__card--main">
          <div class="hero__card-top">
            <span class="hero__flag">
              <span class="hero__flag-green"></span>
              <span class="hero__flag-yellow"></span>
              <span class="hero__flag-blue"></span>
            </span>
            <span class="hero__card-title">巴西本土公司</span>
            <span class="hero__card-status">已合规</span>
          </div>
          <div class="hero__card-body">
            <div class="hero__card-row">
              <span class="hero__card-label">注册主体</span>
              <span class="hero__card-value">CNPJ 巴西公司</span>
            </div>
            <div class="hero__card-row">
              <span class="hero__card-label">法人情况</span>
              <span class="hero__card-value tag-green">工厂员工 · 家属</span>
            </div>
            <div class="hero__card-row">
              <span class="hero__card-label">税务状态</span>
              <span class="hero__card-value tag-green">实缴申报 · 完税证明</span>
            </div>
            <div class="hero__card-row">
              <span class="hero__card-label">交付时效</span>
              <span class="hero__card-value">1 - 1.5 个月</span>
            </div>
            <div class="hero__card-row">
              <span class="hero__card-label">质保赔付</span>
              <span class="hero__card-value tag-green">最高 20 万元</span>
            </div>
          </div>
          <div class="hero__card-foot">
            <span class="hero__card-progress"></span>
            <span>全流程进度 100%</span>
          </div>
        </div>

        <div class="hero__chip hero__chip--1">
          <span class="hero__chip-ic">📋</span>
          <div><strong>财税方案</strong><small>实缴申报 · 完税证明</small></div>
        </div>
        <div class="hero__chip hero__chip--2">
          <span class="hero__chip-ic">🚢</span>
          <div><strong>进出口资质</strong><small>无限额度 · 自行清关</small></div>
        </div>
        <div class="hero__chip hero__chip--3">
          <span class="hero__chip-ic">✅</span>
          <div><strong>主体交付</strong><small>1 个月 - 1 个半月</small></div>
        </div>
      </div>
    </div>

    <div class="hero__bottom">
      <svg width="100%" height="60" viewBox="0 0 1440 60" preserveAspectRatio="none" style="display:block"><path d="M0,60 L0,30 Q360,0 720,25 T1440,18 L1440,60 Z" fill="#ffffff"/></svg>
    </div>
  </section>
</template>

<script setup>
// 首屏视觉组件
</script>

<style scoped>
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: calc(var(--nav-h) + var(--safe-top) + 40px);
  background:
    radial-gradient(900px 420px at 85% -10%, rgba(254, 203, 0, 0.16), transparent 60%),
    radial-gradient(700px 500px at 10% 10%, rgba(0, 162, 91, 0.1), transparent 60%),
    linear-gradient(180deg, #f2faf6 0%, #f6f9f8 100%);
  overflow: hidden;
}

.hero__deco {
  position: absolute;
  border-radius: 50%;
  filter: blur(2px);
  opacity: 0.55;
  pointer-events: none;
}

.hero__deco--1 {
  width: 420px;
  height: 420px;
  right: -140px;
  top: -120px;
  background: radial-gradient(circle, rgba(0, 162, 91, 0.14), transparent 65%);
}

.hero__deco--2 {
  width: 300px;
  height: 300px;
  left: -100px;
  bottom: 8%;
  background: radial-gradient(circle, rgba(254, 203, 0, 0.18), transparent 65%);
}

.hero__deco--3 {
  width: 160px;
  height: 160px;
  right: 22%;
  bottom: 16%;
  background: radial-gradient(circle, rgba(11, 42, 107, 0.08), transparent 65%);
}

.hero__inner {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: 56px;
  padding-bottom: 60px;
}

.hero__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 18px;
  border-radius: 999px;
  background: #fff;
  border: 1px solid rgba(0, 162, 91, 0.25);
  color: var(--green-dark);
  font-size: 13px;
  font-weight: 600;
  box-shadow: var(--shadow-sm);
  margin-bottom: 24px;
}

.hero__badge-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--green);
  animation: pulse 1.8s ease infinite;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 162, 91, 0.45); }
  50% { box-shadow: 0 0 0 6px rgba(0, 162, 91, 0); }
}

.hero__title {
  font-size: clamp(34px, 4.6vw, 56px);
  font-weight: 800;
  line-height: 1.22;
  color: var(--navy);
  letter-spacing: 1px;
}

.hero__title-accent {
  position: relative;
  background: linear-gradient(135deg, var(--green) 0%, #00c471 50%, var(--green-dark) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  white-space: nowrap;
}

.hero__title-accent::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 4px;
  height: 10px;
  background: rgba(254, 203, 0, 0.5);
  z-index: -1;
  border-radius: 4px;
}

.hero__desc {
  margin-top: 22px;
  font-size: 17px;
  color: var(--text-2);
  max-width: 540px;
}

.hero__desc strong {
  color: var(--green-dark);
}

.hero__actions {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 32px;
  flex-wrap: wrap;
}

.hero__stats {
  display: flex;
  gap: 20px;
  margin-top: 44px;
}

.hero__stat {
  display: flex;
  flex-direction: column;
  padding: 18px 22px;
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  box-shadow: var(--shadow-sm);
  flex: 1;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.hero__stat:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.hero__stat--highlight {
  background: linear-gradient(135deg, rgba(255, 247, 214, 0.95), rgba(255, 255, 255, 0.85));
  border-color: rgba(254, 203, 0, 0.35);
}

.hero__stat--highlight strong {
  color: var(--green-dark);
}

.hero__stat strong {
  font-size: 30px;
  font-weight: 800;
  color: var(--navy);
}

.hero__stat strong em {
  font-style: normal;
  color: var(--green);
  font-size: 20px;
  margin-left: 1px;
}

.hero__stat span {
  font-size: 13px;
  color: var(--text-3);
  margin-top: 2px;
}

/* ---------- 右侧视觉 ---------- */
.hero__visual {
  position: relative;
  min-height: 460px;
}

.hero__card--main {
  position: absolute;
  right: 6%;
  top: 40px;
  width: 360px;
  max-width: 88%;
  border-radius: 20px;
  padding: 22px;
  background: #fff;
  border: 1px solid var(--line);
  box-shadow: var(--shadow-lg);
  transform: rotate(1.5deg);
  animation: cardEnter 0.8s ease 0.2s both;
}

@keyframes cardEnter {
  from {
    opacity: 0;
    transform: rotate(1.5deg) translateY(24px);
  }
  to {
    opacity: 1;
    transform: rotate(1.5deg) translateY(0);
  }
}

.hero__card-top {
  display: flex;
  align-items: center;
  gap: 10px;
}

.hero__flag {
  width: 44px;
  height: 30px;
  border-radius: 5px;
  overflow: hidden;
  position: relative;
  display: block;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  flex-shrink: 0;
}

.hero__flag-green { position: absolute; inset: 0; background: #009c3b; }
.hero__flag-yellow {
  position: absolute;
  inset: 6px 0;
  background: #ffdf00;
  clip-path: polygon(0 50%, 100% 0, 100% 100%);
}
.hero__flag-blue {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 12px;
  height: 12px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  background: #002776;
}

.hero__card-title {
  font-weight: 700;
  font-size: 15px;
  color: var(--navy);
  flex: 1;
}

.hero__card-status {
  font-size: 11px;
  font-weight: 700;
  color: var(--green-dark);
  background: var(--green-light);
  padding: 3px 10px;
  border-radius: 999px;
}

.hero__card-body {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.hero__card-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  background: #f7faf9;
  border-radius: 10px;
}

.hero__card-label {
  font-size: 13px;
  color: var(--text-3);
}

.hero__card-value {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
}

.tag-green {
  color: var(--green-dark);
}

.hero__card-foot {
  margin-top: 16px;
  padding: 12px 14px;
  border-radius: 10px;
  background: var(--yellow-light);
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12px;
  font-weight: 600;
  color: #8a6d00;
}

.hero__card-progress {
  flex: 1;
  height: 6px;
  border-radius: 3px;
  background: #ffe9a8;
  position: relative;
  overflow: hidden;
}

.hero__card-progress::after {
  content: '';
  position: absolute;
  inset: 0;
  width: 100%;
  border-radius: 3px;
  background: linear-gradient(90deg, var(--yellow), #ffd84d);
}

/* 浮动标签 */
.hero__chip {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 10px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 12px 16px;
  box-shadow: var(--shadow-md);
  animation: float 5s ease-in-out infinite;
}

.hero__chip-ic {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  display: grid;
  place-items: center;
  font-size: 18px;
  background: var(--green-light);
}

.hero__chip strong {
  display: block;
  font-size: 14px;
  color: var(--navy);
}

.hero__chip small {
  font-size: 11px;
  color: var(--text-3);
}

.hero__chip--1 { left: 2%; top: 12%; animation-delay: 0s; }
.hero__chip--2 { left: 0; bottom: 14%; animation-delay: 1.2s; }
.hero__chip--3 { right: 0; top: 52%; animation-delay: 2.1s; }

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.hero__bottom {
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  z-index: 3;
  line-height: 0;
}

/* 响应式 */
@media (max-width: 960px) {
  .hero__inner {
    grid-template-columns: 1fr;
    gap: 40px;
    padding-bottom: 80px;
  }

  .hero {
    min-height: auto;
    padding-top: calc(var(--nav-h) + var(--safe-top) + 24px);
  }

  .hero__visual {
    min-height: 400px;
    margin: 0 auto;
    width: 100%;
    max-width: 560px;
  }

  .hero__card--main {
    right: 0;
    left: 50%;
    transform: translateX(-50%) rotate(1.5deg);
  }

  .hero__chip--1 { left: 0; }
  .hero__chip--2 { left: 0; }
}

@media (max-width: 560px) {
  .hero__badge {
    font-size: 12px;
    padding: 7px 14px;
    line-height: 1.5;
    text-align: left;
  }

  .hero__title {
    letter-spacing: 0;
  }

  .hero__desc {
    font-size: 15px;
    margin-top: 18px;
  }

  .hero__actions {
    flex-direction: column;
    align-items: stretch;
    gap: 10px;
  }

  .hero__actions .btn {
    width: 100%;
    justify-content: center;
  }

  .hero__stats {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin-top: 32px;
  }

  .hero__stat {
    padding: 14px 16px;
  }

  .hero__stat:last-child {
    grid-column: 1 / -1;
  }

  .hero__stat:hover {
    transform: none;
  }

  .hero__stat strong {
    font-size: 24px;
  }

  .hero__visual {
    min-height: 340px;
  }

  .hero__card--main {
    width: 100%;
    max-width: 320px;
    padding: 18px;
  }

  .hero__card-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
    padding: 8px 12px;
  }

  .hero__chip {
    padding: 8px 10px;
    max-width: 140px;
  }

  .hero__chip strong {
    font-size: 12px;
  }

  .hero__chip small {
    font-size: 10px;
  }

  .hero__chip-ic {
    width: 28px;
    height: 28px;
    font-size: 14px;
  }

  .hero__chip--3 {
    display: none;
  }
}

@media (max-width: 380px) {
  .hero__chip--2 {
    display: none;
  }

  .hero__visual {
    min-height: 300px;
  }
}
</style>
