# TLVR Site

The site is built using Svelte Kit. We use Yarn around here, but I don't think the command for NPM is any different. Also, TypeScript, but I'm not too big of a stickler for that.

For development, run
```bash
yarn run dev
```

To build, **make sure the dev server is still running**, then run
```bash
yarn run build
```

This will build a static site in the `build` folder. Run this for a preview:
```bash
yarn run preview
```

## Static Site Shenanigans
This site is built for server-side, but that's nasty to set up, so I just use Svelte's adapter-static to make it a static site and then upload the result to Github Pages. We did some hacks to make this work.

First, if you check `src/routes/+layout.ts`, you'd notice prerendeing is on. This is applied to every pages in the site:
```js
export const prerender = true;
```

If you check `svelte.config.js`, you'd notice this line in the kit config
```js
prerender: {
  origin: dev ? "http://sveltekit-prerender" : "http://localhost:5173",
}
````
So basically, when a page is opened, it runs a fetch on a specific JSON file in the static file folders. The address for this file is decided by the calling page's origin, but this data isn't received when prerendering. 

We hack it by providing the address of the site while the dev server is on (so technically it's receiving the JSON from the dev server instead of itself). Obviously if the dev server use a different port, you should change it.

Since we're hosting on Github Pages' project page and without a custom domain, we need to adjust the base path in the config. You should also notice we use `{base}` whenever we do internal links. 

Also note how every server.ts files here technically could be a regular .ts file, which would make them be reran on the static site on every page load. I don't think we need that since the data isn't likely to change that often, so I just let them all run server-side (or, since we're prerendering everything, they're only ran when the site is being built).

You might also note how we have dynamic URLs, but we can still prerender everything! This is a Svelte Kit feature. With the static adapter, it will look for *every* internal link and then prerender that page. In our case, since the list page contain links for every character's page, all the pages for those characters are created. I'd assume if a character is missing from the list, even if the JSON file is there, a page won't be created for them and thus they won't be accessible from the static site.