import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.sml.com.pk',
  output: 'static',
  build: {
    format: 'file'
  }
});
