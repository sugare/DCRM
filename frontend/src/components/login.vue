<style type="text/css">
	.form-bg{
        background: #00b4ef;
    }
    .form-horizontal{
        background: #fff;
        padding-bottom: 40px;
        border-radius: 15px;
        text-align: center;
    }
    .form-horizontal .heading{
        display: block;
        font-size: 35px;
        font-weight: 700;
        padding: 35px 0;
        border-bottom: 1px solid #f0f0f0;
        margin-bottom: 30px;
    }
    .form-horizontal .form-group{
        padding: 0 40px;
        margin: 0 0 25px 0;
        position: relative;
    }
    .form-horizontal .form-control{
        background: #f0f0f0;
        border: none;
        border-radius: 20px;
        box-shadow: none;
        padding: 0 20px 0 45px;
        height: 40px;
        transition: all 0.3s ease 0s;
    }
    .form-horizontal .form-control:focus{
        background: #e0e0e0;
        box-shadow: none;
        outline: 0 none;
    }
    .form-horizontal .form-group i{
        position: absolute;
        top: 12px;
        left: 60px;
        font-size: 17px;
        color: #c8c8c8;
        transition : all 0.5s ease 0s;
    }
    .form-horizontal .form-control:focus + i{
        color: #00b4ef;
    }
    .form-horizontal .fa-question-circle{
        display: inline-block;
        position: absolute;
        top: 12px;
        right: 60px;
        font-size: 20px;
        color: #808080;
        transition: all 0.5s ease 0s;
    }
    .form-horizontal .fa-question-circle:hover{
        color: #000;
    }
    .form-horizontal .main-checkbox{
        float: left;
        width: 20px;
        height: 20px;
        background: #11a3fc;
        border-radius: 50%;
        position: relative;
        margin: 5px 0 0 5px;
        border: 1px solid #11a3fc;
    }
    .form-horizontal .main-checkbox label{
        width: 20px;
        height: 20px;
        position: absolute;
        top: 0;
        left: 0;
        cursor: pointer;
    }
    .form-horizontal .main-checkbox label:after{
        content: "";
        width: 10px;
        height: 5px;
        position: absolute;
        top: 5px;
        left: 4px;
        border: 3px solid #fff;
        border-top: none;
        border-right: none;
        background: transparent;
        opacity: 0;
        -webkit-transform: rotate(-45deg);
        transform: rotate(-45deg);
    }
    .form-horizontal .main-checkbox input[type=checkbox]{
        visibility: hidden;
    }
    .form-horizontal .main-checkbox input[type=checkbox]:checked + label:after{
        opacity: 1;
    }
    .form-horizontal .text{
        float: left;
        margin-left: 7px;
        line-height: 20px;
        padding-top: 5px;
        text-transform: capitalize;
    }
    .form-horizontal .btn{
        float: right;
        font-size: 14px;
        color: #fff;
        background: #00b4ef;
        border-radius: 30px;
        padding: 10px 25px;
        border: none;
        text-transform: capitalize;
        transition: all 0.5s ease 0s;
    }
    @media only screen and (max-width: 479px){
        .form-horizontal .form-group{
            padding: 0 25px;
        }
        .form-horizontal .form-group i{
            left: 45px;
        }
        .form-horizontal .btn{
            padding: 10px 20px;
        }
    }
</style>
<template>
	<div class="container">
    <div class="row">
        <div class="col-md-offset-3 col-md-6">
        <br><br>
            <form class="form-horizontal">
                <span class="heading">用户登录</span>
                <div class="form-group">
                    <input type="text" class="form-control" v-model="username" placeholder="用户名或电子邮件">
                    <i class="fa fa-user"></i>
                </div>

                <div class="form-group help">
                    <input type="password" class="form-control" v-model="password" placeholder="密　码">
                    <i class="fa fa-lock"></i>
                    <a href="#" class="fa fa-question-circle"></a>
                </div>
                <div class="form-group">
                    <div class="main-checkbox">
                        <input type="checkbox" id="checkbox1" name="check"/>
                        <label for="checkbox1"></label>
                    </div>
                    <span class="text">Remember me</span>
                    <button @click="login" class="btn btn-default">登录</button>
                </div>
            </form>
        </div>
    </div>

<!-- 	<Modal
        v-model="modal1"
        title="用户登录"
        ok-text="登录"
        @on-ok="login"
        :mask-closable="false"
        @on-cancel="cancel">
          <Input v-model="username" required>
                <span slot="prepend">用户名：</span>
                <span slot="append"></span>
            </Input>
            <br>
          <Input v-model="password">
                <span slot="prepend">密&nbsp;&nbsp;&nbsp;&nbsp;码：</span>
                <span slot="append"></span>
            </Input>
			</Modal> -->
	</div>
</template>

<script type="text/javascript">
  	import * as types from '../store/types';
  	import qs from 'qs';
	
	export default {
		data () {
		    return {
		      username:'',
		      password:'',
		      modal1:true,
		    }
		},
		methods: {
    		login(){

                this.$store.dispatch('Login', {username:this.username, password: this.password});
                

    // 			if (this.username === '' || this.password === ''){
    // 				alert("What's wrong?")
    // 			} else {

    	// 		axios.post('http://127.0.0.1:8888/login', qs.stringify({
					// username: this.username,
					// password: this.password
					// }),{}).then(response => {
					// 	this.token = response.data.token

					// 	if (this.token) {
     //                        this.$store.commit(types.USER, this.username);


		   //      			this.$store.commit(types.LOGIN, this.token);
		   //      			let redirect = decodeURIComponent(this.$route.query.redirect || '/dashboard');
		   //      			this.$router.push({
		   //          			path: redirect
		   //        			});
		   //        			window.location.reload()
		   //      		}

					// }).catch(function (error) {
					// 	console.log(error);
					// })
				
      		},
      		cancel () {
		        this.$Message.info('点击了取消');
		    }
    	}
    }
</script>