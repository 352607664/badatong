<template>
  <section id="faq" class="section faq">
    <div class="container">
      <div class="section-head" v-reveal>
        <span class="section-tag">常见问题</span>
        <h2 class="section-title">你可能<span class="accent">关心</span>的问题</h2>
      </div>

      <div class="faq__list">
        <div v-for="(f, i) in faqs" :key="i" class="faq__item" :class="{ 'is-open': open === i }" v-reveal :style="{ transitionDelay: i * 0.05 + 's' }">
          <button class="faq__q" @click="open = open === i ? null : i">
            <span>{{ f.q }}</span>
            <span class="faq__ic">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
            </span>
          </button>
          <transition name="faq">
            <div v-show="open === i" class="faq__a">
              <p>{{ f.a }}</p>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const open = ref(0)

const faqs = [
  {
    q: '注册巴西本土公司需要提供哪些资料？',
    a: '一般需要：法人护照（公证翻译 + 海牙认证）、个人住址证明、经营类目信息等。巴达通顾问会在签约后给你一对一的材料清单，全程指导办理，无需担心流程复杂。'
  },
  {
    q: '公司注册有哪些方案可选？',
    a: '提供简易税制、预估利润制、中国法人店等多种方案。简易税制适合中小体量卖家、成本低；预估利润制适合规模增长中的卖家；中国法人店适合需要自持法人的卖家，顾问会根据你的经营规划推荐最合适的方案。'
  },
  {
    q: '法人配合度怎么样？KYC 要等多久？',
    a: '法人均为工厂员工及家属，配合程度高，除周末外 KYC 平均配合时效在 12 小时至 7 天以内，认证不卡壳、不误事，运营更省心。'
  },
  {
    q: '说好的 20 万质保，具体是怎么赔付的？',
    a: '质保期内公司与税务出现问题，我们会协助把 Mercado Pago、公户钱包拿回，Full 仓的货物协助拿回；确实拿不回的，按合同最高赔付 20 万元/次。税务实缴申报、完税证明齐全，白纸黑字有保障。'
  },
  {
    q: '进出口和清关是怎么操作的？',
    a: '我们协助办理巴西进出口资质（无限额度），卖家可自行清关掌控时效；同时提供含清关服务的巴西海外仓，货物快速流转、一件代发，物流成本更低。'
  },
  {
    q: '注册完成后，后续遇到问题有人管吗？',
    a: '当然。每位客户都有专属顾问持续服务，质保期内法人配合 KYC 认证不限次数，税务、店铺、经营相关疑问随时咨询。我们做的是长期生意伙伴，不只是注册那一单。'
  }
]
</script>

<style scoped>
.faq {
  background: var(--surface);
}

.faq__list {
  max-width: 780px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.faq__item {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 14px;
  overflow: hidden;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.faq__item.is-open {
  border-color: rgba(0, 162, 91, 0.4);
  box-shadow: var(--shadow-sm);
}

.faq__q {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 24px;
  text-align: left;
  font-size: 15.5px;
  font-weight: 600;
  color: var(--navy);
}

.faq__ic {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: var(--green-light);
  color: var(--green-dark);
  flex-shrink: 0;
  transition: transform 0.3s ease;
}

.faq__item.is-open .faq__ic {
  transform: rotate(45deg);
}

.faq__a {
  padding: 0 24px 20px;
}

.faq__a p {
  font-size: 14.5px;
  color: var(--text-2);
  line-height: 1.8;
  padding-left: 0;
}

.faq-enter-active,
.faq-leave-active {
  transition: all 0.28s ease;
  overflow: hidden;
}

.faq-enter-from,
.faq-leave-to {
  opacity: 0;
  max-height: 0;
}

.faq-enter-to,
.faq-leave-from {
  opacity: 1;
  max-height: 400px;
}

@media (max-width: 560px) {
  .faq__q {
    padding: 16px 18px;
    font-size: 14.5px;
    gap: 12px;
  }

  .faq__a {
    padding: 0 18px 16px;
  }

  .faq__a p {
    font-size: 14px;
  }
}
</style>
