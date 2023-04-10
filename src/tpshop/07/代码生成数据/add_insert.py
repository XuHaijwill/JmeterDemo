#导包
import pymysql
#创建连接
conn = pymysql.connect(host="192.168.91.137",user="litemall",password="litemall123456",database="litemall",port=3306,charset='utf8')
#创建游标
cursor = conn.cursor()
#添加地址的SQL语句
addr_sql = "INSERT INTO `litemall`.`litemall_address` (`id`, `name`, `user_id`, `province`, `city`, `county`, `address_detail`, `area_code`, `postal_code`, `tel`, `is_default`, `add_time`, `update_time`, `deleted`) VALUES ('{}', '{}', '{}', '北京市', '市辖区', '西城区', '天通苑', '110102', '', '{}', '1', '2020-08-12 14:17:23', '2020-08-12 14:17:23', '0');"
#循环插入数据
user_start = 100000
for i in range(100000):
    addr_id = user_start + i
    user_id = user_start + i
    username = "test" + str(user_id)
    mobile = "13012" + str(user_id)

    print("插入第{}条数据ID为{}".format(i+1,user_id))
    sql = addr_sql.format(addr_id,username,user_id,mobile)
    cursor.execute(sql)

    conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()