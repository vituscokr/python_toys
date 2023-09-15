import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  rollupOptions: {
    input: {
      main: resolve(__dirname, 'index.html')
    }
  }
})
