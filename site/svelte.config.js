import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/kit/vite';

const dev = process.argv.includes('dev');

const config = {
  // Consult https://kit.svelte.dev/docs/integrations#preprocessors
  // for more information about preprocessors
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter({
      pages: "build",
      assets: "build"
    }),
    paths: {
      base: dev ? '' : "/tlvr",
    },
    prerender: {
      origin: dev ? "http://sveltekit-prerender" : "http://localhost:5173",
    }
  }
};

export default config;
