<template>
  <section id="plans" class="section plans">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">方案与报价</span>
        <h2 class="section-title">六种开店方案，<span class="accent">总有一款</span>适合你</h2>
        <p class="section-desc">
          法人均为巴西本土工厂自有员工，欢迎随时到巴西实地考察 ·
          全平台本土店免费代开 · KYC 无限次数免费配合（7 个工作日内）
        </p>
      </div>

      <div class="plans__table-wrap" v-reveal>
        <table class="plans__table">
          <thead>
            <tr>
              <th>方案类型</th>
              <th>限时优惠</th>
              <th>原价</th>
              <!-- <th>月费（法人维护·记账报税）</th> -->
              <th>销售限额</th>
              <th>质保</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in plans" :key="p.name" :class="{ 'is-hot': p.hot }">
              <td class="plans__name">
                <strong>{{ p.name }}</strong>
                <small>{{ p.type }}</small>
              </td>
              <td class="plans__price">
                <strong>{{ p.price }}</strong>
                <em v-if="p.note" class="plans__note">{{ p.note }}</em>
              </td>
              <td class="plans__old">{{ p.old }}</td>
              <!-- <td>{{ p.fee }}</td> -->
              <td>{{ p.limit }}</td>
              <td>
                <span class="plans__warranty">{{ p.warranty }}</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- H5 卡片布局 -->
      <div class="plans__cards" v-reveal>
        <article v-for="p in plans" :key="'card-' + p.name" class="plans__card" :class="{ 'is-hot': p.hot }">
          <div class="plans__card-head">
            <div>
              <strong>{{ p.name }}</strong>
              <small>{{ p.type }}</small>
            </div>
            <span v-if="p.hot" class="plans__card-hot">推荐</span>
          </div>
          <div class="plans__card-price">
            <strong>{{ p.price }}</strong>
            <em>{{ p.old }}</em>
          </div>
          <dl class="plans__card-meta">
            <div>
              <dt>销售限额</dt>
              <dd>{{ p.limit }}</dd>
            </div>
            <div>
              <dt>质保</dt>
              <dd><span class="plans__warranty">{{ p.warranty }}</span></dd>
            </div>
          </dl>
          <a href="#contact" class="plans__card-cta">立即咨询此方案 →</a>
        </article>
      </div>

      <div class="plans__cta" v-reveal>
        <p>不确定选哪个方案？<strong>首次咨询免费</strong>，专属顾问为你定制最合适的落地方案</p>
        <a href="#contact" class="btn btn--primary">
          立即免费咨询
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </a>
      </div>

      <div class="plans__extras" v-reveal>
        <div class="plans__extra">
          <span class="plans__extra-ic">🎁</span>
          <div>
            <strong>全平台店铺免费代开</strong>
            <small>美客多、亚马逊、Shopee、TEMU、SHEIN、TikTok、Kwai、速卖通等</small>
          </div>
        </div>
        <div class="plans__extra">
          <span class="plans__extra-ic">🛡️</span>
          <div>
            <strong>KYC 无限次数免费配合</strong>
            <small>法人配合度高，平均时效 12 小时 - 7 天以内（除周末）</small>
          </div>
        </div>
        <div class="plans__extra">
          <span class="plans__extra-ic">🏠</span>
          <div>
            <strong>中国法人店可协助拿永居</strong>
            <small>中国香港公司投资控股，可协助中国法人获得巴西投资移民绿卡身份</small>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const plans = [
  {
    name: '标准店',
    type: '简易税制 · 合规低申报',
    price: '请私聊客服',
    old: '¥28,000',

    limit: '480 万雷亚尔/年',
    warranty: '12 个月',
    hot: true
  },
  {
    name: '合规税表店',
    type: '简易税制梯度 · 合法合规申报',
    price: '请私聊客服',
    old: '¥38,888',

    limit: '480 万雷亚尔/年',
    warranty: '3 年',
    hot: false
  },
  {
    name: '合规长期店',
    type: '预估利润制 · 中型公司',
    price: '请私聊客服',
    old: '¥58,888',

    limit: '7,800 万雷亚尔/年',
    warranty: '3 年',
    hot: false
  },
  {
    name: '中国法人店',
    type: '预估利润制 · 中国法人自持',
    price: '请私聊客服',
    old: '¥128,888',

    limit: '1 亿雷亚尔/年',
    warranty: '3 年',
    hot: false
  },
  {
    name: '美客多（海外仓自发货）',
    type: '小微企业 · A/B 主体双运营',
    price: '请私聊客服',
    old: '¥38,888',

    limit: '不限制销售额',
    warranty: '12 个月',
    hot: false
  },
  {
    name: '进出口资¥质（无限度）',
    type: '无限度 Radar · 自行清关',
    price: '请私聊客服',
    old: '¥188,888',
    limit: '无额度限制',
    warranty: '—',
    hot: false
  }
]
</script>

<style scoped>
.plans {
  background:
    radial-gradient(700px 320px at 15% 0%, rgba(254, 203, 0, 0.08), transparent 60%),
    var(--bg);
}

