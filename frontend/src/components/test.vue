<!-- <template>
    <div style="background-color:#fff">
    <br><br>
        <div :class="className" :id="id" :style="{height:height,width:width}"></div>
    </div>
</template>

<script>
import echarts from 'echarts'

export default {
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '1066px'
    },
    height: {
      type: String,
      default: '400px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(document.getElementById(this.id))

      this.chart.setOption({
        backgroundColor: '#fff;',
        title: {
          text: 'chart title',
          textStyle: {
            fontWeight: 'normal',
            fontSize: 16,
            color: '#000'
          },
          left: '6%'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            lineStyle: {
              color: '#57617B'
            }
          }
        },
        legend: {
          icon: 'rect',
          itemWidth: 14,
          itemHeight: 5,
          itemGap: 13,
          data: ['北京', '上海', '深圳'],
          right: '4%',
          textStyle: {
            fontSize: 12,
            color: '#000'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [{
          type: 'category',
          boundaryGap: false,
          axisLine: {
            lineStyle: {
              color: '#57617B'
            }
          },
          data: ['13:00', '13:05', '13:10', '13:15', '13:20', '13:25', '13:30', '13:35', '13:40', '13:45', '13:50', '13:55']
        }],
        yAxis: [{
          type: 'value',
          name: '单位（%）',
          axisTick: {
            show: false
          },
          axisLine: {
            lineStyle: {
              color: '#57617B'
            }
          },
          axisLabel: {
            margin: 10,
            textStyle: {
              fontSize: 14
            }
          },
          splitLine: {
            lineStyle: {
              color: '#57617B'
            }
          }
        }],
        series: [{
          name: '北京',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
            normal: {
              width: 1
            }
          },
          areaStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(137, 189, 27, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(137, 189, 27, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
            }
          },
          itemStyle: {
            normal: {
              color: 'rgb(137,189,27)',
              borderColor: 'rgba(137,189,2,0.27)',
              borderWidth: 12

            }
          },
          data: [220, 182, 191, 134, 150, 120, 110, 125, 145, 122, 165, 122]
        }, {
          name: '上海',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
            normal: {
              width: 1
            }
          },
          areaStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(0, 136, 212, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(0, 136, 212, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
            }
          },
          itemStyle: {
            normal: {
              color: 'rgb(0,136,212)',
              borderColor: 'rgba(0,136,212,0.2)',
              borderWidth: 12

            }
          },
          data: [120, 110, 125, 145, 122, 165, 122, 220, 182, 191, 134, 150]
        }, {
          name: '深圳',
          type: 'line',
          smooth: true,
          symbol: 'circle',
          symbolSize: 5,
          showSymbol: false,
          lineStyle: {
            normal: {
              width: 1
            }
          },
          areaStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                offset: 0,
                color: 'rgba(219, 50, 51, 0.3)'
              }, {
                offset: 0.8,
                color: 'rgba(219, 50, 51, 0)'
              }], false),
              shadowColor: 'rgba(0, 0, 0, 0.1)',
              shadowBlur: 10
            }
          },
          itemStyle: {
            normal: {
              color: 'rgb(219,50,51)',
              borderColor: 'rgba(219,50,51,0.2)',
              borderWidth: 12
            }
          },
          data: [220, 182, 125, 145, 122, 191, 134, 150, 120, 110, 165, 122]
        }]
      })
    }
  }
}
</script>
 -->

<template>
  <section class="login-wrap">

      <h3>系统登录</h3>
      <div class="fields">
        <!-- <n3-input class="field" v-model="account" placeholder="账号" width="320px"> -->
        <!-- </n3-input> -->
        <Input v-model="value" placeholder="请输入..." style="width: 300px"></Input>

        <!-- <n3-input class="field" v-model="password" type="password" placeholder="密码" width="320px"  @keyup.native.enter="check"> -->
        <Input v-model="value" placeholder="请输入..." style="width: 300px"></Input>

      </div>
      <div class="submit">
      </div>
    <canvas id="J_loginBackground"></canvas>
  </section>
</template>

