# ted

## English

target website: [https://www.ted.com/]

directory structure: (skip automatically created files by 'startproject' command)

- ted
    - ted
        - spiders
            - talks_spider.py: scrapes talks' speaker, title, link, date and rated information
    - talks.json: JSON file created by talks_spider.py

You can scrape data using this project by running bellow commands:

- `scrapy crawl talks -o talks.json`: Runs talks_spider.py

## 한국어

대상 웹사이트: [https://www.ted.com/]

디렉터리 구조: ('startproject' 커맨드로 자동 생성된 파일은 생략하였습니다)

- ted
    - ted
        - spiders
            - talks_spider.py: 강연의 강연자, 제목, 링크, 날짜, 평가 스크래핑
    - talks.json: talks_spider.py로 생성된 JSON 파일

아래의 커맨드들을 실행함으로써 이 프로젝트를 통해 데이터를 스크래핑할 수 있습니다.

- `scrapy crawl talks -o talks.json`: talks_spider.py 실행