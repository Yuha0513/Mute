<template>
    <div class="reco_container">
        <RecommandItem
            v-for="recommand in Recommands"
            :key="recommand.id"
            :recommand="recommand"
        />
    </div>

  
</template>


<script>
import RecommandItem from '@/components/Movie/RecommandItem'


export default {
    name: 'RecommandMovie',
    components: {
        RecommandItem
    },
    methods: {
        getRecommand() {
            this.$store.dispatch('getRecommand')
        }
    },
    computed: {
        Recommands() {
            return this.$store.state.recommandMovie.movies
        }
    },
    created() {
        this.getRecommand()
    },

    
}
</script>

<style>
.reco_container {
    display: flex;
    width: 920px;
    height: auto;
    margin: 30px auto;
}

</style>