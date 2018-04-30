#!/usr/bin/env bash#!/usr/bin/env bash

#현재 시간 + scrapy name 으로 파일생성

#touch 파일명`date +%Y_%m_%d_%H:%M:%S`.json

scrapy crawl baidu -o ipnavi`date +%Y_%m_%d_%H:%M:%S`.json