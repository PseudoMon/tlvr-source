<script lang="ts">
  import AudioIcon from "$lib/icons/AudioIcon.svelte";

  export let assetloc: string;
  export let availability: string[] = [];

  const sourceurl = "https://raw.githubusercontent.com/PseudoMon/arknights-audio/global-server-voices"

  const voiceMap = {
    "jp": "voice",
    "en": "voice_en",
    "cn": "voice_cn",
    "kr": "voice_kr",
  }

  const teamrainbow = ["tachak", "blitz", "ash", "rfrost"]

  function getAudioFileUrl(lang) {
    if (lang === null) {
      return null;
    }
    
    if (Object.keys(voiceMap).includes(lang)) {
      return `${sourceurl}/${voiceMap[selectedLang]}/${assetloc}.mp3`;
    }
    else {
      if (lang === "linkage") {
        if (teamrainbow.some(name => assetloc.includes(name))) {
          return `${sourceurl}/${voiceMap["jp"]}/${assetloc}.mp3`
        } 

        if (assetloc.includes("ncdeer")) {
          return `${sourceurl}/${voiceMap["cn"]}/${assetloc}.mp3`
        }

        if (assetloc.includes("palico")) {
          return `${sourceurl}/${voiceMap["jp"]}/${assetloc}.mp3`
        }
      }
    }

    return null;
  }

  let audiofile: string;
  $: audiofile = getAudioFileUrl(selectedLang);

  let selectedLang: string = null;
  let showAudio: boolean;
  $: showAudio = selectedLang && audiofile;

  function clickLang(lang: string) {
    if (lang === selectedLang) {
      selectedLang = null;
      return;
    }

    selectedLang = lang;
  }
</script>

<div class="audio-container">
  <div class="audio-selector">
    <AudioIcon />
    {#if availability.includes("en")}
    <button 
      on:click={() => clickLang("en")} 
      class:selected={selectedLang === "en"}
    >EN</button>
    {/if}
    {#if availability.includes("cn")}
    <button 
      on:click={() => clickLang("cn")}
      class:selected={selectedLang === "cn"}
    >CN</button>
    {/if}
    {#if availability.includes("jp")}
    <button 
      on:click={() => clickLang("jp")}
      class:selected={selectedLang === "jp"}
    >JP</button>
    {/if}
    {#if availability.includes("kr")}
    <button
      on:click={() => clickLang("kr")}
      class:selected={selectedLang === "kr"} 
    >KR</button>
    {/if}
    {#if availability.includes("linkage")}
     <button
      on:click={() => clickLang("linkage")}
      class:selected={selectedLang === "linkage"} 
    >OG</button>
    {/if}
  </div>
  {#if showAudio}
  <audio controls src={audiofile} preload="metadata">
    <a href={audiofile}> Download audio </a>
  </audio>
  {/if}
</div>

<style>
  .audio-container {
    background-color: var(--color-lighterbg);
    border-radius: 0 0 20px 20px;
    padding: 0 10px 10px 10px;
    max-width: 268px;
  }

  .audio-selector {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    column-gap: 7px;
    padding-left: 15px;
    padding-bottom: 6px;

    background-color: var(--color-background);
    border-radius: 8px;
  }

  .audio-selector :global(svg) {
    margin-right: 6px;
  }

  .audio-selector button {
    width: 39px;
    height: 34px;
    font-size: 16px;
    background-color: #464646;
    color: #fff;
    box-shadow: 0px -4px 0px 0px rgba(0, 0, 0, 0.35) inset;
    border: none;
  }

  .audio-selector button:active, .audio-selector button.selected {
    box-shadow: none;
    padding-top: 4px;
  }

  .audio-selector button.selected {
    background-color: #7F2936
  }

  audio {
    max-width: 100%;
    margin-top: 8px;
  }
</style>