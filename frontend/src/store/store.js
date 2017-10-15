import Vuex from 'vuex'
import Vue from 'vue'
import * as types from './types'

import axios from 'axios';
import qs from 'qs';

Vue.use(Vuex);
export default new Vuex.Store({
	state: {
		user: null,
		token: null
	},
	mutations: {
		[types.LOGIN]: (state, data) => {
            localStorage.token = data;
            state.token = data;
        },
        [types.LOGOUT]: (state) => {
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            state.token = null;
            state.user = null;
        },
        [types.USER]: (state, user) => {
            localStorage.user = JSON.stringify(user);
            state.user = JSON.parse(localStorage.user)
        }
    },
    getters:{
        user: state => {
            return state.user
        }
    },
    actions:{
        Login({ commit }, user) {

            axios({
                method: 'post',
                url: 'http://127.0.0.1:8888/login',
                data: qs.stringify(user)
            }).then(response => {
                // alert(user.username);
                if (response.data.token) {
                    commit(types.USER, response.data);
                    commit(types.LOGIN, response.data.token);
                }
                // console.log(response.data.token)
                // alert(response.data.token)
            }).catch(function (error) {
                console.log(error);
            })
            //         console.log(error);
            //     })
            // alert(user.username);
            // alert(user.password);
            // axios.post('http://127.0.0.1:8888/login', qs.stringify({
            //     // username: user.username,
            //     // password: user.password
            //     username: 'sugare',
            //     password: '123456'
            //     }),{}).then(response => {
            //         // if (response.data.token) {
            //         //     commit(types.USER, username);
            //         //     commit(types.LOGIN, response.data.token);
            //         // } else { 
            //         //     alert(1);
            //         // }
            //         alert(2);
            //     }).catch(function (error) {
            //         console.log(error);
            //     })
            // console.log(12);

        }
    }
})