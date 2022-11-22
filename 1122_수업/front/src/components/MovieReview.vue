<template>
  <div class="review_container">
    <h3>comment</h3>
    <hr>
    <div v-for="review in reviews" :key="review.id" >
      <ul>
        <li> 제목 : {{ review.title }} </li>
        <li> 작성자 : <span @click="goUserProfile(review.userName, $event)">{{review.userName}}</span></li>
        <button @click="reviewDelete(review, $event)">delete</button>
      </ul>
      <hr>
      
    </div>
    <form @submit.prevent class="review_formbox">
        <input type="text" v-model="title">
        <input type="text" v-model="content">
        <button @click="createReview">제출</button>
    </form>
  </div>

</template>

<script>
export default {
    name: 'MovieReview',
    data() {
      return {
        title: '',
        content: '',
      }
    },
    methods: {
      createReview() {
        const payload = {
          title: this.title,
          content: this.content,
          movieID: this.movieID
        }
        this.$store.dispatch('createReview', payload)
        this.title = '',
        this.content = ''
      },

      reviewDelete(event) {
        this.$store.dispatch('reviewDelete', event)

      },
      goUserProfile(event) {
        this.$router.push({ name: 'otheruser', params: { username:event }})
        this.$store.dispatch('getOtherInfo',event)
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


    }
}
</script>

<style>
.review_container {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.review_formbox {
    display: flex;
    flex-direction: column;
    width: 700px;
}
</style>