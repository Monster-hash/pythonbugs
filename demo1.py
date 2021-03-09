class LianJiaSpider():

    # 初始化方法
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{0}/'  # 初始化请求url

        # 用于将爬虫程序伪装成浏览器（对付反爬）
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    # 发送请求的方法
    def __send_request(self):
        pass

    # 解析HTML获取有用数据
    def parse_content(self):
        pass

    # 写入数据库
    def write_mysql(self):
        pass

    # 启动爬虫程序
    def start(self):
        for i in range(1, 11): # 产生一个1到10的之间的整数序列
            full_url = self.url.format(i)
            print(full_url)
        # print("已启动爬虫")

if __name__ == '__main__':
    # 创建类的对象，并调用start()方法
    lianjia = LianJiaSpider()
    lianjia.start()