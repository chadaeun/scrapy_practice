import scrapy

class AuthorSpider(scrapy.Spider):
	name = 'author'
	start_urls = [
		'http://quotes.toscrape.com/page/1/',
	]

	def parse(self, response):
		authors = response.css('div.quote span a')
		for author in authors:
			yield response.follow(author, callback=self.parse_author)

		next_pages = response.css('ul.pager li.next a')
		for next_page in next_pages:
			yield response.follow(next_page, callback=self.parse)

	def parse_author(self, response):
		details = response.css('div.author-details')
		yield {
			'name': details.css('h3.author-title::text').extract_first().strip(),
			'birthdate': details.css('p span.author-born-date::text').extract_first(),
			'bio': details.css('div.author-description::text').extract_first().strip(),
		}