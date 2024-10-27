<script lang="ts">
  import AudioIcon from "$lib/icons/AudioIcon.svelte";

  export let assetloc: string;
  export let availability: string[] = [];

  // Some skins have # in the name, which has to be translated in URL
  $: assetlocClean = assetloc.replace("#", "%23")

  const sourceurl = "https://raw.githubusercontent.com/PseudoMon/arknights-audio/global-server-voices"

  const voiceMap = {
    "jp": "voice",
    "en": "voice_en",
    "cn": "voice_cn",
    "kr": "voice_kr",
  }

  const regionalLangs = ["ita", "cn_topolect"]
  const regionalLang_sans_suffix = ["ger", "rus"]
  const teamrainbow = ["tachak", "blitz", "ash", "rfrost", 
    "ela", "iana", "rdoc", "fuze"]

  const nameMapping = {
    "cn_topolect": "CN REG",
    "linkage": "OG"
  }

  function getAudioFileUrl(lang) {
    if (lang === null) {
      return null;
    }
    
    // One of the standard voice languages
    if (Object.keys(voiceMap).includes(lang)) {
      return `${sourceurl}/${voiceMap[selectedLang]}/${assetlocClean}.mp3`;
    }

    // Regional voice
    else if (regionalLangs.includes(lang)) {
      const regionalAssetloc = assetlocClean.replace("/", `_${lang}/`);
      return `${sourceurl}/voice_custom/${regionalAssetloc}.mp3`;
    }

    else if (regionalLang_sans_suffix.includes(lang)) {
      return `${sourceurl}/voice_custom/${assetlocClean}.mp3`;
    }

    // Specific file location for crossover characters
    else if (lang === "linkage") {
      if (teamrainbow.some(name => assetlocClean.includes(name))) {
        return `${sourceurl}/${voiceMap["jp"]}/${assetlocClean}.mp3`
      } 

      if (assetlocClean.includes("ncdeer")) {
        return `${sourceurl}/${voiceMap["cn"]}/${assetlocClean}.mp3`
      }

      if (assetlocClean.includes("palico")) {
        return `${sourceurl}/${voiceMap["jp"]}/${assetlocClean}.mp3`
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
    
    {#each availability as lang}
      <button
        on:click={() => clickLang(lang)}
        class:selected={selectedLang === lang}
      >{
        Object.keys(nameMapping).includes(lang) ? 
        nameMapping[lang] :
        lang.toUpperCase()
      }</button>
    {/each}
  </div>

  {#if showAudio}
  <audio controls src={audiofile} preload="auto">
    <a href={audiofile}> Download audio </a>
  </audio>
  {/if}

</div>

<style>
  .audio-container {
    background-color: var(--color-lighterbg);
    border-radius: 0 0 20px 20px;
    padding: 0 10px 10px 10px;
    display: inline-block;
    box-sizing: border-box;
    max-width: 100%;
  }

  .audio-selector {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    column-gap: 7px;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 6px;

    background-color: var(--color-background);
    border-radius: 8px;

    overflow-x: auto;
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
    line-height: 0.8;
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