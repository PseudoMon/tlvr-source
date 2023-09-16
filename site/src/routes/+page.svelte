<script lang="ts">
import LangButtonBar from "$lib/LangButtonBar.svelte";
import { currentLang } from "$lib/stores";

export let data;
let welcomeText : string = "..."

$: welcomeText = data.welcomeText[$currentLang]
</script>

<main>
  <h1>TLVR</h1>
  <h2>Rhodes Island Tetralingual Voice Record</h2>
  <LangButtonBar />
  <aside class="home-quote">{welcomeText}</aside>
  <p>TLVR is an Arknights fansite that makes it easy to browse voice lines from the game in all its four languages (English, Chinese, Japanese, Korean). It’s created with multilingual speakers and language-learners in mind!</p>
  <h2>We're still under construction!</h2>
</main>

<style>
  main {
    box-sizing: border-box;
    width: 100%;
    max-width: 700px;
    padding: 0 36px;
  }

  h1 {
    margin-top: 34px;
    font-weight: 900;
    font-size: 4em;
    margin-bottom: 10px;
  }

  h2 {
    font-style: italic;
    font-weight: 600;
    font-size: 24;
    line-height: 0.95em;
    max-width: 250px;
  }

  .home-quote {
    text-align: center;
    background-color: var(--color-lighterbg);
    padding: 16px 52px;
    font-style: italic;

    margin-top: 23px;
  }
</style>
