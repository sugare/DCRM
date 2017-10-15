<style>
    .table th, .table td { 
		text-align: center; 
	}
	th {
		font-size: 14px;
		font-weight: bold;
	}
   	.gray{
        background: #ccc;
    }
    .demo-spin-icon-load{
        animation: ani-demo-spin 1s linear infinite;
    }
    @keyframes ani-demo-spin {
        from { transform: rotate(0deg);}
        50%  { transform: rotate(180deg);}
        to   { transform: rotate(360deg);}
    }
    .demo-spin-col{
        /*height: 900px;*/

        /*position: absolute;*/
        border: 1px solid #eee;
    }
</style>
<template>
<transition name="fade">
	<div style="background:#fff;">
	  <br>
      <div>

    <Input v-model="value1" @on-enter="filterData" style="margin-left: 20px;width:300px;" placeholder="请输入关键字"></Input>

    <Button style="margin-left:20px;" type="ghost" icon="ios-search" @click="filterData">搜索</Button>
    <Button style="margin-left:20px;" type="ghost" icon="plus" @click="modal11 = true">添加</Button>
    <Button style="margin-left:40px;" type="ghost" icon="arrow-down-c" @click="exportData">导出客户信息</Button>
        <Modal
            v-model="modal11"
            title="添加客户"
            @on-ok="handleSubmit('formValidate')"
            @on-cancel="handleReset('formValidate')">
            <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                <Form-item label="客户名字" prop="customer_name">
                    <Input v-model="formValidate.customer_name" placeholder="请输入姓名"></Input>
                </Form-item>

                <Form-item label="客户地址" prop="customer_addr">
                    <Input v-model="formValidate.customer_addr" placeholder="请输入地址"></Input>
                </Form-item>
                
                <Form-item label="联系人" prop="customer_people">
                    <Input v-model="formValidate.customer_people" placeholder="请输入联系人"></Input>
                </Form-item>
                
                <Form-item label="联系电话" prop="customer_tel">
                    <Input v-model="formValidate.customer_tel" placeholder="请输入联系方式"></Input>
                </Form-item>

                <label class="ivu-form-item-label" style="width: 80px;">客户级别 </label><Rate v-model="customer_level"></Rate>
            </Form>
                
        </Modal>
      </div>

	<br>
	<hr>
	<br>
    <div class="demo-spin-article">
        <div class="content" v-if="tt" style="margin-left:10px;" >
            <Table border stripe  :columns="columns7" :data="tt" ref="table"></Table>
        </div>
        <Spin size="large" fix v-if="loading"></Spin>
    </div>

</div>
</transition>
</template>

