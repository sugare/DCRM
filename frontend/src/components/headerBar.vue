<style scoped>
    ::-webkit-input-placeholder { /* WebKit browsers */  
        color:    #A9A9A9;  
    }  
    :-moz-placeholder { /* Mozilla Firefox 4 to 18 */  
       color:    #A9A9A9;  
       opacity:  1;  
    }  
    ::-moz-placeholder { /* Mozilla Firefox 19+ */  
       color:    #A9A9A9;  
       opacity:  1;  
    }  
    :-ms-input-placeholder { /* Internet Explorer 10+ */  
       color:    #A9A9A9;  
    }
    .layout-header input{
        margin:0 0 0 30px;
        border-radius: 30px;
        font-size:22px;
        padding:0 16px;
        outline:0;
        color:#6a6f77;
        border:0.5px solid #eee;

    }
    .layout-header input[type="text"]:focus{
        border:1px solid #57a3f3;
    }
</style>
<template>
    <div class="layout-header" style="border-bottom: 1px solid #eee;">
        <div style="float: left">
            <input placeholder="请输入客户名称" type="text" v-model="t1" @keyup="get($event)" @keydown.down="changeDown()" @keydown.up.prevent="changeUp()" />
        </div>

        <Dropdown style="margin: 0 0 0 650px">

            <Avatar size="large" :src="user.user_img" />

            <DropdownMenu slot="list" style="left: 650px;">
                <DropdownItem><router-link to="/settings">设置中心</router-link></DropdownItem>
                <DropdownItem><a @click="logout">退出登录</a></DropdownItem>
            </DropdownMenu>
        </Dropdown>

    </div>
</template>

<script type="text/javascript">
    import * as types from '../store/types'
    export default {
        name: 'headerBar',
        data(){
            return{
                t1:'',
                now:-1,
            }
        },
        computed:{
             user () {
                return this.$store.getters.user
              }
        },
        methods:{
            logout(){
                this.$store.commit(types.LOGOUT)
                let redirect = decodeURIComponent(this.$route.query.redirect || '/login');
                this.$router.push({
                    path: redirect
                });
                // window.location.reload()
            },

            get:function(ev){
                if(ev.keyCode==38 || ev.keyCode==40)return;

                if(ev.keyCode==13){
                    window.open('https://www.baidu.com/s?wd='+this.t1);
                    this.t1='';
                }

                // this.$axios.jsonp('https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su',{
                //     wd:this.t1
                // },{
                //     jsonp:'cb'
                // }).then(function(res){
                //     this.myData=res.data.s;
                // },function(){
                    
                // });

                console.log(this.$jsonp);
            },

            changeDown:function(){
                this.now++;
                if(this.now==this.myData.length)this.now=-1;
                this.t1=this.myData[this.now];
            },

            changeUp:function(){
                this.now--;
                if(this.now==-2)this.now=this.myData.length-1;
                this.t1=this.myData[this.now];
            }
        }
    }
</script>