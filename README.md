# 巴达通公司官方网站（Vue3 + Vite）

巴达通（BADATONG）巴西电商服务官网，主营：**巴西本土店注册、税务申报、店铺注册**。

## 技术栈

- Vue 3（Composition API + `<script setup>`）
- Vite 6
- 纯手写 CSS（无 UI 框架依赖），IntersectionObserver 滚动动画

## 本地运行

```bash
npm install
npm run dev      # 开发预览 http://localhost:5173
npm run build    # 生产构建，输出到 dist/
npm run preview  # 预览构建产物
```

## 替换二维码（重要）

联系区的二维码目前是**占位图**，请将你自己的二维码图片替换为：

```
public/qrcode.png
```

建议尺寸：`600 × 600` 像素以上、正方形 PNG，替换后刷新页面即可生效。

## 修改联系方式

联系方式集中在 `src/components/ContactSection.vue` 和 `src/components/FooterSection.vue` 中，
搜索「+55 11 0000-0000」「contact@badatong.com」替换为你真实的电话与邮箱。

## 目录结构

```
badatong-website/
├── public/
│   ├── favicon.svg      # 站点图标
│   └── qrcode.png       # ★ 联系二维码（替换成你的）
├── src/
│   ├── assets/styles/main.css   # 全局样式与品牌变量
│   ├── main.js                  # 入口 + 滚动动画指令
│   ├── App.vue
│   └── components/
│       ├── NavBar.vue           # 顶部导航
│       ├── HeroSection.vue      # 首屏
│       ├── ServicesSection.vue  # 核心业务
│       ├── WhyUsSection.vue     # 服务优势
│       ├── ProcessSection.vue   # 服务流程
│       ├── AboutSection.vue     # 关于我们
│       ├── FaqSection.vue       # 常见问题
│       ├── ContactSection.vue   # 联系我们（含二维码）
│       └── FooterSection.vue    # 页脚
```

## 品牌色

| 用途 | 色值 |
| --- | --- |
| 巴西绿（主色） | `#00a25b` |
| 巴西黄（点缀） | `#fecb00` |
| 深海蓝（文字/深色背景） | `#0b2a6b` |
