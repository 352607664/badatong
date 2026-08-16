import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  // 使用相对路径，构建产物可以直接双击 dist/index.html 打开
  base: './',
  plugins: [vue()],
  server: {
    host: true,
    port: 5173
  }
})
