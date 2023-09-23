<script lang="ts">
  export let imgsrc: string
  export let text: string
</script>

<div class="photocard">
  <img src={imgsrc} />
  <span>{text}</span>
</div>

<style>
  .photocard {
    --width: 76px;

    background-color: #E8E5DC;
    padding: 4px 5px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    color: var(--color-background);
    font-weight: 600;
    font-size: 0.75em;

    /* This width does not include padding!
       So it should be the same as image */
    width: var(--width);
    min-height: 98px;
  }  

  span {
    text-align: center;
    line-height: 1em;
    margin-top: 7px;
    /* Sizing eyeballing bc font size autosizing in flexbox is whack */
  }

  img {
    background-color: #3A3A3A;
    width: var(--width);
    height: var(--width);
  }

  @media (min-width: 800px) {
    .photocard {
      --width: 120px;
      padding: 8px 10px;
      font-size: 1.1em;
    }
  }
</style>