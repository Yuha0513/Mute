<template>
  <div>
    <div>
        <label for="selfimg">프로필</label>
        <input type="text" v-model="selfimg">
    </div>
    <div>
        <label for="selfimg">프로필2</label>
        <input type="text" v-model="otherimg">
    </div>
    <div>
        <label for="selfimg">자기소개</label>
        <input type="text" v-model="selfintroduce">
    </div>
    <button @click="makeUserDetail">submit</button>
  </div>
</template>

<script>
export default {
    name: 'UserDetail',
    data() {
        return {
            selfintroduce: null,
            selfimg: "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAzMDhfMjAg%2FMDAxNjQ2NjY1NTM5MjU3.n1W30ivAbDtkfawKgEvOBPRoc7W-N_2s5L1KvbmfCOQg.P65g4u6WKjUoacf6RIVyjIbvlbbi1JIOLBN3FnhiSVMg.JPEG.bo752%2F275278076%25A3%25DF1147796125953926%25A3%25DF4913836884456917253%25A3%25DFn.jpg&type=sc960_832",
            otherimg: 'http://i1112.photobucket.com/albums/k497/animalsbeingdicks/abd-3-12-2015.gif~original',
        }
    },
    methods: {
        makeUserDetail() {
            const payload = {
                selfintroduce:this.selfintroduce,
                otherimg: this.otherimg,
            }
            this.$store.dispatch('makeUserDetail', payload)
        },
    },
    computed: {

    }
}
</script>

<style>

</style>