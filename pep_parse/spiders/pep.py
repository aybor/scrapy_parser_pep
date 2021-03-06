import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import PEP_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [f'{PEP_URL}']
    start_urls = [f'https://{PEP_URL}/']

    def parse(self, response):
        all_peps = response.xpath(
            '//*[@id="numerical-index"]//td[@class="num"]//a'
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        full_name = ''.join(
            response.xpath(
                '//h1[@class="page-title"]//text()'
            ).getall()
        )

        pattern = r'^PEP (?P<number>\d+) – .*$'
        number = int(re.search(
            pattern, full_name
        ).groups()[0].replace('PEP', ''))
        status = response.xpath(
            '//dl[@class="rfc2822 field-list simple"]'
            '/dt[contains(text(), "Status")]'
            '/following-sibling::dd[1]/text()'
        ).get()
        data = {
            'number': number,
            'name': full_name,
            'status': status,
        }
        yield PepParseItem(data)
