# -*- coding: utf-8 -*-
import scrapy


class TalksSpider(scrapy.Spider):
    name = 'talks'
    allowed_domains = ['www.ted.com']
    start_urls = ['https://www.ted.com/talks?page=1']

    def parse(self, response):
        container = response.css('div.container.results')
        talks = container.css('div.talk-link')

        for talk in talks:
        	title_link = talk.css('h4 a.ga-link')
        	meta = talk.css('span.meta__val')

        	speaker = talk.css('h4.talk-link__speaker::text').extract_first()
        	title = title_link.css('::text').extract_first().strip()
        	link = response.urljoin(title_link.css('::attr(href)').extract_first())
        	date = meta[0].css('::text').extract_first().strip()

        	if len(meta) > 1:
        		tags = meta[1].css('::text').extract_first().strip().split(', ')
        	else:
        		tags = []

        	yield {
        		'speaker': speaker,
        		'title': title,
        		'link': link,
        		'date': date,
        		'tags': tags,
        	}

        next_link = container.css('a.pagination__next::attr(href)').extract_first()
        if next_link:
        	yield response.follow(next_link, callback=self.parse)