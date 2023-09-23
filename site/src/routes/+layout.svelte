<script lang="ts">
import Header from "./Header.svelte";
</script>

<svelte:head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sofia+Sans:ital,wght@0,500;0,700;0,900;1,500;1,600&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="https://necolas.github.io/normalize.css/8.0.1/normalize.css">
</svelte:head>
<Header />
<slot></slot>

<style>
  :root {
    --color-background: #070707;
    --color-lighterbg: #202020;
    --color-text: #fff;
  }
  
  :global(body) {
    margin: 0;

    background-color: var(--color-background);
    color: var(--color-text);
    
    font-family: "Sofia Sans", sans-serif;
    line-height: 1.455em;
    letter-spacing: -1%;
    font-size: 16px;
  }  
  
  :global(main) {
    box-sizing: border-box;
    width: 100%;
    max-width: 700px;
    padding: 0 36px;
    margin-left: auto;
    margin-right: auto;
  }

  @media (min-width: 800px) {
    :global(body) {
      font-size: 18px;    
    }
  }
</style>