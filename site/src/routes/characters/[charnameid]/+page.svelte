<script lang="ts">
  import { currentLang } from "$lib/stores";
  import LangButtonBar from "$lib/LangButtonBar.svelte";
  import Photocard from "$lib/char/Photocard.svelte";
  import VoiceCredits from "$lib/char/VoiceCredits.svelte";
  import Voiceline from "$lib/char/Voiceline.svelte";

  export let data;
</script>

<main>
  <LangButtonBar />
  <h1>Operator File</h1>

  {#if data !== null}
  <section class="basicinfo">
    <Photocard 
      imgsrc="https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/char_102_texas.png"
      text={data.names[$currentLang]}
    />
    <VoiceCredits actors={data.actors} />
  </section>

  <ol class="voicelines">
    {#each data.voices as voicedata}
    <li>
    <Voiceline 
      voicedata={voicedata}
    />
    </li>
    {/each}
  </ol>
  {:else}
  <h2>Loading...</h2>
  {/if}
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

  .basicinfo {
    display: flex;
    align-items: center;
    column-gap: 20px;
  }

  .voicelines {
    margin-top: 35px;
    display: flex;
    flex-direction: column;
    row-gap: 24px;
  }

  ol {
    padding: 0;
  }
  
  .voicelines li {
    display: block;
  }
</style>