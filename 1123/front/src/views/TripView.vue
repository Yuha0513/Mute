<template>
  <div class="trip_container">
    <div>
      <TripSelect/>
    </div>
    <div>
      <!-- <RandomMovie/> -->
    </div>
  </div>
</template>

<script>

// import RandomMovie from '@/components/Trip/RandomMovie'
import TripSelect from '@/components/Trip/TripSelect'
// import TripMap from '@/components/Trip/TripMap'

export default {
    name: 'TripView',
    components: {
      // RandomMovie, 
      TripSelect
    }
}
</script>

<style>

.trip_container{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.flag_icon {
  width: 90px;
  height: 80px;
}
</style>