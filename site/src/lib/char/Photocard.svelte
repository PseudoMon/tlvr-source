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
    background-color: #E8E5DC;
    padding: 4px 5px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    color: var(--color-background);
    font-weight: 600;
    font-size: 0.75em;
  }  

  span {
    height: calc(1em + 8px);
     /* Manual sizing bc font size autosizing in flexbox is whack */
  }

  img {
    background-color: #3A3A3A;
    width: 76px;
    height: 76px;
  }
</style>