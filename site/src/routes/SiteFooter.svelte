<script lang="ts">
  import GithubIcon from "$lib/icons/GithubIcon.svelte"
</script>

<footer>
  <a href="https://github.com/PseudoMon/tlvr-source" target="_blank"><GithubIcon /></a>
  <span>Site version 1.4</span>
  <span>Data last updated: 2025-07-20 (Such is the Joy of Our Reunion on Global)</span>
</footer>

<style>
  footer {
    background-color: var(--color-lighterbg);
    color: #A9A9A9;
    font-size: 1rem;
    line-height: 1rem;

    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2em;
    padding: 12px 23px;
    margin-top: 100px;
    margin-bottom: 0;
  }

  a { color: inherit; }
  a:hover { color: #fff; }

  a :global(svg) {
    font-size: 2em;
  }
</style>