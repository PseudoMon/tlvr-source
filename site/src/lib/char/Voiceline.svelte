<script lang="ts">
  import { currentLang } from "$lib/stores";
  import AudioPlayer from "$lib/char/AudioPlayer.svelte";

  export let voicedata: Voicedata;
  export let availability: string[] = [];

  interface Voicedata {
    title: {
      en: string,
      cn: string,
      jp: string,
      kr: string,
    },
    text: {
      en: string,
      cn: string,
      jp: string,
      kr: string,
    },
    asset: string,
  }
</script>

{#if voicedata}
<div class="voiceline" class:en={$currentLang === "en"}>
  <h2>{voicedata.title[$currentLang]}</h2>
  <div>{voicedata.text[$currentLang]}</div>
</div>

<AudioPlayer 
  assetloc={voicedata.asset}
  availability={availability} 
/>
{/if}


<style>
  .voiceline {
    position: relative;
    background-color: var(--color-lighterbg);
    padding: 28px 18px 18px 18px;
    margin-top: 24px;
  }

  h2 {
    font-weight: 400;
    line-height: 0.9em;
    letter-spacing: -0.065em;
    font-size: 1.5em;

    display: inline-block;
    padding: 8px 18px;
    margin: 0;
    border: solid 2px;

    position: absolute;
    top: -24px;
    left: -14px;
  }

  .en h2 {
    font-style: italic;
  }
</style>