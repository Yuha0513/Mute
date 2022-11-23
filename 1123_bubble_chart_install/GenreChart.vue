<template>
  <div>
    <h2>Chart</h2>
      <div id="chart">
      </div>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: 'GenreChart',
  props: {
    data: Array,
    data_chart: Array,
    colorScale: null,
    },
  data: function() {
    return {
      settings: {
        margin: {
          top: 20, 
          right: 10, 
          bottom: 40, 
          left: 70
        },
      width: 600,
      height: 400,
      opacityCircles: 0.6,
      },
      svgContainer: Object,
      chartWrapper: Object,
      key_x: "VoteAverage",
      key_y: "VoteCount",
      key_r: "Popularity",
    }
  },
  mounted: function() {
    
    // chart 표
    this.svgContainer = d3.select("#chart")
      .append("svg")
      .attr("width", (this.settings.width + this.settings.margin.left + this.settings.margin.right))
      .attr("height", (this.settings.height + this.settings.margin.top + this.settings.margin.bottom))

    // x 축
    const xScale = d3.scaleLinear()
      .range([0, this.settings.width])
      .domain(this.key_dom(this.key_x))
    this.svgContainer.append("g")
      .attr("transform", "translate(" + this.settings.margin.left + "," + (this.settings.height + this.settings.margin.top) + ")")
      .call(d3.axisBottom(xScale))

    // y 축
    const yScale = d3.scaleLinear()
      .range([this.settings.height, 0])
      .domain(this.key_dom(this.key_y))
    this.svgContainer.append("g")
      .attr("transform", "translate(" + this.settings.margin.left + "," + this.settings.margin.top + ")")
      .call(d3.axisLeft(yScale));

    this.chartWrapper = this.svgContainer
      .append("g")
      .attr("class", "chordWrapper")
      .attr("transform", "translate(" + this.settings.margin.left + "," + this.settings.margin.top + ")");

    this.chartWrapper
      .append("g")
        .attr("class", "grid")
        .attr("transform", "translate(0," + this.settings.height + ")")
        .call(d3.axisBottom(xScale)
            .ticks(5)
            .tickSize(-this.settings.height)
            .tickFormat("")
        )
    this.chartWrapper.append("g")
        .attr("class", "grid")
        .call(d3.axisLeft(yScale)
            .ticks(5)
            .tickSize(-this.settings.width)
            .tickFormat("")
        )
    this.chartWrapper.append("text")
          .attr("x", (this.settings.width / 2))
          .attr("y", this.settings.height + this.settings.margin.top)
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("VoteAverage");
    this.chartWrapper.append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - this.settings.margin.left)
          .attr("x", 0 - (this.settings.height / 2))
          .attr("dy", "1em")
          .style("text-anchor", "middle")
          .text("VoteCount");

    // 반지름 (원크기)
    const rScale = d3.scaleLinear()
			.range([10,24])
      .domain(this.key_dom(this.key_r))

    // dot 원 그리기
    var that = this
    this.chartWrapper.append('g')
      .selectAll("dot")
      .data(this.data_chart)
      .enter()
      .append("circle")
        .attr("class", function() { return "Spotify" ; })//+ d[]; })
        .style("opacity", this.settings.opacityCircles)
        .style("fill", function(d) {return that.colorScale(d.Genre);})
        .style("stroke", "white")
        .attr("cx", function(d) {return xScale(d.VoteAverage);})
        .attr("cy", function(d) {return yScale(d.VoteCount);})
        .attr("r", function(d) {return rScale(d["Popularity"])});
  },
  methods: {
    key_dom: function(key){
      var dom = d3.extent(this.data, function(d) { return parseFloat(d[key]) ; })
      return dom
      
    },
  }
}
</script>