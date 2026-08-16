<template>
  <footer class="footer">
    <div class="container">
      <div class="footer__main">
        <div class="footer__brand">
          <a href="#home" class="footer__logo">
            <img src="/logo.png" alt="巴达通 BADATONG" class="footer__logo-img" />
            <span>
              <strong>巴达通</strong>
              <small>BADATONG · 巴西电商服务</small>
            </span>
          </a>
          <p class="footer__slogan">
            广州巴达通跨境贸易有限公司 · 深圳巴达通企业管理咨询服务有限公司<br />
            巴西本土公司注册 · 财税方案 · 进出口资质 · 商标注册 · 最高 20 万质保
          </p>
        </div>

        <div class="footer__col">
          <h4>快速导航</h4>
          <a href="#home">首页</a>
          <a href="#services">核心业务</a>
          <a href="#plans">方案报价</a>
          <a href="#why-us">服务优势</a>
          <a href="#faq">常见问题</a>
        </div>

        <div class="footer__col">
          <h4>核心服务</h4>
          <a href="#services">巴西本土公司注册</a>
          <a href="#services">财税方案</a>
          <a href="#services">进出口资质</a>
          <a href="#services">商标注册</a>
        </div>

        <div class="footer__col">
          <h4>联系我们</h4>
          <a href="#contact">电话：+86 191242352547</a>
          <a href="#contact">邮箱：frankyang19920828@gmail.com</a>
          <a href="#contact">中国办事处地址：深圳龙华区利金城中心T2栋1405</a>
          <a href="#contact">扫码添加专属顾问</a>
        </div>
      </div>

      <div class="footer__bottom">
        <span>© 2026 巴达通 BADATONG · 版权所有</span>
        <span>巴西本土公司注册 · 财税方案 · 进出口资质 · 商标注册一站式服务</span>
      </div>
    </div>
  </footer>
</template>

<script setup>
// 页脚
</script>

<style scoped>
.footer {
  background: var(--navy-dark);
  color: #cdd7ea;
  padding: 72px 0 0;
}

.footer__main {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1.2fr;
  gap: 40px;
  padding-bottom: 48px;
}

.footer__logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer__logo-img {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  object-fit: cover;
  flex-shrink: 0;
}

.footer__logo strong {
  display: block;
  font-size: 19px;
  color: #fff;
  letter-spacing: 1px;
}

.footer__logo small {
  font-size: 10.5px;
  color: #8fa0bd;
  letter-spacing: 0.5px;
}

.footer__slogan {
  margin-top: 20px;
  font-size: 13.5px;
  line-height: 1.9;
  color: #9fb0cc;
}

.footer__col h4 {
  font-size: 15px;
  color: #fff;
  font-weight: 700;
  margin-bottom: 18px;
}

.footer__col a {
  display: block;
  font-size: 13.5px;
  color: #9fb0cc;
  padding: 5px 0;
  transition: color 0.2s ease, transform 0.2s ease;
}

.footer__col a:hover {
  color: var(--yellow);
  transform: translateX(4px);
}

.footer__bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: 22px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-size: 12.5px;
  color: #7f90ad;
  flex-wrap: wrap;
}

@media (max-width: 960px) {
  .footer__main {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 560px) {
  .footer__main {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
</style>
