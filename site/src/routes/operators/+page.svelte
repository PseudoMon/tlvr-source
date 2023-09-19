<script lang="ts">
  import { currentLang } from "$lib/stores";
  import { getAvatarUrl } from "$lib/utils"
  import Photocard from "$lib/char/Photocard.svelte";
  import type { SingleChar } from "./+page"; 
  export let data;

  let charlist: SingleChar[];
  $: charlist = data.charlist;
</script>

<main>
  <h1>Operator List</h1>

  <ol class="charlist">
    {#each charlist as char}
    <li>
      <a href=/operators/{char.nameid}>
        <Photocard 
          imgsrc={getAvatarUrl(char.nameid)} 
          text={char.name[$currentLang]}
        />
      </a>
    </li>
    {/each}
  </ol>
</main>

<style>
  main {
    margin: 12px 0;
  }

  h1 {
    font-size: 2em;
    font-weight: 900;
    line-height: 1em;
    margin-bottom: 0.5em;
    margin-top: 0.5em;
  }

  ol {
    padding: 0;
  }
  
  li {
    display: block;
  }

  .charlist {
    /*display: flex;
    flex-wrap: wrap;*/
    display: grid;
    grid-template-columns: repeat(auto-fill, 86px);
    gap: 12px;
    justify-content: center;
  }

  .charlist > * {
    align-self: center;
  }

  .charlist a {
    text-decoration: none;
    color: inherit;
  }

  .charlist a:hover {
    transform: translateY(-5px);
  }
</style>