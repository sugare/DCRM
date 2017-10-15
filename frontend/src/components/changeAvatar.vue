<template>
    <div>
		<my-upload field="myFileName"
	        @crop-success="cropSuccess"
	        @crop-upload-success="cropUploadSuccess"
	        @crop-upload-fail="cropUploadFail"
	        v-model="show"
			:width="150"
			:height="150"
			url="http://127.0.0.1:8888/upload"
			:params="params"
			img-format="png"></my-upload>

		<br><br>
		<img ref='ttt' :src="user.user_img" class="img-thumbnail">
		<br><br>
		<a class="btn btn-default" @click="toggleShow">上传头像</a>
	    <Button type="primary" :loading="loading" v-if="imgDataUrl" @click="change">
	        <span v-if="!loading" >确认更换</span>
	        <span v-else>Loading...</span>
	    </Button>
	</div>

</template>


<script>
	import 'babel-polyfill'; // es6 shim
	import myUpload from 'vue-image-crop-upload';
	import qs from 'qs';
	import * as types from '../store/types';
	import changePass from './changePass.vue';
export default {
		data(){
			return {
				loading: false,
				show: false,
				params:{
					token: '123456798',
					name: 'avatar'
				},
				imgDataUrl: ''
            }
		},
		components: {
			'my-upload': myUpload,
		},
        computed:{
             user () {
                return this.$store.getters.user
              }
        },
		methods: {
			change(){
				this.loading = true;
				this.$axios.post('http://127.0.0.1:8888/user', qs.stringify({
					user_name: this.user.user_name,
					user_img: this.imgDataUrl
					}),{}).then(response => {
						this.user.user_img = this.imgDataUrl
						this.$store.commit(types.USER, this.user);
						this.loading = false;
						this.$Message.success({content: '头像更改成功',duration: 10})
					}).catch(function (error) {
						alert('sorry upload fail!')
					})
			},
			toggleShow() {
				this.show = !this.show;
			},

			cropSuccess(imgDataUrl, field){
				console.log('-------- crop success --------');
				// this.imgDataUrl = imgDataUrl;
				
				this.$axios.post('http://127.0.0.1:8888/imgdata', qs.stringify({
					imgData: imgDataUrl
					}),{}).then(response => {
						console.log(response.data.imgDataUrl)
						this.imgDataUrl = response.data.imgDataUrl
						this.$refs.ttt.src = this.imgDataUrl

					}).catch(function (error) {
						console.log(error);
					})
			},

			cropUploadSuccess(jsonData, field){
				console.log('-------- upload success --------');
				// console.log(jsonData);
				// console.log('field: ' + field);
				// this.$refs.ttt.src = this.imgDataUrl
			},

			cropUploadFail(status, field){
				console.log('-------- upload fail --------');
				// console.log(status);
				// console.log('field: ' + field);
			}
		}
	}
</script>