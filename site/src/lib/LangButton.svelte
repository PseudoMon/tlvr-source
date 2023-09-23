<script lang="ts">
  export let label : string = "N/A"
  export let selected : boolean = false;
</script>

<button class:selected on:click>
  {label}
</button>

<style>
  button {
    --color-bg: #E8E5DC;
    --color-accent: #CC495D;

    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 32px;
    box-sizing: border-box;
    padding: 0;

    font-style: italic;
    font-size: 20px;

    border-radius: 0;
    border: none;
    background: var(--color-bg);
    box-shadow: 0px -5px 0px 0px rgba(0, 0, 0, 0.25) inset;
    padding-bottom: 5px;
  }

  button.selected, button:active {
    border-top: solid var(--color-background) 5px;
    padding-bottom: 0;
    box-shadow: none;
  }

  button.selected {
    background: var(--color-accent);
  }

  @media (min-width: 800px) {
    button { 
      font-size: 24px;
      box-shadow: 0px -6px 0px 0px rgba(0, 0, 0, 0.25) inset;
      width: 90px;
      height: 40px;
      padding-bottom: 6px;
    } 
  }
</style>