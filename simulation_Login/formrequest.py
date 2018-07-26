import scrapy


# 示例：
class WeixinSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        url = "https://github.com/session"
        data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": response.xpath('//*[@id="login"]/form/input[2]/@value').extract_first(),
            "login": "*****",
            "password": "******",
        }
        yield scrapy.FormRequest(url, formdata=data, callback=self.data)

    def data(self, response):
        with open('github02.html', 'wb') as f:
            f.write(response.body)