<script lang="ts">
  import MenuIcon from "$lib/icons/MenuIcon.svelte";
  import Drawer from "svelte-drawer-component";

  let open = false;
</script>

<header>
  <h1>TLVR</h1>
  <button 
    class="burger-button"
    on:click={() => open = true}
  ><MenuIcon /></button>
</header>

<div class="drawer-menu">
<Drawer 
  bind:open
  placement="right" 
  size="200px" on:clickAway={() => open = false}>
  
  <nav>
    <a href="/">Home</a>
    <a href="/credits">Credits</a>
    <a href="/characters">Characters</a>
  </nav>

</Drawer>
</div>

<style>
  header {
    background-color: #333737;
    box-sizing: border-box;
    min-height: 35px;
    padding: 6px 16px;
    display: flex;
    align-items: center;
  }

  h1 {
    font-size: 16px;
    font-weight: 900;
    color: #A7A3A2;
    margin: 0;
  }

  .burger-button {
    border: none;
    background: none;
    color: #fff;
    margin-right: 0;
    margin-left: auto;
    display: flex;
    align-items: center;
    opacity: 1;
  }

  .burger-button:hover, .burger-button:hover, .burger-button:hover {
    opacity: 0.5;
  }

  .burger-button:hover :global(svg) {
    height: 16px;
  }

  .drawer-menu :global(.drawer .panel) {
    background: rgba(0, 0, 0, 0.75);
    color: red;
  }

  .drawer-menu nav {
    margin-top: 82px;
    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 1em;

    font-weight: 900;
    font-size: 2em;
  }

  .drawer-menu nav a {
    color: var(--color-text);
    text-decoration: none;
  }
</style>