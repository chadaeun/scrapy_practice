import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = [
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/',
	]

	def parse(self, response):
		quotes = response.css('div.quote')
		for quote in quotes:
			yield {
				'text': quote.css('span.text::text').extract_first(),
				'author': quote.css('small.author::text').extract_first(),
				'tags': quote.css('div.tags a.tag::text').extract(),
			}

		for a in response.css('ul.pager li.next a'):
			yield response.follow(a, callback=self.parse)