import datetime as dt

from pep_parse.constants import DATETIME_FORMAT


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pep_parse.middlewares.PepParseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pep_parse.middlewares.PepParseDownloaderMiddleware': 543,
#}


# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
     f'../results/pep_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
     },
}
