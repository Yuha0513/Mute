<template>
  <div id="chartbase">

    <b-container class="bv-example-row">
      <div class="chart_area">
        <div class="genre_click">
          <GenreClick 
            v-if="data.length > 0"
            :data="data"
            :legend_class="legend_class"
            :colorScale="colorScale"
            @inputChange="filterInput"
            @inputChangeBack="filterInputBack"
          />
        </div>
        <div class="genre_chart">
          <GenreChart 
            v-if="data_chart.length > 0"
            :data="data"
            :data_chart="data_chart"
            :colorScale="colorScale"
            :key="chartReloadKey"
          />
        </div>
        <!-- <b-col>
        </b-col> -->
      </div>
    </b-container>
  </div>
</template>

<script>

import * as d3 from "d3";

import GenreChart from '@/components/Genre/GenreChart.vue'
import GenreClick from '@/components/Genre/GenreClick.vue'

export default {
  name: 'ChartBase',
  components: {
    GenreChart,
    GenreClick,
  },
  data: function(){
    return {
      data: [],
      data_chart: [],
      legend_class: [],
      chartReloadKey: 0,
      colorScale: null,
    }
  },
  created: function() {
    var that = this 

    d3.csv("movie_statistics.csv",
      function(data) {  
        that.data.push(data)
      }
    );
    this.data_chart = this.data
    this.colorScale = d3.scaleOrdinal(d3.schemeSet3)
    this.data_chart = this.data
  },
  methods: {
    filterInput (input) {
      this.data_chart = this.data_chart.filter(function(d){return d.Genre != input;})
      this.chartReloadKey += 1
    },
    filterInputBack (input) {
      this.data_chart = this.data_chart.concat(this.data.filter(function(d){return d.Genre == input;}))
      this.chartReloadKey += 1
    },
  },

}
</script>

<style>
#chartbase {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 100px;
}
.chart_area{
  display: flex;
}
.genre_chart{
  display: flex;
  flex-direction: column;
}
.genre_click{
  width: 300px;
  padding-top: 80px;
  margin-right: 50px
}
</style>