<template>
  <span class="badge rounded-pill text-bg-secondary"
  > {{actor.name}}
  </span>
</template>

<script>
export default {
  name:'MovieActor',
  props: {
    actor: Object,
  }
}
</script>

<style>

</style>