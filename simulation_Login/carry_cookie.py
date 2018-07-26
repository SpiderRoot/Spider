import scrapy


# 示例：
class WeixinSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/SpiderRoot/AQI']

    def start_requests(self):
        cookies_str = '......'
        # 将cookie转成字典
        cookies_dic = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dic
        )

    def parse(self, response):
        with open('github.html', 'wb') as f:
            f.write(response.body)