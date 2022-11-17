<template>
  <div class="container">
    <h3>comment</h3>
    <form @submit.prevent class="formbox">
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
      },
      reviewDetail() {
        
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
      this.$store.dispatch('getReview')
    }
}
</script>

<style>
/* .container {

} */
.formbox {
    display: flex;
    flex-direction: column;
    width: 300px;
}
</style>