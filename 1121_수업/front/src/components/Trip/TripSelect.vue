<template>
  <div>
    <div class="select_country"
      v-for="(country, index) in countries"
      :key="index"  
    >
      <button @click="selectCountry(country, $event)">{{ country }}</button>
    </div>
    <div class="country_movies">
      <ul>
        <!-- <TripSelectItem
          v-for="countrymovie in countrymovies"
          :key="countrymovie.id"
          :countrymovie="countrymovie"
        /> -->
        <TripSelectItem
          :countrymovie="random_country"
        />
        <!-- {{ random_country }} -->
      </ul>
    </div>
  </div>
</template>

<script>
import TripSelectItem from '@/components/Trip/TripSelectItem'
import _ from 'lodash'

export default {
  name: 'TripSelect',
  data() {
    return {
      
    }
  },
  components: {
    TripSelectItem
  },
  computed: {
    countries() {
      return this.$store.state.country
    },
    countrymovies() {
      return this.$store.state.country_movie
    },
    random_country() {
      return _.sampleSize(this.$store.state.country_movie, 1)
    }
  },
  methods: {
    selectCountry(event) {
      this.$store.dispatch('selectCountry', event)
      this.$store.dispatch('countryMovie')
    },
    clearTrip() {
      this.$store.dispatch('clearTrip')
    }
  },
  beforeDestroy() {
    this.$store.state.country_movie = []
  }
}
</script>

<style>

</style>