<template>
  <section id="contact" class="section contact">
    <div class="container">
      <div class="contact__card" v-reveal>
        <div class="contact__info">
          <span class="contact__tag">联系我们 · 首次咨询免费</span>
          <h2 class="contact__title">开启你的巴西生意，<br />就从<span class="accent">一次咨询</span>开始</h2>
          <p class="contact__desc">
            扫码添加专属顾问，或通过以下方式联系我们。首次咨询免费，
            我们会根据你的经营体量定制最合适的巴西落地方案。
            质保期内法人或者税务问题，Pago / 公户钱包、Full 仓货物协助拿回，
            拿不回<strong class="contact__warranty">最高 20 万元赔付</strong>。
          </p>

          <ul class="contact__list">
            <li>
              <span class="contact__list-ic">
                <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              </span>
              <div>
                <small>电话 / phone</small>
                <strong>+86 191242352547</strong>
              </div>
            </li>
            <li>
              <span class="contact__list-ic">
                <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><path d="M22 6l-10 7L2 6"/></svg>
              </span>
              <div>
                <small>邮箱</small>
                <strong>frankyang19920828@gmail.com</strong>
              </div>
            </li>
            <li>
              <span class="contact__list-ic">
                <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </span>
              <div>
                <small>中国办事处</small>
                <strong>深圳</strong>
              </div>
            </li>
          </ul>
        </div>

        <div class="contact__qr">
          <div class="contact__qr-box">
            <div class="contact__qr-ring">
              <img src="/qrcode.jpg" alt="巴达通专属顾问二维码" class="contact__qr-img" />
            </div>
            <span class="contact__qr-tip">长按识别 / 扫码添加</span>
          </div>
          <p class="contact__qr-note">
            添加好友备注「巴西开店」<br />
            优先获取一对一方案咨询
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
// 联系区
</script>

<style scoped>
.contact {
  background:
    radial-gradient(800px 400px at 90% 10%, rgba(0, 162, 91, 0.08), transparent 60%),
    var(--bg);
}

.contact__card {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 48px;
  background: linear-gradient(135deg, #fff 0%, #f8fdf9 100%);
  border: 1px solid rgba(0, 162, 91, 0.15);
  border-radius: var(--radius-lg);
  padding: 52px 56px;
  box-shadow: var(--shadow-md);
  overflow: hidden;
  position: relative;
}

.contact__card::before {
  content: '';
  position: absolute;
  left: -80px;
  top: -80px;
  width: 240px;
  height: 240px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(254, 203, 0, 0.16), transparent 70%);
}

.contact__tag {
  display: inline-block;
  padding: 6px 16px;
  border-radius: 999px;
  background: linear-gradient(135deg, var(--green-light), #d4f5e4);
  color: var(--green-dark);
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 18px;
  border: 1px solid rgba(0, 162, 91, 0.15);
}

.contact__title {
  font-size: clamp(26px, 3.2vw, 34px);
  font-weight: 800;
  line-height: 1.3;
  color: var(--navy);
}

.contact__title .accent {
  color: var(--green);
}

.contact__desc {
  margin-top: 16px;
  font-size: 15px;
  color: var(--text-2);
  max-width: 480px;
}

.contact__warranty {
  color: var(--green-dark);
  font-weight: 700;
}

.contact__list {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.contact__list li {
  display: flex;
  align-items: center;
  gap: 14px;
}

.contact__list-ic {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  background: var(--green-light);
  color: var(--green-dark);
  flex-shrink: 0;
}

.contact__list small {
  display: block;
  font-size: 12px;
  color: var(--text-3);
}

.contact__list strong {
  font-size: 15px;
  color: var(--navy);
  font-weight: 600;
  word-break: break-all;
}

/* 二维码 */
.contact__qr {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;

  border-radius: 20px;

  text-align: center;
}

.contact__qr-box {
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  border: 1px solid var(--line);
}

.contact__qr-ring {
  position: relative;
  padding: 4px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--green), var(--yellow));
  animation: qrPulse 2.5s ease-in-out infinite;
}

@keyframes qrPulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0, 162, 91, 0.3); }
  50% { box-shadow: 0 0 0 8px rgba(0, 162, 91, 0); }
}

.contact__qr-img {
  width: 200px;
  height: 200px;
  border-radius: 8px;
  object-fit: contain;
  display: block;
  background: #fff;
}

.contact__qr-tip {
  font-size: 13px;
  font-weight: 600;
  color: var(--navy);
}

.contact__qr-note {
  font-size: 13px;
  color: var(--text-2);
  line-height: 1.7;
}

@media (max-width: 960px) {
  .contact__card {
    grid-template-columns: 1fr;
    padding: 40px 28px;
    gap: 36px;
  }

  .contact__qr {
    order: -1;
  }
}

@media (max-width: 560px) {
  .contact__card {
    padding: 28px 18px;
    gap: 28px;
  }

  .contact__title br {
    display: none;
  }

  .contact__desc {
    font-size: 14px;
  }

  .contact__list li {
    align-items: flex-start;
  }

  .contact__qr-img {
    width: 160px;
    height: 160px;
  }
}
</style>
