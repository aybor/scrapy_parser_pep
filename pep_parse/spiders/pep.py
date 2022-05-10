import scrapy

from pep_parse.items import PepParseItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        all_peps = response.xpath('//*[@id="numerical-index"]//td[@class="num"]//a')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.xpath('//h1[@class="page-title"]/text()').get().split('–')
        number = int(number.replace('PEP', ''))
        name = name.strip()
        status = response.xpath(
            '//dl[@class="rfc2822 field-list simple"]'
            '/dt[contains(text(), "Status")]'
            '/following-sibling::dd[1]/text()'
        ).get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
