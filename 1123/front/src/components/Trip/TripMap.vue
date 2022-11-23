<template>
  <div id="map">
    <svg class="canvas" :viewBox="`0, 0, ${width}, ${height}`">
      <g class="pathGroup"></g>
      <text id="tooltip" x="50" y="50">{{ displayedCountry }}</text>
    </svg>
  </div>
</template>

<script>
import json from "@/assets/world.json";
import { geoPath, geoEqualEarth } from "d3-geo";
import * as selection from "d3-selection";
import * as zoom from "d3-zoom";
import { feature } from "topojson-client";

export default {
  name: "TripMap",
  data() {
    return {
      myJson: feature(json, json.objects["ne_50m_admin_0_countries_lakes"]),
      displayedCountry: "",
      width: 950,
      height: 550,
    };
  },
  computed: {
    projection() {
      return geoEqualEarth().fitSize([this.width, this.height], this.myJson);
    },
    path() {
      return geoPath().projection(this.projection);
    },
    g() {
      return selection.select(".pathGroup");
    },
    svg() {
      return selection.select(".canvas");
    },
    zoom() {
      return zoom
        .zoom()
        .scaleExtent([1, 8])
        .on("zoom", this.zoomed);
    }
  },
  methods: {
    zoomed() {
      const { transform } = selection.event;
      this.g.attr("transform", transform);
      this.g.attr("stroke-width", 1 / transform.k);
    },
    clicked(event) {
      this.$store.dispatch('selectCountry', event.properties.NAME)
      this.$store.dispatch('countryMovie')
      // const [[x0, y0], [x1, y1]] = this.path.bounds(d);
      // selection.event.stopPropagation();
      // this.svg
      //   .transition()
      //   .duration(750)
      //   .call(
      //     this.zoom.transform,
      //     zoom.zoomIdentity
      //       .translate(this.width / 2, this.height / 2)
      //       .scale(
      //         Math.min(
      //           8,
      //           0.9 / Math.max((x1 - x0) / this.width, (y1 - y0) / this.height)
      //         )
      //       )
      //       .translate(-(x0 + x1) / 2, -(y0 + y1) / 2),
      //     selection.mouse(this.svg.node())
      //   );
    },
    reset() {
      this.svg
        .transition()
        .duration(750)
        .call(
          this.zoom.transform,
          zoom.zoomIdentity,
          zoom
            .zoomTransform(this.svg.node())
            .invert([this.width / 2, this.height / 2])
        );
    },
    mouseentered(d, i, nodes) {
      this.displayedCountry = d.properties.NAME;
      selection
        .select(nodes[i])
        .classed("active", true)
        .raise();
    },
    mouseleft(d, i, nodes) {
      this.displayedCountry = "";
      selection.select(nodes[i]).classed("active", false);
    },
  },
  mounted() {
    this.g
      .selectAll(".country")
      .data(this.myJson.features)
      .join("path")
      .attr("class", "country")
      .attr("d", this.path)
      .on("mouseenter", this.mouseentered)
      .on("mouseleave", this.mouseleft)
      .on("click", this.clicked); 
      // 여기에 this.methods이름 넣으면 클릭 시, 메서드 함수 실행
    this.svg.on("click", this.reset).call(this.zoom);
  }
};
</script>

<style lang="scss">
#map{
  // margin-top: 100px;
  width: 1200px;

}

.canvas {
  background: linear-gradient(to right, #74ebd5, #acb6e5); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.country {
  fill: #90d6b0 ;  /* fallback for old browsers */

stroke: rgb(87, 105, 86);
}

#tooltip {
  font-size: 1.5rem;
}

.active {
  // stroke: rgb(146, 146, 146);
  fill: rgb(183, 238, 217);
  cursor: pointer; 
}
</style>
