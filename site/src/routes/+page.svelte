<script lang="ts">
import LangButtonBar from "$lib/LangButtonBar.svelte";
import { currentLang } from "$lib/stores";

export let data;
let welcomeText : string = "..."

$: welcomeText = data.welcomeText[$currentLang]
</script>

<svelte:head>
  <title>Rhodes Island Tetralingual Voice Record Archive</title>
</svelte:head>

<main>
  <header>
    <h1>TLVR</h1>
    <h2>Rhodes Island Tetralingual Voice Record Archive</h2>
  </header>
  <LangButtonBar />
  <aside class="home-quote">{welcomeText}</aside>
  <p>TLVR is an Arknights fansite that makes it easy to browse voice lines from the game in all its four languages (English, Chinese, Japanese, Korean). It’s created with multilingual speakers and language-learners in mind!</p>

  <p>This site includes all characters and all voice files currently available in the Global servers, including regional voices. Check footer for when the site was last updated.</p>

  <p>This site was made with love by <a href="https://pseudomon.github.io">PseudoMon</a>. Its creation was inspired by <a href="https://050644zf.github.io/ArknightsStoryTextReader">ASTR</a>. The site's source code is available on <a href="https://github.com/PseudoMon/tlvr-source">GitHub</a>.</p>

  <p>If you found a bug or have suggestions for the site, you can <a href="https://github.com/PseudoMon/tlvr-source/issues">submit an issue in Github</a> or contact me directly on <a href="https://twitter.com/PseudoMonious">Twitter</a>.</p>
</main>

<style>
  h1 {
    margin-top: 0.55em;
    font-weight: 900;
    font-size: 4em;
    margin-bottom: 0.3em;
  }

  h2 {
    font-style: italic;
    font-weight: 600;
    font-size: 24;
    line-height: 0.95em;
    max-width: 250px;
    margin-bottom: 0.5em;
  }

  .home-quote {
    text-align: center;
    background-color: var(--color-lighterbg);
    padding: 1em 3.25em;
    font-style: italic;

    margin-top: 23px;
  }

  a {
    color: #e8e5dc;
  }

  @media (min-width: 800px) {
    header { 
      text-align: center;
    }

    h1 {
      font-size: 5em;
    }

    h2 {
      max-width: initial;
    }

    .home-quote {
      font-size: 1.3em;
    }
  }
</style>
