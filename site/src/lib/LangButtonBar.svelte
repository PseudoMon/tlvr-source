<script lang="ts">
  // TODO: Make a store that keeps selected language
  import LangButton from "./LangButton.svelte";
</script>

<div class="lang-buttons">
  <LangButton label="EN" />
  <LangButton label="CN" selected />
  <LangButton label="JP" />
  <LangButton label="KR" />
</div>

<style>
  .lang-buttons {
    display: flex;
    flex-direction: row;
    column-gap: 14px;
    justify-content: center;
    align-items: center;
  }
</style>