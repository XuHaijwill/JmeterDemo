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
```

# Refer 

- [JMeter 中_time 函数的使用（时间戳、当前时间）](https://blog.csdn.net/DreamTL/article/details/68957447)
- [Jms point to point sampler](https://sqa.stackexchange.com/questions/37215/i-got-an-issue-with-jms-point-to-point-sampler)
- [Concurrency Thread Group的介绍](https://www.cnblogs.com/poloyy/p/12845465.html)
- [Jmeter 学习路线](https://www.cnblogs.com/poloyy/p/15257716.html)

# FAQ
## Cannot instantiate class: org.apache.activemq.jndi.ActiveMQInitialContextFactory [Root exception is java.lang.ClassNotFoundException: org.apache.activemq.jndi.ActiveMQInitialContextFactory
https://activemq.apache.org/jndi-support.html

add activemq-all.jar dependency to /lib/ext folder of the JMeter,

https://stackoverflow.com/questions/41600180/cannot-instantiate-class-org-apache-activemq-jndi-activemqinitialcontextfactory