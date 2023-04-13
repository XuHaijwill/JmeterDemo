# Jmeter使用指南

[下载地址](https://dlcdn.apache.org//jmeter/binaries/)

# Jms test
[JMeter JMS Point-to-Point Sampler with ActiveMQ](https://stackoverflow.com/questions/59733419/jmeter-jms-point-to-point-sampler-with-activemq)

https://www.blazemeter.com/blog/jmeter-load-testing

[Jmeter 教程](https://www.tutorialspoint.com/jmeter/jmeter_jms_pointtopoint_test_plan.htm)

# Docker安装ActiveMQ
- 查询Docker镜像
```
docker search activemq
```
- 下载Docker镜像
```
docker pull webcenter/activemq
```
- 创建&运行ActiveMQ容器
```
docker run -d --name myactivemq -p 61616:61616 -p 8161:8161 webcenter/activemq
```
- 查看WEB管理页面：
  浏览器输入`http://192.168.0.109:8161/`，点击`Manage ActiveMQ broker`使用默认账号/密码：`admin`/`admin`进入查看

# ActiveMQ - Java
https://juejin.cn/post/6844904057652379661

# Jmeter对RabbitMQ压力测试
https://blog.51cto.com/fengwan/5184502

# 启动测试
```
./jmeter.bat -n -t E:\sources\git\github\JmeterDemo\src\Jms_test_thread_group.jmx -l E:\sources\git\github\JmeterDemo\tmp\activemq.jtl -j E:\sources\git\github\JmeterDemo\tmp\activemq.jmx.log -e -o E:\sources\git\github\JmeterDemo\tmp\result

https://youle.zhipin.com/articles/f1f5d04c13c47074qxB72Ny6FQ~~.html
-e: 在脚本运行结束后生成html报告
-o: 保存html报告路径，此文件夹必须为空或者不存在
```
# ActiveMQ java demo

E:\sources\git\github\javaCodeGuid\javaBase\src\main\java\org\example\jms\JmsConsumer.java

# Refer 

- [JMeter 中_time 函数的使用（时间戳、当前时间）](https://blog.csdn.net/DreamTL/article/details/68957447)
- [Jms point to point sampler](https://sqa.stackexchange.com/questions/37215/i-got-an-issue-with-jms-point-to-point-sampler)
- [Concurrency Thread Group的介绍](https://www.cnblogs.com/poloyy/p/12845465.html)
- [Jmeter 学习路线](https://www.cnblogs.com/poloyy/p/15257716.html)
- [Jmeter模拟RocketMQ生产者消息发送](https://blog.csdn.net/C343500263/article/details/120532664)

# 性能测试

- https://bbs.itheima.com/thread-405757-1-1.html
- https://www.bilibili.com/video/BV1ty4y1q72g/?p=2&spm_id_from=pageDriver&vd_source=c102ec68c51d3f8673e6ec1b0c5f195b
- https://www.bilibili.com/video/BV1wC4y1Y7yX/?vd_source=c102ec68c51d3f8673e6ec1b0c5f195b

- [学习网址](https://www.bilibili.com/video/BV1st411Y7QW?p=71&vd_source=c102ec68c51d3f8673e6ec1b0c5f195b)

- [User's Manual](https://jmeter.apache.org/usermanual/index.html#index)

- https://jmeter.apache.org/usermanual/get-started.html#non_gui

![image-20230409214900348](docs\imgs\image-20230409214900348.png)

## Jmeter报告查看

![image-20230409220216568](docs\imgs\image-20230409220216568.png)

![image-20230409220359257](docs\imgs\image-20230409220359257.png)

JMeter聚合报告中响应时间的单位是毫秒（ms）

## 性能测试课程总体目标

1. 什么是性能

   - 时间

   - 资源

2. 性能测试

3. 什么是基准测试

4. 基准测试的用途

5. 稳定性测试：

   - 在服务器稳定运行（用户正常的业务负载下）的情况下进行长时间测试（1天-1周等），并最终保证服务器能满足线上的业务需求
   - 系统在用户要求的业务负载下运行达到规定的时间时，西永才能正式上线使用

   ![image-20230410084727853](docs\imgs\image-20230410084727853.png)

![image-20230410084750973](docs\imgs\image-20230410084750973.png)

6. 压力测试

   - 在请负载下的测试，查看系统在峰值的情况下是否功能隐患、系统是否具有良好的容错能力和客恢复能力

   - 测试场景：

     ```
     极限负载情况下的破坏性压力测试
     高负载下的长时间的稳定性压力测试
     第一种：极限负载情况下的破坏性压力测试（C-D区间）
     第二种：高负载下的长时间稳定性压力测试（B-C区间）
     ```

7. 并发测试：
   - 并发测试（绝对并发）：是指在极端的时间内，发送多个请求，来验证服务器对并发的处理能力
   - 应用场景：如抢红包，秒杀，抢购等

## 性能测试指标

定义：从客户端发送请求，到客户端收到服务器响应的总时间

组成：网络传输时间+服务器处理时间

![image-20230410085407540](docs\imgs\image-20230410085407540.png)

### 吞吐量

1. 什么是吞吐量

   ```
   指的是单位时间内处理的客户端请求数量。直接体现软件系统的性能承载能力
   ```

2. 吞吐量的单位有哪些

   ```
   从业务角度： 业务数/天、访问人数/天、页面访问量/天
   从网络角度： 字节数/小时、字节数/天
   从技术指标： 每秒查询数（QPS）、每秒事务数（TPS）
   ```

3. QPS和TPS有什么关系

   ```
   事务，即业务。一个事务可以对应一个请求，多个请求
   一个事务对应一个请求时： TPS = QPS
   一个事务对应n个请求时： QPS = n * TPS
   ```

### 点击数

### 错误率

```
指系统在负载情况下，失败的业务概率
注意：
	错误率是性能指标，是高负载下的失败业务的概率
	随机bug是功能bug，先解决随机bug才能进行性能测试
```

### 资源利用率

![image-20230410091454647](docs\imgs\image-20230410091454647.png)

## 性能测试的流程

![image-20230410091657796](docs\imgs\image-20230410091657796.png)

### 需求分析

![image-20230410091633281](docs\imgs\image-20230410091633281.png)

### 性能测试计划

- 测试的目的和范围 

- 测试人员和分工 

- 测试时间安排 

- 测试的方法

### 性能测试用例

![image-20230410085522309](docs\imgs\image-20230410085522309.png)

## 性能测试工具

- Loadrunner
- Jmeter

![image-20230410090547759](docs\imgs\image-20230410090547759.png)

#  Jmeter

## Jmeter语言修改

![image-20230410092207564](docs\imgs\image-20230410092207564.png)

永久修改：jmeter.propertie -> #language=en

## 元件执行顺序：

同一作用域下的不同元件：

配置元件 - 前置处理程序 - 定时器 - 取样器 - 后置处理程序 - 断言 - 监听器

同一作用域下相同元件： 从上到下的顺序依次执行

![image-20230410093958326](docs\imgs\image-20230410093958326.png)

## 线程参数说明

![image-20230410094059523](docs\imgs\image-20230410094059523.png)

Ramp-Up: 多长时间用户全部启动

循环次数 若选择永远： 一般和调度器配置配合使用： 持续时间 - 脚本持续运行时间 启动延迟 - 脚本等多久开始执行

控制线程组运行顺序（并发或者执行完下一个）

![image-20230410094441098](docs\imgs\image-20230410094441098.png)

## HTTP请求：

```
参数介绍：
作用：向服务器发送http及https请求
参数：
```

![image-20230410095930907](docs\imgs\image-20230410095930907.png)

## Jmeter乱码

sampleresult.default.encoding=utf-8

## Jmeter断言

```
定义：检查实际的返回结果是否与预期结果保持一致
	自动校验机制：自动判断响应状态码（2xx：成功，4xx/5xx：失败）
Jmeter断言：
	响应断言：对任意格式的响应数据进行断言
	json断言：对json格式的响应数据进行断言
	持续时间断言：对响应时间进行断言
```

### 响应断言

![image-20230411220758865](docs\imgs\image-20230411220758865.png)

![image-20230411220818057](docs\imgs\image-20230411220818057.png)

![image-20230411221002544](docs\imgs\image-20230411221002544.png)

### JSON断言

![image-20230411221154304](docs\imgs\image-20230411221154304.png)

![image-20230411221243794](docs\imgs\image-20230411221243794.png)

### 断言持续时间

![image-20230411221426776](docs\imgs\image-20230411221426776.png)

## Jmeter关联

```
定义：请求之间有依赖关系，一个请求的响应数据作为另一个的请求参数来传递
JMeter关联：
正则表达式提取器：提取任意格式的响应数据
Xpath提取器：提取HTML格式的响应数据
JSON提取器： 提取JSON格式的响应数据
```

### 正则表达式介绍

正则表达式：就是一个公式，或者说一套规则，使用这套规则可以从任意字符串中提取出想要的数据内容

```
公式格式：左边界(匹配符号)右边界：可以提取出想要获取的数据内容
.：是通配符，可以代表任意字符（除换行回车）
*: 代表前面的字符出现0次或者多次
.*匹配规则：找到左边界值后，往右查找有边界，找到最后面的右边界，中间的所有数据都被记录下来
?: 代表非贪婪匹配，找到左边界后，往右查找匹配右边界，只要有匹配的右边界就停止继续查找；再次查找
左边界和右边界
公式格式：左边界(.*?)右边界
<title>百度一下，你就知道</title><title>百度一下，你就知道</title>
<title>(.*?)</title>
```

- http://tools.haokh.net/Regex
- https://www.bejson.com/othertools/regex/

```
原始文本：
021-1234-1234
022-1234-1235
023-1234-1236
024-1234-1237
025-1234-1238
026-1234-1239
027-1234-1230
要求：匹配出 城市号、地区号、个人号码三组
```

```
正则表达式匹配：
(.*?)-(.*?)-(.*?)\n
结论：
通过一个正则表达式可以提取出多组数据，每组数据设置对应的左边界和右边界即可
每一组数据都可以有一个或者多个值
```

### 正则表达式提取器

![image-20230411222557953](docs\imgs\image-20230411222557953.png)

![image-20230411222748103](docs\imgs\image-20230411222748103.png)

![image-20230411223412208](docs\imgs\image-20230411223412208.png)

![image-20230411223452266](docs\imgs\image-20230411223452266.png)



### xpath提取器

```
案例：
//a : 找出所有的a标签
//a[@id='kw']： 在HTML页面中，找出a标签（有一个属性为id，且id的值为kw）
//b[@name='kw']： 在HTML页面中，找出b标签（有一个属性为name，且name的值为kw）
案例2：获取itcast中的title标签，
使用：//title
```

![image-20230412093027677](docs\imgs\image-20230412093027677.png)

### json提取器

![image-20230412093422926](docs\imgs\image-20230412093422926.png)

### JMeter属性

![image-20230412093557582](docs\imgs\image-20230412093557582.png)

![image-20230412093621019](docs\imgs\image-20230412093621019.png)

## 自动录制脚本

### 原理：

![image-20230412094452222](docs\imgs\image-20230412094452222.png)

### jmeter脚本录制

```
1.添加HTTP代理服务器，并进行配置
•加HTTP代理服务器：测试计划(右键)->非测试元件->HTTP代理服务器
•配置代理服务器的参数
```

![image-20230412095345054](docs\imgs\image-20230412095345054.png)

![image-20230412095412015](docs\imgs\image-20230412095412015.png)

2.开启windows操作系统的浏览器代理

![image-20230412095506153](docs\imgs\image-20230412095506153.png)

3. 启动代理服务器，开始录制

![image-20230412095534843](docs\imgs\image-20230412095534843.png)

4. 在浏览器页面中进行操作，成功后，就能在JMeter当中看到抓取到的接口请求了。

![image-20230412095625759](docs\imgs\image-20230412095625759.png)

```
练习：
设置过滤规则，录制tpshop的登录脚本，运行脚本观察测试结果
```

```
当使用代理的过程中，发现抓不到包，几个可能的情况：
过滤规则设置有问题
重启Jmeter代理服务器或者重启Jmeter
换浏览器来使用（Chrome、IE）
检查PC机中的代理设置是否处于可用状态
拔掉网线，抓包
```

## Jmeter直连数据库

```
步骤：
•添加MySQL驱动jar包
-方式一：在测试计划面板点击“浏览…“按钮，将你的JDBC驱动添加进来
-方式二：将MySQL驱动jar包放入到lib/ext目录下，重启JMete

```

![image-20230412095957230](docs\imgs\image-20230412095957230.png)

### 配置数据库连接信息

-添加方式：测试计划 --> 线程组--> (右键添加) 配置元件 --> JDBC Connection Configuration

![image-20230412100144019](docs\imgs\image-20230412100144019.png)

![image-20230412100207841](docs\imgs\image-20230412100207841.png)

操作： 02_直连数据库-搜索案例断言.jmx ...TODO

## 逻辑控制器

### 如果（if）控制器

![image-20230412100941320](docs\imgs\image-20230412100941320.png)

```
1、使用‘用户定义的变量’定义一个变量name，name的值可以是baidu或itcast
2、根据name的变量值实现对应网站的访
```

## 定时器

### 同步定时器

![image-20230412102329523](docs\imgs\image-20230412102329523.png)

```
1、模拟100个用户同时访问百度首页，统计各种高并发情况下运行情况
```

```
使用同步定时器的操作步骤？
1.添加线程组，设置线程数为n
2.添加HTTP请求
3.添加同步定时器
•设置并发线程数：同时发送请求的虚拟用户数
•设置超时时间：
Ø建议设置：不设置的话，若没有达到设置的线程数会一直死等
Ø不能设置太小：等待时间后还没达到设置的线程数，会释放已到达的线程
4.添加查看结果树
5.添加监听器-聚合报告
```

### 常数吞吐量定时器

```
案例：
（1）一个用户以 20QPS (20 次/s) 的频率访问百度首页，持续一段时间，统计运行情况
案例：1、模拟100个用户同时访问百度首页，统计各种高并发情况下运行情况
（2）2个用户针对 （服务器的QPS要求：20QPS (20 次/s)） 的频率访问百度首页，持续一段时间，统
```

![image-20230412102728254](docs\imgs\image-20230412102728254.png)

### 固定定时器

```
案例：
（1）IHRM系统登录错误3次后，锁定1分钟，等待1分钟后重新输入正确的用户名密码登录成功
请求方法：POST
请求URL：http://ihrm-test.itheima.net/api/sys/login
请求头：Content-Type: application/json;charset=UTF-8
请求体：{"mobile":"13800000002","password":"123456"}
步骤：
添加线程组
添加HTTP请求1 - 错误1次
添加HTTP请求2 - 错误2次
添加HTTP请求3 - 错误3次
添加HTTP请求4 - 正确用户名密码
在HTTP请求4下，添加固定定时器
添加查看结果树
```

![image-20230412102833981](docs\imgs\image-20230412102833981.png)

## jmeter分布式

```
应用场景：
当单个测试机无法模拟用户要求的业务场景时，可以使用多台测试机进行模拟，就是Jmeter的分布式测试
```

![image-20230413083339789](docs\imgs\image-20230413083339789.png)

```
分布式相关注意事项：
关闭防火墙
所有的控制机、代理机、服务器都在同一个网络上
所有机器的Jmeter和JAVA版本必须一致
关闭RMI SSL开关
```

![image-20230413083426655](docs\imgs\image-20230413083426655.png)

![image-20230413083501426](docs\imgs\image-20230413083501426.png)

## jmeter报告

### 聚合报告

![image-20230413083631418](docs\imgs\image-20230413083631418.png)

```
补充：
正常情况下，响应时间的结果取平均值
当响应时间最大值特别高（超出平均水平特别多），导致平均值不能代表正常/大部分水平时，可
以使用百分比时间
```

```
案例：
1、请求：https://www.baidu.com
2、模拟5个用户并发，控制服务器QPS为20，运行时长设置为10分钟
3、添加聚合报告，收集系统性能指标：响应时间、吞吐量、错误率、网路速率
```

![image-20230413083824835](docs\imgs\image-20230413083824835.png)

### HMTL报告

![image-20230413083909342](docs\imgs\image-20230413083909342.png)

![image-20230413083936672](docs\imgs\image-20230413083936672.png)

## 并发数计算

### 普通方法

```
并发tps = 总请求数/总时间
只能满足最基本的要求，但是不能很好覆盖系统正常的使用情况
```

### 二八原则

```
并发tps = 总请求数 * 80% / 总时间 * 20%
满足系统绝大多数情况下的应用场景的需要
```

### 根据业务运营数据的统计计算（通常用来做稳定性测试）

```
并发TPS = 有效请求数 * 80% / 有效时间 * 20%
当运营数据统计越精确时，计算出的并发TPS与实际的越接近
```

### 根据用户峰值业务操作来计算（通常用来做压力测试）

```
并发TPS = 峰值请求数 / 峰值时间 * 系数
满足峰值请求时间段内的负载量，系数取决于项目组对于未来业务量的评估
```

```
某购物商城，经过运营统计，正常一天成交额为100亿，客单价平均为300元，交易时间主要为10:00-
14:00，17:00-24:00，其中19:00—20:00的成交量最大，大约成交20亿。
现升级系统，需要进行性能测试，保证软件在上线后能稳定运行。
请计算出系统稳定性测试时的并发（负载）量，及保证系统峰值业务时的并发（负载）量
稳定性并发量：
并发TPS = 有效请求数 * 80% / 有效时间 * 20%
并发TPS = （100E/300 * 80%） / (3600 * 11 * 20%)
压力并发量：
并发TPS = 峰值请求数 / 峰值时间 * 系数
压力TPS = (20E/300) / (3600 * 1) * 系数
```

## 插件安装

```
（1）安装插件管理器
在Jmeter官网上下载插件管理器Plugins-manager-1.3.jar
将JAR包放入到lib\ext目录下
重启Jmeter，可以在选项下看到Plugins Manager选项
```

![image-20230413084604188](docs\imgs\image-20230413084604188.png)

```
安装指定的插件
打开Plugins Manager插件管理器
选择Available Plugins，当前可用的插件
选择需要下载的插件（等待右方文本内容展示出来）
下载右下角的下载按钮，自动的完成下载，Jmeter会自动重启
```

![image-20230413084940508](docs\imgs\image-20230413084940508.png)

![image-20230413085020764](docs\imgs\image-20230413085020764.png)

## 并发数及Jmeter性能测试常用图表

### Concurrency Thread Group线程组

```
性能测试常用图表：
Concurrency Thread Group线程组：
作用：
线程数阶梯上升
图形化的展示
添加方式：测试计划 --> 线程（用户）--> Concurrency Thread Group

```

![image-20230413085133566](docs\imgs\image-20230413085133566.png)

每秒性能指标统计：

![image-20230413085205225](docs\imgs\image-20230413085205225.png)

```
作用：
•性能测试的结果统计，以聚合报告的结果为准
每秒性能指标的作用是：查看系统长时间运行过程中是否有异常出现，有则进一步分析
```

## 基于jmeter客户端监控服务器 硬件资源

![image-20230413085317806](docs\imgs\image-20230413085317806.png)

```
监控性能指标的步骤（windows服务器）：
下载ServerAgent程序，并上传到服务器上
手动启动ServerAgent程序，windows服务器startAgent.bat，linux服务器startAgent.sh
在Jmeter中添加PerfMon监控组件，并配置
```

![image-20230413085501659](docs\imgs\image-20230413085501659.png)

添加线程组及HTTP请求脚本，并配置，运行即可监控资源指标

### 监控性能指标的步骤（linux服务器）

```
监控性能指标的步骤（linux服务器）：
下载ServerAgent程序，并上传到服务器上
通过finalshell工具上传到指定的目录下
手动启动ServerAgent程序，windows服务器startAgent.bat，linux服务器startAgent.sh
```

### 添加HTTP请求 - 请求litemall首页

![image-20230413085823084](docs\imgs\image-20230413085823084.png)

### 在Jmeter中添加PerfMon监控组件，并配置

![image-20230413085917217](docs\imgs\image-20230413085917217.png)

# 案例分析

## 使用1个线程组，添加HTTP请求（百度） 配置线程数为2，循环次数为3时，运行观察结果 

​          配置线程数为3，循环次数为2时，运行观察结果，对比是否有不同 

相同点：从请求数量来说，是完全相同的 

不同点：场景不同 线程数：代表用户数，即性能测试时的负载量（线程数为2比线程数为3对应的负载量小）

 循环次数：代表时间，即性能测试时的运行时间（循环次数3比循环次数2对应的时间长）

## 某支付系统，需要用1000个不同的用户登录，并使用添加不同的测试金额数据访问支付接口？

```
答案：
添加线程组
添加配置元件 - CSV数据文件设置，读取CSV文件数据中的用户名密码
添加HTTP请求 - 登录，引用CSV数据文件设置中的变量
添加HTTP请求 - 支付，使用counter函数传入不同金额的测试数据
添加查看结果树
```

# FAQ

## Jmeter右上角不显示线程数和运行时间
https://www.cnblogs.com/LucasMeng/p/17208063.html

在GUI界面去修改的语言这样就会出现这样的bug

## Cannot instantiate class: org.apache.activemq.jndi.ActiveMQInitialContextFactory [Root exception is java.lang.ClassNotFoundException: org.apache.activemq.jndi.ActiveMQInitialContextFactory
https://activemq.apache.org/jndi-support.html

add activemq-all.jar dependency to /lib/ext folder of the JMeter,

https://stackoverflow.com/questions/41600180/cannot-instantiate-class-org-apache-activemq-jndi-activemqinitialcontextfactory