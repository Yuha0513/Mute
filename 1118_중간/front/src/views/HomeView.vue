<template>
  <div id="container">
  <div id="header"><h1><a href="http://www.free-css.com/free-css-layouts.php">Free CSS Layouts</a></h1></div>
    <div id="wrapper">
      <div id="content">
        <p><strong>Content here.</strong></p>
        <p>Sapibulumnibh phasellus nulla egestibulum enim pretium elit tincidunt estiquam ultrisque donectetur. Sedcondimentumsan odio hendrerit proin vitae dignis nibh ac justo id congue. Amesintesque vel curabitae volutpat donec alique nasceleifendimentesque montesque rhoncus quis eros. Vestnunc nonummy</p>
        <p>Montegeraliquam sed pede in cursus praesenec vestas rhoncus wisi at wisi. Condisseloborttis enim et ipsum mauristie id felit adipiscipit ac auctortorttitor sempor. Vitantesqueat sempus non sed et mus sit vivamus purus netus hendiment. Pretiuma diam et id tempus dolor por wisi sed volutpat facilisi.</p>
        <p>Wisiet sus adipit phasellentum elit condissim consecteturpiscing sapien vivamus et congue. Utvel tris quismod cursus liberos elit nisse curabitur tur parturpis tellenterdum. Semperligula curabitae tellentesque nulla trices vestas ristibulum id justo auctor facinia. Natisdonec consequat nibh pellus.</p>
        <p>Vestibusodio euisque id elerisus lacus tincidunt sit malesuada lacus pellus parturpiscing. Pellenterdumat maecenatoque cras a magna nibh et quis diam ames et. Laoremvolutpat ac dolor eget eget temper lacus vestibus velit lacus venean. Magnaipsum tellus morbi leo aliquat nulla convallis pellentesque.</p>
      </div>
    </div>
    <div id="extra">
      <p><strong>More stuff here.</strong></p>
      <p>sit malesuada lacus pellus parturpiscing. Pellenterdumat maecenatoque cras a magna nibh et quis diam ames et. Laoremvolutpat ac dolor eget eget temper lacus vestibus velit lacus venean. Magnaipsum tellus morbi leo aliquat nulla convallis pellentesque.</p>
    </div>
    <div id="footer">
      <p>Footer</p>
    </div>
    
  </div>
</template>

<script>



export default {
  name: 'HomeView',
  components: {

  }
}
</script>

<style>
/* @import 'scss/slide.scss'; */

html,body{margin:0;padding:0}

p{margin:0 10px 10px}
/* a{padding:5px; text-decoration:none; color:#000000;} */
div#header{background-color:#F3F2ED;}
div#header h1{height:80px;line-height:80px;margin:0;padding-left:10px;}
div#container{text-align:left}
div#content p{line-height:1.4}
div#extra{background:#CCC8B3;}
div#footer{background:#BFBD93;}
div#footer p{margin:0;padding:5px 10px}
div#container{width:700px;margin:0 auto}
div#content{float:right;width:500px}
div#navigation{float:left;width:200px}
div#extra{float:left;clear:left;width:200px}
div#footer{clear:both;width:100%}
</style>
