### 请求：浏览器的地址栏的url向服务器发送请求
​	请求的url

​	请求的方式method get/ post

​	请求参数

### 响应:作出响应

​	响应状态码：  200  418  404  500

浏览器的工作原理：发请求 --> 收响应 --> 解析 --> 显示

爬虫工作：模拟浏览器发送请求，收响应结果， --> 解析-->提取数据-->存储到数据库中.

### 爬取流程：

使用Python去编写代码，模拟浏览器去 工作..

1. 找到要爬取的url,发送请求

https://bj.lianjia.com/ershoufang/

2. 分析url是如何变化，提取有用的url

https://bj.lianjia.com/ershoufang/pg2/  -->pg2  页码2

3. 提取有用数据
4. 数据持久化  -->数据库中（以备后用）

python程序发送请求，需要使用第三方库，requests 在使用之前需要先安装 pip install requests

### 数据解析

数据解析,使用的是BeautifulSoup 库（Python3的选择bs4进行安装，Python2的选择beautifulSoup），pip install

> 注：区别requests.get（）与self.send_request（）
> requests.get（） requests库中的get 方法 ()
> self.send_request（） 手动编写的LianJiaSpider（）

### 提取数据

数据被包含在一个名为sellListContent的url中--> 获取url

### 存储数据

数据的存储-MySQL数据库

- 安装MySQL数据库

	- https://dev.mysql.com/downloads/mysql

  - 安装第三方库mysql-connector 
  - pip install mysql-connector

- 获取数据库连接

  - connect(host,user,passwd,database)
  - ALTER USER 'root @'localhost' IDENTIFIED WITH mysq! native_ password BY新密码';
  - mysql 8需要加一句`auth_plugin=mysql_native_password`

### 通过面向对象的方法要先搭建基础框架

```
# 使用面向对象的方式，搭建项目框架class LianJiaSpider():

    # 初始化方法    
    def __init__(self):
        pass    
    # 发送请求的方法    
    def send_request(self):
        pass    
    # 解析HTML获取有用数据    
    def parse_content(self):
        pass    
    # 写入数据库    
    def write_mysql(self):
        pass        
    # 启动爬虫程序    
    def start(self):
        print('启动成功')
        
if __name__ == '__main__':
    # 创建类的对象，调用start()方法    
    lianjia = LianJiaSpider()
    lianjia.start()
```

### 遍历输出
```
 # 遍历列表    
for item in li_list:       

    title = item.find('div', class_='title')       
    title_t = title.text if title!=None else ''      
    print('找标题')       
    house_info = item.find('div', class_='houseInfo')       
    house_it = house_info.text if house_info!=None else ''      
    print('房屋描述')       
    total_price = item.find('div', class_='totalPrice')       
    total_pt = total_price.text if total_price!=None else ''      
    print('总价')       
    position_info = item.find('div', class_='positionInfo')       	
    position_it = position_info.text if position_info!=None else ''    
    print('位置')       
    unit_price = item.find('div', class_='unitPrice')       
    unit_pt = unit_price.text if unit_price!=None else ''      
    print('单价') 
    
    lst.append((title_t, house_it, total_pt, position_it, unit_pt))     
    print('添加完成')     
    self.write_mysql(lst)     
    print('数据解析完毕，存储到数据库')
```

### 数据库建表
```
CREATE TABLE tbl_lianjia(
	id int(4) primary key auto_increment,
	title varchar(255),
	house_Info varchar(255),
	deal_date varchar(255),
	total_price varchar(255),
	position_info varchar(255),
	unit_price varchar(255),
	listing_price varchar(255),
	date varchar(255),
	agent_name varchar(255)
);
```

### 数据库连接部分

```
# 数据库解析完毕，需要存储到数据库中
    self.write_mysql(list)
# 写入数据库
def write_mysql(self,list):
    # print(self.mydb)
    sql = 'insert into tbl_lianjia (title,house_Info,deal_date,total_price,position_info,unit_price,listing_price,date,agent_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    # 执行批量插入
    self.mycursor.executemany(sql,list)

    #提交事务
    self.mydb.commit()
```

### 总结

发送请求：requests

解析使用：BeautifulSoup

数据库使用：mysql-connector
