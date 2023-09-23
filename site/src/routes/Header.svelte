<script lang="ts">
  import MenuIcon from "$lib/icons/MenuIcon.svelte";
  import Drawer from "svelte-drawer-component";

  let open = false;

  function closeDrawer() {
    open = false;
  }
</script>

<header>
  <a href="/"><h1>TLVR</h1></a>
  <button 
    class="burger-button"
    on:click={() => open = true}
  ><MenuIcon /></button>

  <h2>Rhodes Island Tetralingual Voice Record Database</h2>

  <nav class="fullsize-nav">
    <a href="/" on:click={closeDrawer}>Home</a>
    <a href="/credits" on:click={closeDrawer}>Credits</a>
    <a href="/operators" on:click={closeDrawer}>Operators</a>
  </nav>
</header>

<div class="drawer-menu">
<Drawer 
  bind:open
  placement="right" 
  size="200px" on:clickAway={() => open = false}>
  
  <nav>
    <a href="/" on:click={closeDrawer}>Home</a>
    <a href="/credits" on:click={closeDrawer}>Credits</a>
    <a href="/operators" on:click={closeDrawer}>Operators</a>
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
    font-size: 1em;
    font-weight: 900;
    color: #A7A3A2;
    margin: 0;
  }

  h2 {
    display: none;
  }

  .fullsize-nav {
    display: none;
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

  @media (min-width: 800px) {
    header {
      min-height: 117px;
      padding: 0 42px;
    }

    h1 {
      font-size: 64px;
    }

    h2 {
      display: initial;
      margin-left: 21px;
      font-weight: 600;
      font-style: italic;
      max-width: 400px;
      color: #A7A3A2;
    }

    .burger-button {
      display: none;
    }

    .fullsize-nav {
      margin-left: auto;
      align-self: flex-end;
      font-size: 1.6em;
      font-weight: 900;

      border-radius: 10px 10px 0 0;
      background-color: var(--color-lighterbg);

      display: flex;
    }

    .fullsize-nav a {
      padding: 12px 16px;
      border-radius: 10px 10px 0 0;

      text-decoration: none;
      color: #D3D3D3;
      transition: 0.5s;
    }

    .fullsize-nav a:hover {
      color: #fff;
      background-color: #4F4F4F;
    }
  }
</style>