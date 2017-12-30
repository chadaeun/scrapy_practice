# tutorial

## English

This project is following [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html) in [Scrapy documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html).

target website: [http://quotes.toscrape.com/]

directory structure: (skip automatically created files by 'startproject' command)

- tutorial
    - tutorial
        - spiders
            - author_spider.py: scrapes authors' name, birth date, and biography
            - quotes_spider.py: scrapes quotes' text, author, and tags
    - author.json: JSON file created by author_spider.py
    - quotes.jl: JSON Lines file created by quotes_spider.py
    - quotes.json: JSON file created by quotes_spider.py

You can scrape data using this project by running bellow commands:

- `scrapy crawl author -o author.json`: Runs author_spider.py
- `scrapy crawl quotes -o quotes.json`: Runs quotes_spider.py

## 한국어

이 프로젝트는 [Scrapy documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html)의 [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)을 따라 만든 프로젝트입니다.

대상 웹사이트: [http://quotes.toscrape.com/]

디렉터리 구조: ('startproject' 커맨드로 자동 생성된 파일은 생략하였습니다)

- tutorial
    - tutorial
        - spiders
            - author_spider.py: 작자의 이름, 태어난 날짜, 생애를 스크래핑
            - quotes_spider.py: 인용구의 텍스트, 작자, 태크를 스크래핑
    - author.json: author_spider.py로 생성된 JSON 파일
    - quotes.jl: quotes_spider.py로 생성된 JSON Lines 파일
    - quotes.json: quotes_spider.py로 생성된 JSON 파일

아래의 커맨드들을 실행함으로써 이 프로젝트를 통해 데이터를 스크래핑할 수 있습니다.

- `scrapy crawl author -o author.json`: author_spider.py 실행
- `scrapy crawl quotes -o quotes.json`: quotes_spider.py 실행