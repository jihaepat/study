BOT_NAME = 'newscrawling'

SPIDER_MODULES = ['newscrawling.spiders']
NEWSPIDER_MODULE = 'newscrawling.spiders'
LOG_LEVEL = 'ERROR'
#
# Url 크롤링시 CSVPipeline 설정
ITEM_PIPELINES = {'newscrawling.pipelines.CsvPipeline': 300, }

# 기사 내용 크롤링시 MongoDBPipeline 설정
# ITEM_PIPELINES = {'newscrawling.pipelines.MongoDBPipeline': 300,}

# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "news_crawl"
# MONGODB_COLLECTION = "news"