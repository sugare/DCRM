<style type="text/css">
    .layout-logo-left{
        width: 90%;
        height: 60px;
        border-radius: 3px;
        padding-top: 15px;
        padding-left: 25px;
        border-bottom: 1px solid #eee;
    }
    .sidebar-border {
        border-right: 1px solid #eee;
    }
    .layout-menu-left{
        position: fixed;
        /*width: 250px;*/
    }
</style>
<template>
    <div>
        <Menu class="sidebar-border"  ref="menu" :active-name="activeName" width="auto" :open-names="['1','2','3']" @on-select="handleSelect">
            <div class="layout-logo-left">
              <h3>Daocloud CRM</h3>
            </div>

            <MenuItem name="/dashboard">
                <Icon type="document-text"></Icon>
                Dashboard
            </MenuItem>            

            <Submenu name="1">
                <template slot="title">
                    <Icon type="ios-navigate"></Icon>
                    客户管理
                </template>
                <Menu-item name="/customers">客户列表</Menu-item>
            </Submenu>

            <Submenu name="2">
                <template slot="title">
                    <Icon type="ios-keypad"></Icon>
                    统计分析
                </template>
                <MenuItem name="/a">新增和启动</MenuItem>
                <MenuItem name="/b">活跃分析</MenuItem>
                <MenuItem name="/c">时段分析</MenuItem>
            </Submenu>

            <Submenu name="3">
                <template slot="title">
                    <Icon type="ios-analytics"></Icon>
                  留存
                </template>
                <MenuItem name="/d">用户留存</MenuItem>
                <MenuItem name="/d">流失用户</MenuItem>
                <MenuItem name="/e">CRM用户管理</MenuItem>
            </Submenu>
        </Menu>
    </div>
</template>

<script>
  export default {
    name: 'sidebar',
    data () {
      return {
        activeName: '',
        openNames: []
      }
    },
    created () {
      this.update()
    },
    methods: {
      handleSelect (name) {
        this.$router.push(name)
      },
      update (route) {
        const path = route ? route.path : this.$route.path
        const openName = path.split('/')[1]
        const activeName = '/' + openName

        this.$set(this, 'activeName', activeName)
        this.$set(this, 'openNames', [openName])

        this.$nextTick(() => {
          this.$refs.menu.updateActiveName()
          this.$refs.menu.$children.forEach((item) => {
            item.opened = false
          })
          this.$refs.menu.updateOpened()
        })
      }
    }
  }
</script>