<script lang="ts">
  import { base } from "$app/paths"
  import { currentLang } from "$lib/stores";
  import { getAvatarUrl } from "$lib/utils"
  import LangButtonBar from "$lib/LangButtonBar.svelte";
  import Photocard from "$lib/char/Photocard.svelte";
  import RatingFilter from "./RatingFilter.svelte";
  import FactionFilter from "./FactionFilter.svelte";

  import type { SingleChar } from "./+page"; 
  export let data;

  let charlist: SingleChar[];
  let filteredCharlist: SingleChar[];
  let nations: string[];
  $: charlist = data.charlist;
  $: filteredCharlist = filterCharlist(charlist, appliedFilters)
  $: nations = data.miscdata.nations.filter(n => !!n);

  type Filters = {
    name: string,
    rating: string[],
  }

  let appliedFilters: Filters = {
    name: "",
    rating: [],
  }

  function filterCharlist(list, filter) {
    return list.filter(char => {
      let include: boolean = true;

      if (filter.name != "") {
        const nameToSearch = filter.name.toLowerCase();
        const names = Object.values(char.name);
        include = names.some(name => 
          name.toLowerCase().includes(nameToSearch)
        );
      }

      if (include && filter.rating.length > 0) {
        include = filter.rating.includes(char.rating);
      }

      return include;
    })
  }

  function handleSearchName(e) {
    const value = e.target.value;
    appliedFilters = { ...appliedFilters, name: value };
  }

  function handleFilterRatings(e) {
    const rating = e.detail;
    appliedFilters = { ...appliedFilters, rating };
  }
</script>

<svelte:head>
  <title>Operators - TLVR</title>
</svelte:head>

<main>
  <LangButtonBar />

  <article class="charpage">
    <section class="filter-options">
      <h1>Operator List</h1>
      <label for="name-search">Search</label>
      <input type="text" placeholder="Search" 
        on:input={handleSearchName}
      />

      <RatingFilter on:onRatingsChange={handleFilterRatings} />

      <FactionFilter nations={nations} />
    </section>

    <ol class="charlist">
      {#each filteredCharlist as char}
      <li>
        <a href="{base}/operators/{char.nameid}">
          <Photocard 
            imgsrc={getAvatarUrl(char.nameid, base)} 
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
      grid-template-columns: repeat(auto-fill, 110px);
    }

    .charlist :global(.photocard) {
      --width: 90px;
      font-size: 0.8em;
    }
  }

  @media (min-width: 1000px) {
    main {
      max-width: 1100px;
    }

    .charpage {
      display: grid;
      grid-template-columns: 261px 1fr;
      column-gap: 6%;
    }

    h1 {
      font-size: 2.2em;
    }
  }
</style>