<script lang="ts">
  export let nations: string[] = [];
  
  let selectedNations: string[] = [];

  function selectNation(nation) {
    if (!selectedNations.includes(nation)) {
      selectedNations = [...selectedNations, nation];
    }
    else {
      selectedNations = selectedNations.filter(n => n !== nation);
    }
  }
</script>

<h2>Nation</h2>
<div class="nations">
  {#each nations as nation}
    <button on:click={() => selectNation(nation)}>
      <img 
        src={`/images/factions/${nation}.webp`}
      >
    </button>
  {/each}
</div>

<style>
  h2 {
    font-size: 1.4em;
    border-bottom: solid 2px;
  }

  .nations {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
  }

  .nations button {
    border: none;
    background: none;
    opacity: 0.25;
    cursor: pointer;
  }

  .nations button:hover {
    opacity: 1.0;
  }

  .nations img {
    max-width: 100%;
  }
</style>