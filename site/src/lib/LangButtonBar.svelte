<script lang="ts">
  import LangButton from "./LangButton.svelte";
</script>

<div class="lang-buttons">
  <LangButton label="EN" selected />
  <LangButton label="CN" />
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