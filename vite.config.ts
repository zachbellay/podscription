import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path";


// https://vitejs.dev/config/
export default defineConfig({
  mode: 'development',
  plugins: [react()],
  base: '/static/',
  root: path.resolve('./django/podscription-project/static/src'),
  server: {
    host: '0.0.0.0',
    port: 3000,
    strictPort: true,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false
    },
    hmr: {
      host: '0.0.0.0',
      port: 3000,
      protocol: 'ws',
    },
  },
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
  },
  build: {
    outDir: path.resolve('./django/podscription-project/static/dist'),
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
    target: 'esnext',
    rollupOptions: {
      input: {
        main: path.resolve('./django/podscription-project/static/src/js/main.tsx'),
      },
      output: {
        chunkFileNames: undefined,
      }
    },
  },
})


