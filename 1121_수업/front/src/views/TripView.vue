<template>
  <div>
    trip
    <div>
      <TripSelect/>
    </div>
    <div>
      <RandomMovie/>
    </div>
  </div>
</template>

<script>

import RandomMovie from '@/components/Trip/RandomMovie'
import TripSelect from '@/components/Trip/TripSelect'

export default {
    name: 'TripView',
    components: {
      RandomMovie, TripSelect
    }
}
</script>

<style>
.flag_icon {
  width: 90px;
  height: 80px;
}
</style>