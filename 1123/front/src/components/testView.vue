<!-- <template>
  <div class="stage">
  
  
  <div class="container">
    <div class="ring">
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
      <div class="img"></div>
    </div>
  </div>
  
  </div>
</template>

<script>
import gsap from 'gsap'
// import ScrollTrigger from "gsap/ScrollTrigger"

let xPos = 0;

gsap.timeline()
    .set('.ring', { rotationY:180, cursor:'grab' }) //set initial rotationY so the parallax jump happens off screen
    .set('.img',  { // apply transform rotations to each image
      rotateY: (i)=> i*-36,
      transformOrigin: '50% 50% 500px',
      z: -500,
      backgroundImage:(i)=>'url(https://picsum.photos/id/'+(i+32)+'/600/400/)',
      backgroundPosition:(i)=>getBgPos(i),
      backfaceVisibility:'hidden'
    })    
    .from('.img', {
      duration:1.5,
      y:200,
      opacity:0,
      stagger:0.1,
      ease:'expo'
    })
    .add(()=>{
      ('.img').on('mouseenter', (e)=>{
        let current = e.currentTarget;
        gsap.to('.img', {opacity:(i,t)=>(t==current)? 1:0.5, ease:'power3'})
      })
      ('.img').on('mouseleave', (e)=>{
        gsap.to('.img', {opacity:1, ease:'power2.inOut'})
      })
    }, '-=0.5')

(window).on('mousedown touchstart', dragStart);
(window).on('mouseup touchend', dragEnd);
      

function dragStart(e){ 
  if (e.touches) e.clientX = e.touches[0].clientX;
  xPos = Math.round(e.clientX);
  gsap.set('.ring', {cursor:'grabbing'})
  (window).on('mousemove touchmove', drag);
}


function drag(e){
  if (e.touches) e.clientX = e.touches[0].clientX;    

  gsap.to('.ring', {
    rotationY: '-=' +( (Math.round(e.clientX)-xPos)%360 ),
    onUpdate:()=>{ gsap.set('.img', { backgroundPosition:(i)=>getBgPos(i) }) }
  });
  
  xPos = Math.round(e.clientX);
}


function dragEnd(e){
  (window).off('mousemove touchmove', drag);
  gsap.set('.ring', {cursor:'grab'});
}


function getBgPos(i){ //returns the background-position string to create parallax movement in each image
  return ( 100-gsap.utils.wrap(0,360,gsap.getProperty('.ring', 'rotationY')-180-i*36)/360*500 )+'px 0px';
}

export default {
    name: 'testView',
    methods: {

    }
}
</script>

<style>
* {
  box-sizing: border-box;
}
body {
  background: #111;
  min-height: 100vh;
  padding: 0;
  margin: 0;
}
.gallery {
  position: absolute;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.cards {
  position: absolute;
  width: 14rem;
  height: 18rem;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.cards li {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 14rem;
  height: 18rem;
  text-align: center;
  line-height: 18rem;
  font-size: 2rem;
  font-family: sans-serif;
  background-color: #9d7cce;
  position: absolute;
  top: 0;
  left: 0;
  border-radius: 0.8rem;
}

.actions {
  position: absolute;
  bottom: 25px;
  left: 50%;
  transform: translateX(-50%);
}

button {
  display:inline-block;
  outline: none;
  border: none;
  padding: 8px 14px;
  background: #414141;
  background-image: -webkit-linear-gradient(top, #575757, #414141);
  background-image: -moz-linear-gradient(top, #575757, #414141);
  background-image: -ms-linear-gradient(top, #575757, #414141);
  background-image: -o-linear-gradient(top, #575757, #414141);
  background-image: linear-gradient(to bottom, #575757, #414141);
  text-shadow: 0px 1px 0px #414141;
  -webkit-box-shadow: 0px 1px 0px 414141;
  -moz-box-shadow: 0px 1px 0px 414141;
  box-shadow: 0px 1px 0px 414141;
  color: #ffffff;
  text-decoration: none;
  margin: 0 auto 10px;
  -webkit-border-radius: 4;
  -moz-border-radius: 4;
  border-radius: 4px;
  padding: 12px 25px;
  font-family: "Signika Negative", sans-serif;
  text-transform: uppercase;
  font-weight: 600;
  cursor: pointer;
  font-size: 13px;
  line-height: 18px;
}

button:hover {
  background: #57a818;
  background-image: -webkit-linear-gradient(top, #57a818, #4d9916);
  background-image: -moz-linear-gradient(top, #57a818, #4d9916);
  background-image: -ms-linear-gradient(top, #57a818, #4d9916);
  background-image: -o-linear-gradient(top, #57a818, #4d9916);
  background-image: linear-gradient(to bottom, #57a818, #4d9916);
  text-shadow: 0px 1px 0px #32610e;
  -webkit-box-shadow: 0px 1px 0px fefefe;
  -moz-box-shadow: 0px 1px 0px fefefe;
  box-shadow: 0px 1px 0px fefefe;
  color: #ffffff;
  text-decoration: none;
}

button {
  font-size: 20px;
  font-weight: 400;
}

a {
  color: #88ce02;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}


</style> -->