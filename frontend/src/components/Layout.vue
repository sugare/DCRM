<style scoped>
    .layout-header{
        padding-top: 10px;
        height: 60px;
        box-shadow: 0 1px 1px rgba(0,0,0,.1);
    }
    .layout-menu-right{
        left: 225px;
        min-height: 600px;

    }
</style>
<template>
        <div class="layout">
            <Row type="flex">
                <Col span="4" class="layout-menu-left"  style="box-shadow: -10px -10px 2px #888888;">
                    <sideBar ref="sidebar"></sideBar>
                </Col>
                <Col span="20" class="layout-menu-right">
                    <headerBar></headerBar>
                    <router-view></router-view>
                </Col>
            </Row>
        </div>
</template>

<script>
  import sideBar from './sideBar.vue'
  import headerBar from './headerBar.vue'

  export default {
    name: 'layout',
    components: {
      sideBar,
      headerBar
    },
    beforeRouteUpdate (to, from, next) {
      this.$nextTick(() => {
        this.$refs.sidebar.update(to)
      })
      next()
    }
  }
</script>

<!-- 
<style lang="scss" scoped src="./styles/index.scss">
</style>
 -->