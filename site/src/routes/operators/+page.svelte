<script lang="ts">
  import { currentLang } from "$lib/stores";
  import { getAvatarUrl } from "$lib/utils"
  import LangButtonBar from "$lib/LangButtonBar.svelte";
  import Photocard from "$lib/char/Photocard.svelte";
  import type { SingleChar } from "./+page"; 
  export let data;

  let charlist: SingleChar[];
  let filteredCharlist: SingleChar[];
  $: charlist = data.charlist;
  $: filteredCharlist = charlist.filter(char => {
    if (appliedFilters.name != "") {
      const nameToSearch = appliedFilters.name.toLowerCase();
      const names = Object.values(char.name);
      return names.some(name => 
        name.toLowerCase().includes(nameToSearch)
      );
    }
    else {
      return true;
    }

  });

  let appliedFilters = {
    name: "",
  }

  function handleSearchName(e) {
    const value = e.target.value 
    appliedFilters = { ...appliedFilters, name: value }
  }
</script>

<main>
  <LangButtonBar />

  <article class="charpage">
    <h1>Operator List</h1>
    <section class="filter-options">
      <label for="name-search">Search</label>
      <input type="text" placeholder="Search" 
        on:input={handleSearchName}
      />
      
    </section>

    <ol class="charlist">
      {#each filteredCharlist as char}
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
  </article>
</main>

<style>
  main {
    margin-top: 12px;
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

  .charlist a > :global(*:hover) {
    transform: translateY(-5px);
  }

  .filter-options {
    margin-left: 4px;
  }

  .filter-options label {
    display: none;
  }

  input {
    background-color: #E5E5E5;
    border-radius: 8px;
    padding: 4px 12px;
    border: none;
  }

  input:focus, input:focus-visible {
    outline: solid 2px #CC495D;
  }

  @media (min-width: 800px) {
    .charlist {
      grid-template-columns: repeat(auto-fill, 105px);
    }

    .charlist :global(.photocard) {
      --width: 80px;
      font-size: 0.8em;
    }
  }
</style>