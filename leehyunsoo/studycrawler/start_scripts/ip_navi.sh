#!/usr/bin/env bash

#현재 시간 + scrapy name 으로 파일생성

#touch ipnavi`date +%Y_%m_%d_%H:%M:%S`.json

scrapy crawl ipnavi -o ipnavi`date +%Y_%m_%d_%H:%M:%S`.json