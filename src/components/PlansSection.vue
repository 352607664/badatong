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

@media (max-width: 960px) {
  .plans__extras {
    grid-template-columns: 1fr;
  }
}
</style>
