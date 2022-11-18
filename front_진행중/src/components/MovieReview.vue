<template>
  <div class="container">
    <h3>comment</h3>
    <form @submit.prevent class="review_formbox">
        <input type="text" v-model="title">
        <input type="text" v-model="content">
        <button @click="createReview">제출</button>
    </form>
    <hr>
    <div v-for="review in reviews" :key="review.id" >
      <ul>
        <li @click="reviewDetail"> 제목 : {{ review.title}} </li>
        <li> 작성자 : {{review.userName}} </li>
      </ul>
      <hr>
      
    </div>
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
      reviewDetail() {
        const movieid = this.movieID
        this.$router.push({ name: 'review', params: { id:movieid }})
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
/* .container {

} */
.review_formbox {
    display: flex;
    flex-direction: column;
    width: 300px;
}
</style>