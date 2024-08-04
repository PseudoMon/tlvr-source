<svelte:head>
  <title>Voice Actors List - TLVR</title>
</svelte:head>

<script lang="ts">
// import LangButtonBar from "$lib/LangButtonBar.svelte";
// import { currentLang } from "$lib/stores";
import SvelteTable from "svelte-table";

export let data;

let filteredList = [];
$: filteredList = data.charlist;

const langs = ["en", "cn", "jp", "kr"]

let rows =  [{ id: 1, first_name: "Marilyn", last_name: "Monroe", pet: "dog" },
  { id: 2, first_name: "Abraham", last_name: "Lincoln", pet: "dog" }]

const langColumns = langs.map(lang => ({
  key: lang,
  title: lang.toUpperCase(),
  value: char => char.actors[lang] ? char.actors[lang].global : "-",
}));

const columns = [
  {
    key: "name",
    title: "Operator",
    value: char => char.names.en,
    class: "charname",
  }
].concat(langColumns)

</script>

<main>
  <h1>Voice Actor List</h1>
  <SvelteTable rows={filteredList} columns={columns}></SvelteTable>

  <!-- <table>
    <thead>
      <tr>
        <td></td>
        <td>EN</td>
        <td>CN</td>
        <td>JP</td>
        <td>KR</td>   
      </tr>
    </thead>
    <tbody>
      {#each filteredList as char}
      <tr>
        <td class="charname">{char.names.en}</td>
        {#each langs as lang}
          <td>
            {#if char.actors[lang]}
              {char.actors[lang].global}
            {:else}
              -
            {/if}
          </td>
        {/each}
      </tr>
      {/each}
    </tbody>
  </table> -->
</main>

<style>
  thead, * :global(.charname) {
    font-weight: 600;
  }

  * :global(td) {
    padding: 0.25em 0.5em;
  }

  main {
    max-width: 1000px;
    overflow-x: auto;
  }
</style>