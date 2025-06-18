import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  // prevent a build error when using AWS Amplify libraries with Vite
  // https://github.com/aws/aws-sdk-js/issues/3673
  resolve: {
    alias: {
      './runtimeConfig': './runtimeConfig.browser',
    },
  }
});