<script>
  import { mapActions } from 'vuex'
  // import {
  //   STORAGE_KEY
  // } from '../utils/const'
  // import storage from '../utils/storage'
  
  function render() {
    var canvas = document.querySelector('#J_loginBackground');
    if (!canvas) {
      return;
    }
    var ctx = canvas.getContext('2d')
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    ctx.lineWidth = .3;
    ctx.strokeStyle = (new Color(150)).style;
    var i, j, i_dot, j_dot;
    var mousePosition = {
      x: 30 * canvas.width / 100,
      y: 30 * canvas.height / 100
    };
    var dots = {
      nb: 750,
      distance: 50,
      d_radius: 100,
      array: []
    };
    function colorValue(min) {
      return Math.floor(Math.random() * 255 + min);
    }
    
    function createColorStyle(r,g,b) {
      return 'rgba(' + r + ',' + g + ',' + b + ', 0.8)';
    }
    
    function mixComponents(comp1, weight1, comp2, weight2) {
      return (comp1 * weight1 + comp2 * weight2) / (weight1 + weight2);
    }
    
    function averageColorStyles(dot1, dot2) {
      var color1 = dot1.color,
          color2 = dot2.color;
      
      var r = mixComponents(color1.r, dot1.radius, color2.r, dot2.radius),
          g = mixComponents(color1.g, dot1.radius, color2.g, dot2.radius),
          b = mixComponents(color1.b, dot1.radius, color2.b, dot2.radius);
      return createColorStyle(Math.floor(r), Math.floor(g), Math.floor(b));
    }
    
    function Color(min) {
      min = min || 0;
      this.r = colorValue(min);
      this.g = colorValue(min);
      this.b = colorValue(min);
      this.style = createColorStyle(this.r, this.g, this.b);
    }
    function Dot(){
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.vx = -.5 + Math.random();
      this.vy = -.5 + Math.random();
      this.radius = Math.random() * 2;
      this.color = new Color();
    }
    Dot.prototype = {
      draw: function() {
        ctx.beginPath();
        ctx.fillStyle = this.color.style;
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fill();
      }
    };
    function createDots(){
      for(i = 0; i < dots.nb; i++) {
        dots.array.push(new Dot());
      }
    }
    function moveDots() {
      for(i = 0; i < dots.nb; i++) {
        var dot = dots.array[i];
        if(dot.y < 0 || dot.y > canvas.height) {
          dot.vx = dot.vx;
          dot.vy = - dot.vy;
        }
        else if(dot.x < 0 || dot.x > canvas.width) {
          dot.vx = - dot.vx;
          dot.vy = dot.vy;
        }
        dot.x += dot.vx;
        dot.y += dot.vy;
      }
    }
    function connectDots() {
      for(i = 0; i < dots.nb; i++) {
        for(j = 0; j < dots.nb; j++) {
          i_dot = dots.array[i];
          j_dot = dots.array[j];
          if((i_dot.x - j_dot.x) < dots.distance && (i_dot.y - j_dot.y) < dots.distance && (i_dot.x - j_dot.x) > - dots.distance && (i_dot.y - j_dot.y) > - dots.distance){
            if((i_dot.x - mousePosition.x) < dots.d_radius && (i_dot.y - mousePosition.y) < dots.d_radius && (i_dot.x - mousePosition.x) > - dots.d_radius && (i_dot.y - mousePosition.y) > - dots.d_radius){
              ctx.beginPath();
              ctx.strokeStyle = averageColorStyles(i_dot, j_dot);
              ctx.moveTo(i_dot.x, i_dot.y);
              ctx.lineTo(j_dot.x, j_dot.y);
              ctx.stroke();
              ctx.closePath();
            }
          }
        }
      }
    }
    function drawDots() {
      for(i = 0; i < dots.nb; i++) {
        var dot = dots.array[i];
        dot.draw();
      }
    }
    function animateDots() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      moveDots();
      connectDots();
      drawDots();
      requestAnimationFrame(animateDots); 
    }
    canvas.onmousemove = function(e) {
      mousePosition.x = e.pageX;
      mousePosition.y = e.pageY;
    };
    canvas.onmouseleave = function(e) {
      mousePosition.x = canvas.width / 2;
      mousePosition.y = canvas.height / 2;
    };
    createDots();
    requestAnimationFrame(animateDots); 
  }
  export default {
    data () {
      return {
        account: '',
        password: '',
        remember: [],
        loading: false
      }
    },
    methods: {
      ...mapActions(['login']),
      saveAccount () {
        this.remember.length && storage.setItem(STORAGE_KEY.ACCOUNT, this.account)
      },
      getAccount () {
        this.account = storage.getItem(STORAGE_KEY.ACCOUNT) || ''
      },
      check () {
        if (!this.account) {
          return this.n3Alert({
            content: '请输入账号',
            type: 'success',
            placement: 'top-right',
            duration: 2000,
            width: '240px'
          })
        }
        if (!this.password) {
          return this.n3Alert({
            content: '请输入密码',
            type: 'success',
            placement: 'top-right',
            duration: 2000,
            width: '240px'
          })
        }
        this.saveAccount()
        this.submit()
      },
      submit () {
        this.loading = true
        this.login({
          account: this.account,
          password: this.password
        })
          .then(data => {
            this.loading = false
            if (this.$route.query.back) {
               this.$router.replace(this.$route.query.back)
            } else {
              this.$router.replace('/form')
            }
          })
          .catch(error => {
            this.loading = false
            this.n3Alert({
              content: error || '登录失败，请检查账号密码~',
              type: 'success',
              placement: 'top-right',
              duration: 2000,
              width: '240px'
            })
          })
      },
      render: render
    },
    watch: {
      '$route' () {
        if (this.$route.name == 'login') {
          this.render()
        }
      }
    },
    created () {
      this.getAccount()
    },
    mounted () {
      this.render()
    }
  }
</script>

<style lang="less">
  .login-wrap {
    position: fixed;
    z-index: 0;
    top: 0;
    left: 0;
    overflow: hidden;
    width: 100%;
    height: 100%;
    background: #111;
    canvas {
      width: 100%;
      height: 100%;
      position: absolute;
    }
  }
  .login-form {
    position: absolute;
    z-index: 1;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    padding: 16px 20px 0;
    width: 360px;
    height: 252px;
    font-size: 14px;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 12px;
    box-shadow: 2px 2px 32px 1px rgba(0, 0, 0, .45);
    opacity: .75;
    h3 {
      margin-top: 0;
      margin-bottom: 0;
      padding: 12px 0;
      font-weight: normal;
      font-size: 22px;
      text-align: center;
    }
    .field {
      display: block;
      margin: 0 auto;
      padding: 6px 0;
    }
    .submit {
      padding: 12px 0;
    }
  }
</style>