<template>
<transition name="slide">
	<div>
    <div style="background-color:#fff">
    <br><br>
        <div :class="className" :id="id" :style="{height:height,width:width}"></div>
    </div>
	<div style="background-color: #fff">
	<div id="myChart3" :style="{width: '1050px', height: '300px'}"></div>
	</div>

<br>


	</div>
</transition>
	
</template>

<script type="text/javascript">
let echarts = require('echarts/lib/echarts')
// 引入柱状图组件
require('echarts/lib/chart/bar')
// 引入提示框和title组件
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')

import { mapState,mapGetters } from 'vuex'
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
  data () {
    return {
    	chart: null,
      msg: 'Welcome to Your Vue.js App',
      data: [["2000-06-05",116],["2000-06-06",129],["2000-06-07",135],["2000-06-08",86],["2000-06-09",73],["2000-06-10",85],["2000-06-11",73],["2000-06-12",68],["2000-06-13",92],["2000-06-14",130],["2000-06-15",245],["2000-06-16",139],["2000-06-17",115],["2000-06-18",111],["2000-06-19",309],["2000-06-20",206],["2000-06-21",137],["2000-06-22",128],["2000-06-23",85],["2000-06-24",94],["2000-06-25",71],["2000-06-26",106],["2000-06-27",84],["2000-06-28",93],["2000-06-29",85],["2000-06-30",73],["2000-07-01",83],["2000-07-02",125],["2000-07-03",107],["2000-07-04",82],["2000-07-05",44],["2000-07-06",72],["2000-07-07",106],["2000-07-08",107],["2000-07-09",66],["2000-07-10",91],["2000-07-11",92],["2000-07-12",113],["2000-07-13",107],["2000-07-14",131],["2000-07-15",111],["2000-07-16",64],["2000-07-17",69],["2000-07-18",88],["2000-07-19",77],["2000-07-20",83],["2000-07-21",111],["2000-07-22",57],["2000-07-23",55],["2000-07-24",60],["2000-07-25",44],["2000-07-26",127],["2000-07-27",114],["2000-07-28",86],["2000-07-29",73],["2000-07-30",52],["2000-07-31",69],["2000-08-01",86],["2000-08-02",118],["2000-08-03",56],["2000-08-04",91],["2000-08-05",121],["2000-08-06",127],["2000-08-07",78],["2000-08-08",79],["2000-08-09",46],["2000-08-10",108],["2000-08-11",80],["2000-08-12",79],["2000-08-13",69],["2000-08-14",80],["2000-08-15",105],["2000-08-16",119],["2000-08-17",105],["2000-08-18",55],["2000-08-19",74],["2000-08-20",41],["2000-08-21",62],["2000-08-22",104],["2000-08-23",118],["2000-08-24",121],["2000-08-25",126],["2000-08-26",99],["2000-08-27",92],["2000-08-28",75],["2000-08-29",91],["2000-08-30",94],["2000-08-31",69],["2000-09-01",93],["2000-09-02",124],["2000-09-03",120],["2000-09-04",93],["2000-09-05",26],["2000-09-06",32],["2000-09-07",70],["2000-09-08",89],["2000-09-10",117],["2000-09-11",144],["2000-09-12",111],["2000-09-13",120],["2000-09-14",97],["2000-09-15",108],["2000-09-17",74],["2000-09-18",105],["2000-09-19",127],["2000-09-20",143],["2000-09-21",62],["2000-09-22",80],["2000-09-23",136],["2000-09-24",29],["2000-09-25",91],["2000-09-26",93],["2000-09-27",114],["2000-09-28",45],["2000-09-29",102],["2000-09-30",111],["2000-10-01",93],["2000-10-02",117],["2000-10-03",78],["2000-10-04",76],["2000-10-05",100],["2000-10-06",75],["2000-10-07",169]]
    }
  },
	computed: {
		...mapGetters([
			'doneTodos'
			])
	},
  mounted(){
    // this.drawLine();
    // this.drawLine2();
    this.drawLine3();
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
    },
    drawLine(){
        // 基于准备好的dom，初始化echarts实例
        let myChart1 = this.$echarts.init(document.getElementById('myChart1'))
        // 绘制图表
        myChart1.setOption({
            title: { text: 'Daocloud !' },
            tooltip: {},
            xAxis: {
                data: ["DCS","羊毛衫","DCE","裤子","DevOps","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        });
    },
    drawLine2(){
    	let myChart2 = this.$echarts.init(document.getElementById('myChart2'))

    	myChart2.setOption({
		    series : [
		        {
		            name: '访问来源',
		            type: 'pie',
		            radius: '55%',
		            data:[
		                {value:235, name:'USA'},
		                {value:274, name:'上海'},
		                {value:310, name:'武汉'},
		                {value:335, name:'深圳'},
		                {value:400, name:'北京'}
		            ]
		        }
		    ]
		})
    },
    drawLine3(){
    	let myChart3 = this.$echarts.init(document.getElementById('myChart3'))

		myChart3.setOption({



		        title: {
		            text: ''
		        },
		        tooltip: {
		            trigger: 'axis'
		        },
		        xAxis: {
		            data: this.data.map(function (item) {
		                return item[0];
		            })
		        },
		        yAxis: {
		            splitLine: {
		                show: false
		            }
		        },
		        toolbox: {
		            left: 'center',
		            feature: {
		                dataZoom: {
		                    yAxisIndex: 'none'
		                },
		                restore: {},
		                saveAsImage: {}
		            }
		        },
		        dataZoom: [{
		            startValue: '2014-06-01'
		        }, {
		            type: 'inside'
		        }],
		        visualMap: {
		            top: 10,
		            right: 10,
		            pieces: [{
		                gt: 0,
		                lte: 50,
		                color: '#096'
		            }, {
		                gt: 50,
		                lte: 100,
		                color: '#ffde33'
		            }, {
		                gt: 100,
		                lte: 150,
		                color: '#ff9933'
		            }, {
		                gt: 150,
		                lte: 200,
		                color: '#cc0033'
		            }, {
		                gt: 200,
		                lte: 300,
		                color: '#660099'
		            }, {
		                gt: 300,
		                color: '#7e0023'
		            }],
		            outOfRange: {
		                color: '#999'
		            }
		        },
		        series: {
		            name: 'Beijing AQI',
		            type: 'line',
		            data: this.data.map(function (item) {
		                return item[1];
		            }),
		            markLine: {
		                silent: true,
		                data: [{
		                    yAxis: 50
		                }, {
		                    yAxis: 100
		                }, {
		                    yAxis: 150
		                }, {
		                    yAxis: 200
		                }, {
		                    yAxis: 300
		                }]
		            }
		        }
		    });
		}
	}
}
</script>