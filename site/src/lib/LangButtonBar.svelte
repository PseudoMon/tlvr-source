<script lang="ts">
  import LangButton from "./LangButton.svelte";
  import { currentLang } from "./stores.ts"

  function langClicked(lang: string) {
    $currentLang = lang;
  }
</script>

<div class="lang-buttons">
  <LangButton 
    label="EN" 
    selected={$currentLang == "en"} 
    on:click={() => langClicked("en")}
  />
  <LangButton 
    label="CN" 
    selected={$currentLang == "cn"} 
    on:click={() => langClicked("cn")}
  />
  <LangButton 
    label="JP" 
    selected={$currentLang == "jp"} 
    on:click={() => langClicked("jp")}
  />
  <LangButton 
    label="KR" 
    selected={$currentLang == "kr"}
    on:click={() => langClicked("kr")}
  />
</div>

<style>
  .lang-buttons {
    display: flex;
    flex-direction: row;
    column-gap: 14px;
    justify-content: center;
    align-items: center;

    position: sticky;
    z-index: 90;
    top: 0;

    background-color: var(--color-background);
    padding: 12px;
    border-radius: 8px;
  }
</style>