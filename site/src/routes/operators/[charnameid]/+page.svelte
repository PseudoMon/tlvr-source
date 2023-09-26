<script lang="ts">
  import { base } from "$app/paths";
  import { currentLang } from "$lib/stores";
  import { getAvatarUrl } from "$lib/utils";
  import LangButtonBar from "$lib/LangButtonBar.svelte";
  import Photocard from "$lib/char/Photocard.svelte";
  import VoiceCredits from "./VoiceCredits.svelte";
  import Voiceline from "./Voiceline.svelte";

  export let data;
  let photosrc: string;
  $: photosrc = data === null ? null : getAvatarUrl(data.nameid, base)

  // Image from Aceship
  //`https://raw.githubusercontent.com/Aceship/Arknight-Images/main/avatars/${data.charid}.png` 

  // Image from local
  //`/images/avatars/${data.nameid}.webp` 
</script>

<svelte:head>
  <title>{data.names.en} - TLVR</title>
</svelte:head>

<main>
  <LangButtonBar />
  {#if data !== null}
  <article class="charpage">
    <div class="leftcolumn">
      <h1>Operator File</h1>

      <section class="basicinfo">
        <Photocard 
          imgsrc={photosrc}
          text={data.names[$currentLang]}
        />
        <VoiceCredits actors={data.actors} />
      </section>
    </div>

    <ol class="voicelines">
      {#each data.voices as voicedata}
      <li>
      <Voiceline 
        voicedata={voicedata}
        availability={data.availability}
      />
      </li>
      {/each}
    </ol>
    
  </article>
  {:else}
    <h2>Loading...</h2>
  {/if}
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

  .basicinfo {
    display: flex;
    align-items: center;
    gap: 20px;
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

  @media (min-width: 1000px) {
    main {
      max-width: 1100px;
    }

    .charpage {
      display: grid;
      grid-template-columns: 1fr 1.8fr;
      column-gap: 6%;
    }

    .leftcolumn {
      position: sticky;
      top: 80px;
      z-index: 89;
      align-self: start;
    }

    h1 {
      text-align: center;
    }

    .basicinfo {
      flex-direction: column;
    }
  }
</style>