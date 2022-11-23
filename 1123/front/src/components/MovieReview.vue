<template>
  <div class="review_container">
    <h4>당신의 리뷰를 남겨주세요</h4>
    <hr>
    <div v-for="review in reviews" :key="review.id">
      <ul class="review_area">
        <li class="user_review"> 작성자 : <span @click="goUserProfile(review.userName, $event)">{{review.userName}}</span></li>
        <li class="user_review"> {{ review.content }} </li>
        <button @click="reviewDelete(review, $event)" class="small_button">삭제</button>
        <button data-bs-toggle="modal" class="small_button" data-bs-target="#exampleModal" @click="getReviewid(review, $event)">수정</button>
      </ul>
      
      
    </div>
    <form @submit.prevent class="review_formbox">
      <div class="review_input">
        <textarea v-model="content" cols="30" rows="5"></textarea>
        <!-- <input type="text" v-model="content"> -->
      </div>
      <div class="button_area">
        <button @click="createReview" class="big-button">등록</button>
      </div>
    </form>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">리뷰 수정</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <textarea cols="30" rows="10" v-model="newcontent"></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary"  @click="reviewUpdate" data-bs-dismiss="modal">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>


export default {
    name: 'MovieReview',
    data() {
      return {
        content: '',
        newcontent: '',
        updateid: '',
      }
    },
    methods: {
      createReview() {

        const payload = {
          content: this.content,
          movieID: this.movieID
        }
        this.$store.dispatch('createReview', payload)
        this.title = '',
        this.content = ''
        
      },

      reviewDelete(event) {
        const payload = {
          event: event,
          movieID: this.movieID
        }
        this.$store.dispatch('reviewDelete', payload)

      },
      reviewUpdate() {
        const payload = {
          newcontent: this.newcontent,
          movieID: this.movieID,
          reviewId: this.updateid
        }
        this.$store.dispatch('reviewUpdate', payload)
      },

      goUserProfile(event) {
        this.$router.push({ name: 'otheruser', params: { username:event }})
        this.$store.dispatch('getOtherInfo',event)
      },

      getReviewid(event) {
        this.updateid = event.id
      }

    },
    props: {
      movieID:Number,
    },
    computed: {
      reviews() {
        return this.$store.getters.reviews
      }
    },
    created() {
      const movieid = this.movieID
      this.$store.dispatch('getReview',movieid)
    },
    mounted() {
      const movieid = this.movieID
      this.$store.dispatch('getReview',movieid)
    },
    beforeMount() {
      const movieid = this.movieID
      this.$store.dispatch('getReview',movieid)
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@500;600&display=swap');

:root {
  --colorShadeA: rgb(106, 163, 137);
  --colorShadeB: rgb(121, 186, 156);
  --colorShadeC: rgb(150, 232, 195);
  --colorShadeD: rgb(187, 232, 211);
  --colorShadeE: rgb(205, 255, 232);
}
.review_container {
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: left;
  width: 1465px;
}
.review_formbox {
    display: flex;
    /* background-color: rgb(224, 255, 255); */
    width: 1400px;
    border-radius: 10px;
    height: 250px;
    /* flex-direction: column;
    /* width: 1465px; */
}
.review_input{
  display: flex;
  flex-direction: column;
  width: 1200px;
  margin-top: 43px;
  margin-left: 40px;
}
.button_area{
  /* padding-top: 70px; */
  padding-left: 60px;
}
/* .review_button {

  background: transparent;
  color: rgb(48, 47, 47);
  border: 2px solid rgb(41, 40, 40);
  font-size: 20px;
  letter-spacing: 2px;
  padding: 25px 80px;
  text-transform: uppercase;
  cursor: pointer;
  display: inline-block;
  margin: 15px 30px;
  -webkit-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}
.review_button:hover {
  background-color: rgb(0, 0, 0);
  color: rgb(255, 255, 255);
  -webkit-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
} */

button {
  /* position: relative; */
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-size: 1rem;
  color: var(--colorShadeA);
  font-weight: 700;
  text-transform: uppercase;
  font-family: inherit;
  /* margin-left: 5px; */
  margin-top: 20px;
  /* margin-bottom: 100px; */
}

button.big-button {
  width: 90px;
  height: 50px;
  /* padding: 1em 2em; */
  border: 2px solid var(--colorShadeA);
  border-radius: 1em;
  background: var(--colorShadeE);
  transform-style: preserve-3d;
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
  margin-top: 70px;
}
button.big-button::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--colorShadeC);
  border-radius: inherit;
  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.75em 0 0 var(--colorShadeA);
  transform: translate3d(0, 0.75em, -1em);
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}

button.big-button:hover {
  background: var(--colorShadeD);
  transform: translate(0, 0.375em);
}

button.big-button:hover::before {
  transform: translate3d(0, 0.75em, -1em);
}

button.big-button:active {
  transform: translate(0em, 0.75em);
}

button.big-button:active::before {
  transform: translate3d(0, 0, -1em);

  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.25em 0 0 var(--colorShadeB);
}
textarea {
	border: 2px solid rgb(161, 161, 161);
  outline-color: rgb(121, 186, 156);
}
.review_area{
  padding-top: 15px;
  padding-bottom: 15px;
  margin-top: 15px;
  background-color:rgba(187, 232, 211, 0.493);
  border-radius: 7px;
  /* width: 1100px;
  height: 180px; */

}
.user_review {
  margin-top: 10px;
}

button.small_button {
  width: 40px;
  height: 25px;
  /* padding: 1em 2em; */
  border: 2px solid var(--colorShadeA);
  border-radius: 1em;
  background: var(--colorShadeE);
  transform-style: preserve-3d;
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
  font-size: x-small;
  margin-left: 5px;
  margin-bottom: 5px;
}
button.small_button::before {
  position: absolute;
  content: "";
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--colorShadeC);
  border-radius: inherit;
  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.75em 0 0 var(--colorShadeA);
  transform: translate3d(0, 0.75em, -1em);
  transition: all 175ms cubic-bezier(0, 0, 1, 1);
}

button.small_button:hover {
  background: var(--colorShadeD);
  transform: translate(0, 0.375em);
}

button.small_button:hover::before {
  transform: translate3d(0, 0.75em, -1em);
}

button.small_button:active {
  transform: translate(0em, 0.75em);
}

button.small_button:active::before {
  transform: translate3d(0, 0, -1em);

  box-shadow: 0 0 0 2px var(--colorShadeB), 0 0.25em 0 0 var(--colorShadeB);
}
</style>
