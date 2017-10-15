<template>
	<div style="margin: 10px;">
		<Row>
	        <Col span="14" push=1>
	        <br>
	        <h4 style="border-bottom: 1px solid #eee;padding: 10px;">设置中心</h4>
	        <br>
            <Tabs type="card" style="">
		        <TabPane label="基本资料">
		        	<Form :model="formItem" :label-width="80" style="width: 600px; margin: 10px;">
				        <FormItem label="用户名"  >
				            <Input v-model="formItem.input" placeholder="请输入"></Input>
				        </FormItem>
				        <FormItem label="选择器">
				            <Select v-model="formItem.select" placeholder="请选择">
				                <Option value="beijing">北京市</Option>
				                <Option value="shanghai">上海市</Option>
				                <Option value="shenzhen">深圳市</Option>
				            </Select>
				        </FormItem>
				        <FormItem label="日期控件">
				            <Row>
				                <Col span="11">
				                    <DatePicker type="date" placeholder="选择日期" v-model="formItem.date"></DatePicker>
				                </Col>
				                <Col span="2" style="text-align: center">-</Col>
				                <Col span="11">
				                    <TimePicker type="time" placeholder="选择时间" v-model="formItem.time"></TimePicker>
				                </Col>
				            </Row>
				        </FormItem>
				        <FormItem label="单选框">
				            <RadioGroup v-model="formItem.radio">
				                <Radio label="male">男</Radio>
				                <Radio label="female">女</Radio>
				            </RadioGroup>
				        </FormItem>
				        <FormItem label="多选框">
				            <CheckboxGroup v-model="formItem.checkbox">
				                <Checkbox label="JAVA"></Checkbox>
				                <Checkbox label="Pathon"></Checkbox>
				                <Checkbox label="C/C++"></Checkbox>
				                <Checkbox label="JS"></Checkbox>
				            </CheckboxGroup>
				        </FormItem>
				        <FormItem label="开关">
				            <i-switch v-model="formItem.switch" size="large">
				                <span slot="open">开启</span>
				                <span slot="close">关闭</span>
				            </i-switch>
				        </FormItem>
				        <FormItem label="滑块">
				            <Slider v-model="formItem.slider" range></Slider>
				        </FormItem>
				        <FormItem label="文本域">
				            <Input v-model="formItem.textarea" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入..."></Input>
				        </FormItem>
				        <FormItem>
				            <Button type="primary">提交</Button>
				            <Button type="ghost" style="margin-left: 8px">取消</Button>
				        </FormItem>
				    </Form>

		        </TabPane>
		        <TabPane label="修改密码">
			        <div style="margin: 10px;">
					    <changePass></changePass>	
			        </div>

		        </TabPane>
		    </Tabs>
	        </Col>

	        <Col span="6" style="text-align:center; margin-top: 50px;margin-left:100px;border-left: 1px solid #eee;">
	        <changeAvatar></changeAvatar>
	        </Col>
	    </Row>
	</div>
</template>


<script>
	import 'babel-polyfill'; // es6 shim
	import myUpload from 'vue-image-crop-upload';
	import qs from 'qs';
	import * as types from '../store/types';
	import changePass from './changePass.vue';
	import changeAvatar from './changeAvatar.vue';

export default {
		data(){
			return {
				formLeft: {
                    input1: '',
                    input2: '',
                    input3: ''
                },
				loading: false,
				value1: '1',
				show: false,
				params:{
					token: '123456798',
					name: 'avatar'
				},
				imgDataUrl: '',
				// img: this.user.user_img
				formItem: {
                    input: '',
                    select: '',
                    radio: 'male',
                    checkbox: [],
                    switch: true,
                    date: '',
                    time: '',
                    slider: [20, 50],
                    textarea: ''
                }
            }
		},
		components: {
			'my-upload': myUpload,
			'changePass': changePass,
			'changeAvatar': changeAvatar
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


				// console.log(imgDataUrl);
				// console.log(field)

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