<script type="text/javascript">
import qs from 'qs'
	export default {
		data(){
			return{
                value1:'',
                model1:'',
                cityList: [1,2,3,4,5],
                formValidate: {
                    customer_name: '',
                    customer_addr: '',
                    customer_people: '',
                    customer_tel: ''
                },
                ruleValidate: {
                    customer_name: [
                        { required: true, message: '姓名不能为空', trigger: 'blur' }
                    ],
                    customer_addr: [
                        { required: true, message: '地址不能为空', trigger: 'blur' }
                    ],
                    customer_people: [
                        { required: true, message: '联系人不能为空', trigger: 'blur' }
                    ],
                    customer_tel: [
                        { required: true, message: '联系电话不能为空', trigger: 'blur' },
                        { len:11, message: '手机格式不正确', trigger: 'blur' }
                    ]
                },
                modal11:false,
                customer_level: 1,
                value3:'',
                data3:[1,2,3,4,5],
				columns7: [
                    {
                        title: '客户名',
                        key: 'customer_name',
                        align: "center",
                        filters: [
                            {
                                label: '银行',
                                value: 1
                            },
                            {
                                label: '其他',
                                value: 2
                            }
                        ],
                        filterMultiple: false,
                        filterMethod (value, row) {
                            if (value === 1) {
                                return row.customer_name > 25;
                            } else if (value === 2) {
                                return row.customer_name === 'butterfly';
                            }
                        }
                    },
                    {
                        title: '地址',
                        key: 'customer_addr',
                        align: "center",
                        filters: [
                            {
                                label: '北京',
                                value: '北京'
                            },
                            {
                                label: '上海',
                                value: '上海'
                            },
                            {
                                label: '深圳',
                                value: '深圳'
                            }
                        ],
                        filterMethod (value, row) {
                            return row.customer_addr.indexOf(value) > -1;
                        }
                    },
                    {
                        title: '联系人',
                        key: 'customer_people',
                        align: "center"
                    },
                    {
                        title: '联系方式',
                        key: 'customer_tel',
                        align: "center"
                    },
                    {
                        title: '客户等级',
                        key: 'customer_level',
                        align: "center",
                        sortable: true
                    },

                    {
                        title: '操作',
                        key: 'action',
                        width: 200,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '4px'
                                    },
                                    on: {
                                        click: () => {
                                            this.show(params.index)
                                        }
                                    }
                                }, '查看'),

                                h('Button', {
                                    props: {
                                        type: 'warning',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '4px'
                                    },
                                    on: {
                                        click: () => {
                                            this.edit(params.index)
                                        }
                                    }
                                }, '编辑'),


                                h('Poptip',{
                                    props: {
                                        confirm: true,
                                        title: "您确认删除这条内width: 4吗？",
                                        width: '400px'
                                    },
                                    on: {
                                        'on-ok': () => {
                                            this.ok();
                                        }
                                    }
                                }, [
                                    h('Button', {
                                        props: {
                                            type: 'error',
                                            size: 'small'
                                        },
                                        on: {
                                            click: () => {
                                                this.remove(params.index)
                                            }
                                        }
                                    }, '删除')


                                ])
                                        
                                // h('Button', {
                                //     props: {
                                //         type: 'error',
                                //         size: 'small'
                                //     },
                                //     on: {
                                //         click: () => {
                                //             this.remove(params.index)
                                //         }
                                //     }
                                // }, '删除')
                            ]);
                        }
                    }
                ],
                tt: null,
                loading: false
			}
		},
        created(){
            this.getCustomersData()
        },
        watch: {
            '$route': 'getCustomersData'
        },
		methods:{
            exportData() {
                this.$refs.table.exportCsv({
                        filename: '客户信息'
                    })
                },
            get:function(ev){
                if(ev.keyCode===13){
                    this.filterData();
                    alert(1);
                }
            },
            filterData(){
                this.loading = true,
                this.$axios({
                    method: 'get',
                    dataType: 'jsonp',
                    url: 'http://127.0.0.1:8888/aa',
                    headers: {'Authorization':'bearer ' + localStorage.token},
                    params: {'title': this.value1}
                    
                }).then(response => {
                    // console.log(response)

                    localStorage.setItem('CustomersData',JSON.stringify(response.data));
                    // console.log(JSON.parse(localStorage.getItem('CustomersData')));
                    this.loading = false;
                    this.tt = JSON.parse(localStorage.getItem('CustomersData'))

                }).catch(function(err){
                    console.log(err);
                })
            },
            handleSubmit(name) {
                this.$refs[name].validate((valid) => {
                    if (valid) {
                        this.$axios.post('http://127.0.0.1:8888/api/customer/', qs.stringify({
                            customer_id:'',
                            customer_name: this.formValidate.customer_name,
                            customer_addr: this.formValidate.customer_addr,
                            customer_people: this.formValidate.customer_people,
                            customer_tel: this.formValidate.customer_tel,
                            customer_level: parseInt(this.customer_level),
                        }),{})
                            .then(response => {
                            if (response.status == 200){
                                this.$Modal.remove();
                                // window.location.reload()
                                this.filterData();
                            }

                        }).catch(function (error) {
                            console.log(error);
                        });
                        this.$refs[name].resetFields();
                        this.$Message.success('提交成功!')
                    } else {
                        this.$Modal.remove();
                        alert('sorry');
                        this.$Message.error('表单验证失败!');
                    }
                })
            },
            handleReset (name) {
                this.$refs[name].resetFields();
            },
            getCustomersData(){
                this.loading = true;
                this.$axios({
                    method: 'get',
                    dataType: 'jsonp',
                    url: 'http://127.0.0.1:8888/api/customer/',
                    headers: {'Authorization':'bearer ' + localStorage.token},
                    
                }).then(response => {
                    console.log(response)

                    localStorage.setItem('CustomersData',JSON.stringify(response.data));
                    console.log(JSON.parse(localStorage.getItem('CustomersData')));
                    this.loading = false;
                    this.tt = JSON.parse(localStorage.getItem('CustomersData'))

                }).catch(function(err){
                    console.log(err);
                })
            },
			show (index) {
                this.$Modal.info({
                    title: '用户信息',
                    width: 500,
                    okText:'关闭',
                    content: `
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>key</th>
                                    <th>value</th>
                                </th>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>ID</td>
                                    <td>${this.tt[index].customer_id}</td>
                                <tr>
                                <tr>
                                    <td>客户名</td>
                                    <td>${this.tt[index].customer_name}</td>
                                <tr>
                                <tr>
                                    <td>客户地址</td>
                                    <td>${this.tt[index].customer_addr}</td>
                                <tr>
                                <tr>
                                    <td>联系人</td>
                                    <td>${this.tt[index].customer_people}</td>
                                <tr>
                                <tr>
                                    <td>联系方式</td>
                                    <td>${this.tt[index].customer_tel}</td>
                                <tr>
                                <tr>
                                    <td>客户等级</td>
                                    <td>${this.tt[index].customer_level}</td>
                                <tr>
                            </tbody>
                        </table>`
                })
            },
            edit(index){
                this.$Modal.confirm({
                    width: 600,
                    title: 'edit customer info',
                    loading: 'true',
                    content: `<form class="form-horizontal" id="editForm" action="http://localhost:8888/api/customer/" method="post">

                                  <div class="form-group" style="display:none;">
                                    <label for="customer_id" class="col-sm-2 control-label">客户名字：</label>
                                    <div class="col-sm-10">
                                      <input type="text" class="form-control" id="customer_id" placeholder="客户名字：" name="customer_id" value="${this.tt[index].customer_id}">
                                    </div>
                                  </div>

                                  <div class="form-group">
                                    <label for="customer_name" class="col-sm-2 control-label">客户名字：</label>
                                    <div class="col-sm-10">
                                      <input type="text" class="form-control" id="customer_name" placeholder="客户名字：" name="customer_name" value="${this.tt[index].customer_people}">
                                    </div>
                                  </div>

                                  <div class="form-group">
                                    <label for="customer_addr" class="col-sm-2 control-label">客户地址：</label>
                                    <div class="col-sm-10">
                                      <input type="text
                                      w" class="form-control" id="customer_addr" placeholder="客户地址：" value="${this.tt[index].customer_addr}">
                                    </div>
                                  </div>

                                  <div class="form-group">
                                    <label for="customer_people" class="col-sm-2 control-label">联系人：</label>
                                    <div class="col-sm-10">
                                      <input type="text
                                      w" class="form-control" id="customer_people" placeholder="联系人：" value="${this.tt[index].customer_people}">
                                    </div>
                                  </div>

                                  <div class="form-group">
                                    <label for="customer_tel" class="col-sm-2 control-label">联系方式：</label>
                                    <div class="col-sm-10">
                                      <input type="text
                                      w" class="form-control" id="customer_tel" placeholder="联系方式：" value="${this.tt[index].customer_tel}">
                                    </div>
                                  </div>

                                  <div class="form-group">
                                    <label for="customer_level" class="col-sm-2 control-label">客户等级：</label>
                                    <div class="col-sm-10">
                                      <input type="text
                                      w" class="form-control" id="customer_level" placeholder="客户等级：" value="${this.tt[index].customer_level}">
                                    </div>
                                  </div>

                              </form>`,
                    onOk: () => {
                        this.$Message.info('点击了确定');

                        this.$axios.post('http://127.0.0.1:8888/api/customer/', qs.stringify({
                            customer_id: document.getElementById("customer_id").value,
                            customer_name: document.getElementById("customer_name").value,
                            customer_addr: document.getElementById("customer_addr").value,
                            customer_people: document.getElementById("customer_people").value,
                            customer_tel: document.getElementById("customer_tel").value,
                            customer_level: document.getElementById("customer_level").value
                            // password: this.password
                            }),{}).then(response => {
                                // console.log(response);
                                // this.token = response.data.token
                                // console.log(this.token)
                                // if (this.token) {
                                //     this.$store.commit(types.LOGIN, this.token)
                                //     let redirect = decodeURIComponent(this.$route.query.redirect || '/dashboard');
                                //     this.$router.push({
                                //         path: redirect
                                //     })
                                // }
                                // window.location.href='http://127.0.0.1:8080/index';
                                // this.getCustomersData();
                                console.log('ok');
                                this.$Modal.remove();
                                window.location.reload()
                            }).catch(function (error) {
                                console.log(error);
                            });
                    },
                    onCancel: () => {
                        this.$Message.info('点击了取消');
                    },
                    cancelText: 'Cancel'

                })
            },
            remove (index) {
                this.tt.splice(index, 1);
            },
            handleSearch1 (value) {
                this.tt = !value ? [] : [
                    value,
                    value + value,
                    value + value + value
                ];
            },
            ok() {
                // this.$Message.info('点击了确定');
                alert(1);
            },
            cancel(){
                alert(2);
            }
	    }

	}	

</script>