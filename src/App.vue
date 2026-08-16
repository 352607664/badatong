<script setup>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
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
      <ServicesSection />
      <PlansSection />
      <WhyUsSection />
      <ProcessSection />
      <AboutSection />
      <FaqSection />
      <ContactSection />
    </main>
    <FooterSection />
  </div>
</template>

<style scoped>
.app-root {
  min-height: 100vh;
  overflow-x: hidden;
}
</style>
