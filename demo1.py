import requests # 导入发送请求
from bs4 import BeautifulSoup # 用于解析数据
import mysql.connector # 用于连接数据库

import time
import random

class LianJiaSpider():

    #获取连接对象
    mydb = mysql.connector.connect(host='localhost',user='root',passwd='root',database='lianjia',auth_plugin='mysql_native_password')

    # 获取cursor对象
    mycursor = mydb.cursor()

    # 初始化方法
    def __init__(self):
        self.url = 'https://sh.lianjia.com/chengjiao/pg{0}/'  # 初始化请求url

        time.sleep(random.random() * 3) # 设置随机访问时间间隔

        # 用于将爬虫程序伪装成浏览器（对付反爬）
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    # 发送请求的方法
    def send_request(self,url):
        # 由于请求方式为get，所以使用requests方法中的get方法
        resp = requests.get(url,headers = self.headers)
        if resp.status_code == 200: # 如果响应状态码为200，将返回方法的调用处
            return resp

    # 解析HTML获取有用数据
    def parse_content(self,resp):
        list = [] # 空列表，用于保存数据
        html = resp.text # 获取响应的html
        bs = BeautifulSoup(html,'html.parser') # 第一个参数是要解析的内容，第二个参数是解析器

        # 查找名称为sellListContent的ul
        ul = bs.find('ul',class_='listContent')

        # 在ul中获取所有的li标签
        li_list = ul.find_all('li') # 1.获取数据数量 print(len(li_list)) # 2.是否获取到数据 print(li_list)

        # 遍历
        for item in li_list:
            title = item.find('div', class_='title').text  # 获取标题
            house_Info = item.find('div', class_='houseInfo').text  # 获取房屋描述
            deal_date = item.find('div', class_='dealDate').text  # 获取成交日期
            total_price = item.find('div', class_='totalPrice').text  # 获取总价
            position_info = item.find('div', class_='positionInfo').text  # 楼层信息
            unit_price = item.find('div', class_='unitPrice').text  # 单价
            span = item.find('span', class_='dealCycleTxt')  # 获取到span标签，有两个span标签
            span_list = span.find_all('span')  # 获取挂牌价 / 成交周期
            agent_name = item.find('a','agent_name') # 房产销售
            agent_namet = agent_name.text if agent_name!=None else '' # 判空输出空值
            list.append((title, house_Info, deal_date, total_price, position_info, unit_price, span_list[0].text,span_list[1].text, agent_namet))
            # print(title, house_Info, deal_date, total_price, position_info, unit_price, span_list[0].text,span_list[1].text, agent_name)

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


    # 启动爬虫程序
    def start(self):

        for i in range(1, 101): # 产生一个1到10的之间的整数序列
            full_url = self.url.format(i)
            # print(full_url)
            resp = self.send_request(full_url) # 发送请求，获取一个响应
            # print(resp.text)
            if resp:
                self.parse_content(resp) # 将相应结果传入，调用解析方法提取有用数据

if __name__ == '__main__':
    # 创建类的对象，并调用start()方法
    lianjia = LianJiaSpider()
    lianjia.start()

