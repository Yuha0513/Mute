<template>
  <div class="home_container">
    <div id="wrapper">
      <div id="home_content">
        
        <div>
          <RecommandMovie/>
        </div>
        <div class="home_textarea">
          <p><strong>Content here.</strong></p>
          <p>Montegeraliquam sed pede in cursus praesenec vestas rhoncus wisi at wisi. Condisseloborttis enim et ipsum mauristie id felit adipiscipit ac auctortorttitor sempor. Vitantesqueat sempus non sed et mus sit vivamus purus netus hendiment. Pretiuma diam et id tempus dolor por wisi sed volutpat facilisi.</p>
          <p>Wisiet sus adipit phasellentum elit condissim consecteturpiscing sapien vivamus et congue. Utvel tris quismod cursus liberos elit nisse curabitur tur parturpis tellenterdum. Semperligula curabitae tellentesque nulla trices vestas ristibulum id justo auctor facinia. Natisdonec consequat nibh pellus.</p>
          <p>Vestibusodio euisque id elerisus lacus tincidunt sit malesuada lacus pellus parturpiscing. Pellenterdumat maecenatoque cras a magna nibh et quis diam ames et. Laoremvolutpat ac dolor eget eget temper lacus vestibus velit lacus venean. Magnaipsum tellus morbi leo aliquat nulla convallis pellentesque.</p>
        </div>
      </div>
    </div>
    <div class="home_user">
      <p><HomeUser/></p>
      <p><strong>More stuff here.</strong></p>
      <p>sit malesuada lacus pellus parturpiscing. Pellenterdumat maecenatoque cras a magna nibh et quis diam ames et. Laoremvolutpat ac dolor eget eget temper lacus vestibus velit lacus venean. Magnaipsum tellus morbi leo aliquat nulla convallis pellentesque.</p>
    </div>
    <div id="footer">
      <p>Footer</p>
    </div>
    
  </div>
</template>

<script>
import HomeUser from '@/components/User/HomeUser'
import RecommandMovie from '@/components/Movie/RecommandMovie'

export default {
  name: 'HomeView',
  components: {
    HomeUser, RecommandMovie
  },
}
</script>

<style>
/* @import 'scss/slide.scss'; */

html,body{margin:0;padding:0}

p{margin:0 10px 10px}
/* a{padding:5px; text-decoration:none; color:#000000;} */

div#header h1{height:80px;line-height:80px;margin:0;padding-left:10px;}

div#content p{line-height:1.4}
.home_footer{
  background:#BFBD93;
  margin:0;padding:5px 5px;
}

.home_container {

  width: 80%;
  margin:0 auto
}
#home_content{
  float:right;
  width:1000px;
  margin-right: 100px;
  margin-top: 30px;
}
.home_user{
  margin-left:100px;
}
div#navigation{float:left;width:200px}
.home_user{
  display: flex;
  flex-direction: column;
  align-items: center;
  float:left;
  clear:left;
  width:200px;
}
div#footer{clear:both;width:100%}


</style>
