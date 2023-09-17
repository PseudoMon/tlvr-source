<script lang="ts">
  import { currentLang } from "$lib/stores";
  import LangButtonBar from "$lib/LangButtonBar.svelte";
  import Photocard from "$lib/char/Photocard.svelte";
  import VoiceCredits from "$lib/char/VoiceCredits.svelte";

  export let data;
  $: console.log(data);
</script>

<main>
  <LangButtonBar />
  <h1>Operator File</h1>

  <section class="basicinfo">
    <Photocard 
      imgsrc="https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/char_102_texas.png"
      text="Texas"
    />

    <VoiceCredits actors={data.actors} />
  </section>
</main>

<style>
  main {
    margin: 24px 0;
  }
  h1 {
    font-size: 2em;
    font-weight: 900;
    line-height: 1em;
    margin-bottom: 0.5em;
  }

  .basicinfo {
    display: flex;
    align-items: center;
    column-gap: 20px;
  }
</style>