import scrapy


# 示例：
class WeixinSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//*[@id="login"]/form',
            formdata={'login':'***', 'password': '***'},
            callback=self.data
        )

    def data(self, response):
        with open('github03.html', 'wb') as f:
            f.write(response.body)