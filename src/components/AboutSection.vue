<template>
  <section id="about" class="section about">
    <div class="container about__inner">
      <div class="about__visual" v-reveal>
        <div class="about__card-main">
          <div class="about__card-head">
            <img src="/logo.png" alt="巴达通 BADATONG" class="about__logo" />
            <div>
              <strong>巴达通 BADATONG</strong>
              <small>巴西籍华人创办 · 巴西电商一站式服务商</small>
            </div>
          </div>
          <p class="about__quote">
            「让中国卖家在巴西做得更简单、更合规、更长久。」
          </p>
          <div class="about__tags">
            <span>本土公司注册</span>
            <span>财税方案</span>
            <span>进出口资质</span>
            <span>商标注册</span>
          </div>
        </div>
        <div class="about__badge">
          <strong>50年+</strong>
          <span>家族深耕巴西市场</span>
        </div>
      </div>

      <div class="about__content" v-reveal>
        <span class="section-tag">关于我们</span>
        <h2 class="section-title">深耕中巴贸易，<span class="accent">一站式落地</span></h2>
        <p class="about__text">
          <strong>广州巴达通跨境贸易有限公司</strong>深耕中巴贸易领域，提供巴西本土公司设立、
          财税管理、本地化运营、商标注册及含清关服务的海外仓等一站式解决方案。
          创始人林晓懋——巴西籍华人、巴西第一代华人，家族生意深耕巴西市场
          <strong>50 余年</strong>，本人一线经营本土服装电商与工厂（D-ONE、Very Night），
          是 SHEIN、Shopee 巴西本土服装大卖。
        </p>
        <p class="about__text">
          团队专业且精通巴西市场与政策，依托优质本土资源，为卖家提供巴西本土公司注册
          （简易税制 / 预估利润制 / 中国法人店）、财税方案、进出口资质（无限额度 · 自行清关）、
          商标注册等全链路服务，期待与您携手开拓巴西市场，实现互利发展。
        </p>
        <ul class="about__points">
          <li>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
            巴西籍华人老板直营，一手资源、无中间商
          </li>
          <li>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
            巴西华人华侨电商总会 / 青年联合会 副会长
          </li>
          <li>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
            质保期出问题 Pago / 公户钱包、Full 仓货物拿不回，最高 20 万赔付
          </li>
        </ul>
        <a href="#contact" class="btn btn--primary">和我们聊聊</a>
      </div>
    </div>
  </section>
</template>

<script setup>
// 关于我们
</script>

<style scoped>
.about__inner {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: 72px;
  align-items: center;
}

.about__visual {
  position: relative;
}

.about__card-main {
  background: linear-gradient(160deg, #0b2a6b 0%, #123a8f 55%, #0b2a6b 100%);
  border-radius: 24px;
  padding: 36px 32px;
  color: #fff;
  box-shadow: var(--shadow-lg);
  position: relative;
  overflow: hidden;
}

.about__card-main::before {
  content: '';
  position: absolute;
  right: -60px;
  top: -60px;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(254, 203, 0, 0.35), transparent 70%);
}

.about__card-main::after {
  content: '';
  position: absolute;
  left: -40px;
  bottom: -60px;
  width: 160px;
  height: 160px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 162, 91, 0.45), transparent 70%);
}

.about__card-head {
  display: flex;
  align-items: center;
  gap: 14px;
  position: relative;
  z-index: 1;
}

.about__logo {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  object-fit: cover;
  flex-shrink: 0;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.25);
}

.about__card-head strong {
  display: block;
  font-size: 19px;
  letter-spacing: 1px;
}

.about__card-head small {
  font-size: 12px;
  opacity: 0.75;
}

.about__quote {
  margin: 28px 0;
  font-size: 17px;
  line-height: 1.8;
  font-weight: 500;
  position: relative;
  z-index: 1;
  opacity: 0.95;
}

.about__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  position: relative;
  z-index: 1;
}

.about__tags span {
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.22);
  font-size: 12.5px;
}

.about__badge {
  position: absolute;
  right: -16px;
  bottom: -24px;
  background: linear-gradient(135deg, #ffd84d, var(--yellow));
  color: var(--navy-dark);
  border-radius: 16px;
  padding: 16px 22px;
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
  text-align: center;
  animation: float 5s ease-in-out infinite;
}

.about__badge strong {
  font-size: 26px;
  font-weight: 800;
}

.about__badge span {
  font-size: 12px;
  font-weight: 600;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.about__content .section-tag {
  margin-bottom: 16px;
}

.about__text {
  margin-top: 18px;
  font-size: 15.5px;
  color: var(--text-2);
  line-height: 1.85;
}

.about__points {
  margin: 26px 0 30px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.about__points li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 15px;
  font-weight: 500;
  color: var(--text);
}

.about__points svg {
  color: var(--green);
  background: var(--green-light);
  border-radius: 50%;
  padding: 3px;
  box-sizing: content-box;
}

@media (max-width: 960px) {
  .about__inner {
    grid-template-columns: 1fr;
    gap: 56px;
  }

  .about__visual {
    max-width: 520px;
    margin: 0 auto;
    width: 100%;
    padding-bottom: 32px;
  }
}

@media (max-width: 560px) {
  .about__card-main {
    padding: 28px 22px;
  }

  .about__quote {
    font-size: 15px;
    margin: 22px 0;
  }

  .about__badge {
    right: 8px;
    bottom: -16px;
    padding: 12px 16px;
  }

  .about__badge strong {
    font-size: 22px;
  }

  .about__text {
    font-size: 14.5px;
  }

  .about__points li {
    font-size: 14px;
    align-items: flex-start;
  }

  .about__content .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