.plans__table-wrap {
  overflow-x: auto;
  border-radius: 20px;
  border: 1px solid var(--line);
  background: #fff;
  box-shadow: var(--shadow-md);
}

.plans__table {
  width: 100%;
  min-width: 860px;
  border-collapse: collapse;
  font-size: 14px;
}

.plans__table th {
  background: linear-gradient(135deg, #0b2a6b, #123a8f);
  color: #fff;
  font-weight: 600;
  font-size: 13.5px;
  padding: 16px 18px;
  text-align: left;
  white-space: nowrap;
}

.plans__table th:first-child {
  border-top-left-radius: 20px;
}

.plans__table th:last-child {
  border-top-right-radius: 20px;
}

.plans__table td {
  padding: 18px;
  border-top: 1px solid var(--line);
  color: var(--text-2);
  vertical-align: middle;
}

.plans__table tbody tr {
  transition: background 0.2s ease;
}

.plans__table tbody tr:hover {
  background: #f7faf9;
}

.plans__table tbody tr.is-hot {
  background: linear-gradient(90deg, #f2faf6, #fff7d6);
}

.plans__name strong {
  display: block;
  font-size: 15px;
  color: var(--navy);
}

.plans__name small {
  display: block;
  font-size: 12px;
  color: var(--text-3);
  margin-top: 3px;
}

.plans__price strong {
  font-size: 18px;
  font-weight: 800;
  color: var(--green);
  white-space: nowrap;
}

.plans__price em {
  display: block;
  font-style: normal;
  font-size: 11px;
  color: var(--text-3);
  margin-top: 2px;
}

.plans__old {
  color: var(--text-3);
  text-decoration: line-through;
  white-space: nowrap;
}

.plans__warranty {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 999px;
  background: var(--green-light);
  color: var(--green-dark);
  font-weight: 600;
  font-size: 12.5px;
  white-space: nowrap;
}

.plans__extras {
  margin-top: 28px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.plans__cta {
  margin-top: 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 28px 36px;
  background: linear-gradient(135deg, var(--navy) 0%, #123a8f 100%);
  border-radius: 20px;
  color: #fff;
  box-shadow: var(--shadow-md);
}

.plans__cta p {
  font-size: 16px;
  line-height: 1.6;
  opacity: 0.92;
}

.plans__cta strong {
  color: var(--yellow);
}

.plans__cta .btn {
  flex-shrink: 0;
  white-space: nowrap;
}

/* H5 卡片布局（默认隐藏，移动端显示） */
.plans__cards {
  display: none;
}

.plans__card {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 20px;
  box-shadow: var(--shadow-sm);
}

.plans__card.is-hot {
  border-color: rgba(0, 162, 91, 0.45);
  background: linear-gradient(180deg, #f2faf6, #fff);
  box-shadow: 0 8px 24px rgba(0, 162, 91, 0.12);
}

.plans__card-hot {
  flex-shrink: 0;
  font-size: 11px;
  font-weight: 700;
  color: #fff;
  background: linear-gradient(135deg, var(--green), #00c471);
  padding: 4px 12px;
  border-radius: 999px;
  box-shadow: 0 2px 8px rgba(0, 162, 91, 0.3);
}

.plans__card-price {
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px dashed var(--line);
}

.plans__card-price strong {
  display: block;
  font-size: 20px;
  font-weight: 800;
  color: var(--green);
}

.plans__card-price em {
  display: block;
  font-style: normal;
  font-size: 13px;
  color: var(--text-3);
  text-decoration: line-through;
  margin-top: 2px;
}

.plans__card-meta {
  margin-top: 14px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.plans__card-meta dt {
  font-size: 11px;
  color: var(--text-3);
  margin-bottom: 4px;
}

.plans__card-meta dd {
  font-size: 13px;
  color: var(--text-2);
  font-weight: 600;
}

.plans__card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.plans__card-head strong {
  display: block;
  font-size: 16px;
  color: var(--navy);
}

.plans__card-head small {
  display: block;
  font-size: 12px;
  color: var(--text-3);
  margin-top: 4px;
  line-height: 1.5;
}

.plans__card-cta {
  display: block;
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px dashed var(--line);
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: var(--green-dark);
  transition: color 0.2s ease;
}

.plans__card-cta:hover {
  color: var(--green);
}

.plans__extra {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 22px;
  box-shadow: var(--shadow-sm);
}

.plans__extra-ic {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 20px;
  background: var(--yellow-light);
  flex-shrink: 0;
}

.plans__extra strong {
  display: block;
  font-size: 15px;
  color: var(--navy);
  margin-bottom: 4px;
}

.plans__extra small {
  font-size: 12.5px;
  color: var(--text-2);
  line-height: 1.6;
}

@media (max-width: 768px) {
  .plans__table-wrap {
    display: none;
  }

  .plans__cards {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .plans__cta {
    flex-direction: column;
    align-items: stretch;
    text-align: center;
    padding: 24px 20px;
    gap: 16px;
  }

  .plans__cta .btn {
    justify-content: center;
  }

  .plans__extras {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .plans__extra {
    padding: 18px;
  }
}
</style>
