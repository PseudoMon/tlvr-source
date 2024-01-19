<script lang="ts">
  import { base } from "$app/paths";
  import { getAvatarUrl } from "$lib/utils";
  import { currentLang } from "$lib/stores";
  import Photocard from "$lib/char/Photocard.svelte";
</script>

<div class="overlay">
  <aside>
    <h2>Other characters with the same voice actor:</h2>
    <Photocard 
      imgsrc={getAvatarUrl("falco", base)}
      text="Plume"
    /><Photocard 
      imgsrc={getAvatarUrl("falco", base)}
      text="Plume"
    />
  </aside>
</div>

<style>
  aside {
    position: absolute;
    background-color: black;
    z-index: 89;
    padding: 2em;
    border-radius: 1em;
  }

  .overlay {
    position: fixed;
    z-index: 89;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.6);

    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>