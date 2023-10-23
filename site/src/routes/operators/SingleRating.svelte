<script lang="ts">
  import StarIcon from "$lib/icons/StarIcon.svelte"

  export let rating = 0;
  $: starArray = Array(rating);
</script>

<button on:click class="single-rating">
  {#each starArray as _, __}
    <StarIcon />
  {/each}
</button>

<style>
  .single-rating {
    background-color: #333737;
    display: inline-flex;
    padding: 7px 14px;
    border-radius: 20px;

    border: none;
    color: inherit;
    cursor: pointer;
  }

  .single-rating:hover {
    background-color: #8A2929;
  }

  .single-rating > :global(*) {
    opacity: 0.5;
  }
</style>