import { fileURLToPath, URL } from 'node:url'
import { baseURL_main, server_host, server_port } from './src/config/main.js'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    host: server_host,
    port: server_port,
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
