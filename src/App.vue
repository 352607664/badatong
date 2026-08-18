<script setup>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import TrustBar from './components/TrustBar.vue'
import FloatingCta from './components/FloatingCta.vue'
import ServicesSection from './components/ServicesSection.vue'
import PlansSection from './components/PlansSection.vue'
import WhyUsSection from './components/WhyUsSection.vue'
import ProcessSection from './components/ProcessSection.vue'
import AboutSection from './components/AboutSection.vue'
import FaqSection from './components/FaqSection.vue'
import ContactSection from './components/ContactSection.vue'
import FooterSection from './components/FooterSection.vue'
</script>

<template>
  <div class="app-root">
    <NavBar />
    <main>
      <HeroSection />
      <TrustBar />
      <ServicesSection />
      <PlansSection />
      <WhyUsSection />
      <ProcessSection />
      <AboutSection />
      <FaqSection />
      <ContactSection />
    </main>
    <FooterSection />
    <FloatingCta />
  </div>
</template>

<style scoped>
.app-root {
  min-height: 100vh;
  min-height: 100dvh;
  overflow-x: hidden;
  padding-bottom: var(--safe-bottom);
}

@media (max-width: 768px) {
  .app-root {
    padding-bottom: calc(72px + var(--safe-bottom));
  }
}
</style>
