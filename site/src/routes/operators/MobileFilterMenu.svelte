<script lang="ts">
  import Drawer from "svelte-drawer-component";
  import FilterIcon from "$lib/icons/FilterIcon.svelte";
  import CloseFilterIcon from "$lib/icons/CloseFilterIcon.svelte";
  import RatingFilter from "./RatingFilter.svelte";
  import FactionFilter from "./FactionFilter.svelte";

  export let nations: string[];
  let filterDrawerOpen: boolean = false;
</script>

<button class="search-button" on:click={() => filterDrawerOpen = true}>
  <FilterIcon />
</button>

<div class="drawer-menu">
  <Drawer 
    open={filterDrawerOpen}
    placement="right" 
    size="80%" on:clickAway={() => filterDrawerOpen = false}>
    
    <button class="close-drawer-button" on:click={() => filterDrawerOpen = false}>
      <CloseFilterIcon />
    </button>

    <RatingFilter on:onRatingsChange />

    <FactionFilter 
      nations={nations}
      on:nationsChange
    />
  </Drawer>
</div>

<style>

  .search-button, .close-drawer-button {
    width: 82px;
    height: 48px;
    background-color: #E8E5DC;
    color: #070707;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border: none;

    position: fixed;
    bottom: 16px;
    right: 0;

    cursor: pointer;
  }

  .close-drawer-button {
    position: initial;
    bottom: 16px;
  }


  .search-button :global(svg), .close-drawer-button :global(svg) {
    font-size: 1.5em;
  }

  .drawer-menu :global(.drawer .panel) {
    background: rgba(0, 0, 0, 0.9);
    color: var(--color-text);
    padding: 30px 20px;
   /* max-height: 100vh;
    overflow-y: auto;*/
  }

  @media (min-width: 1000px) {
    .search-button {
      display: none;
    }
  }
</style>