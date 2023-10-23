<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import StarIcon from "$lib/icons/StarIcon.svelte"
  import SingleRating from "./SingleRating.svelte"

  const dispatch = createEventDispatcher();
  const ratings: number[] = [1, 2, 3, 4, 5, 6]

  let selectedStatus: boolean[] = ratings.map(_ => false);
  let selectedRatings: number[] = []

  $: dispatch('onRatingsChange', selectedRatings)

  function onSelect(idx: number) {
    if (!selectedRatings.includes(ratings[idx])) {
      selectedRatings = [...selectedRatings, ratings[idx]];
    }

    // Reset selected display
    selectedStatus = ratings.map(_ => false);
  }

  function onHover(selectedIdx: number) {
    selectedStatus = selectedStatus.map((rating, idx) => {
      if (idx <= selectedIdx) {
        return true;
      }
      return false;
    })
  }

  function onUnhover() {
    // Reset selected display
    selectedStatus = ratings.map(_ => false);
  }

  function removeRating(ratingToRemove) {
    selectedRatings = selectedRatings.filter(
      rating => rating !== ratingToRemove
    );
  }
</script>

<h2>Rating</h2>
<div class="selector">
  {#each ratings as _, index}
    <button 
      on:click={() => onSelect(index)}
      on:pointerover={() => onHover(index)}
      on:pointerleave={onUnhover}
      class:selected={selectedStatus[index]}
    >
      <StarIcon />
    </button>
  {/each}
</div>

<ol>
  {#each selectedRatings as rating}
  <li><SingleRating 
    on:click={() => removeRating(rating)} 
    rating={rating}
  /></li>
  {/each}
</ol>



<style>
  h2 {
    font-size: 1.4em;
    border-bottom: solid 2px;
  }

  button {
    color: var(--color-text);

    background: none;
    border: none;
    cursor: pointer;
    opacity: 0.25;

    padding: 0;
    margin-right: -2px;
  }

  button:hover, button.selected {
    opacity: 1;
  }

  .selector {
    display: flex;
  }

  ol {
    list-style: none;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
</style>
      