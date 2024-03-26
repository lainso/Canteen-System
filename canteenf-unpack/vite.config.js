import { fileURLToPath, URL } from 'node:url'
import { baseURL_main } from './src/config/baseURL.js'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    host: '192.168.159.133',
    port: 80,
    proxy: {
      'api': {
        target: baseURL_main,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
