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

## 断言



# 案例

案例分析： 

（5）使用1个线程组，添加HTTP请求（百度） 配置线程数为2，循环次数为3时，运行观察结果 

​          配置线程数为3，循环次数为2时，运行观察结果，对比是否有不同 

相同点：从请求数量来说，是完全相同的 

不同点：场景不同 线程数：代表用户数，即性能测试时的负载量（线程数为2比线程数为3对应的负载量小）

 循环次数：代表时间，即性能测试时的运行时间（循环次数3比循环次数2对应的时间长）



# FAQ

## Jmeter右上角不显示线程数和运行时间
https://www.cnblogs.com/LucasMeng/p/17208063.html

在GUI界面去修改的语言这样就会出现这样的bug

## Cannot instantiate class: org.apache.activemq.jndi.ActiveMQInitialContextFactory [Root exception is java.lang.ClassNotFoundException: org.apache.activemq.jndi.ActiveMQInitialContextFactory
https://activemq.apache.org/jndi-support.html

add activemq-all.jar dependency to /lib/ext folder of the JMeter,

https://stackoverflow.com/questions/41600180/cannot-instantiate-class-org-apache-activemq-jndi-activemqinitialcontextfactory