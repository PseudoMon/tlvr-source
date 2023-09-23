<script lang="ts">
  export let actors;
</script>

<div class="voiceinfo">
  <h2>Voice Credits</h2>
  {#each Object.keys(actors) as lang}
    <div class="label">{lang.toUpperCase()}</div>
    <div class="content">
      {actors[lang]["native"]}
      {#if actors[lang]["native"] != actors[lang]["global"]}
        ({actors[lang]["global"]})
      {/if}
    </div>
  {/each}
</div>

<style>
  .voiceinfo {
    display: grid;
    grid-template-columns: 2em 1fr;
    column-gap: 0.5em;
    row-gap: 0.625em;

    line-height: 1.1em;
  }

  h2 {
    grid-column: 1 / -1;
    font-weight: 600;
    font-size: 1em;
    text-align: center;
    margin: 0;
  }

  .label {
    text-align: right;
    font-weight: 600;
    align-self: center;
  }

  @media (min-width: 800px)
  {
    h2 { 
      font-size: 1.2em; 
      margin-bottom: 0.2em; 
      margin-top: 0.5em;
      text-align: left;
      grid-column: 2;
    }
  }
</style>