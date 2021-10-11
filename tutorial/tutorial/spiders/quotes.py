import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/',
                    'https://quotes.toscrape.com/page/2/']

    def parse(self, response):
        page=response.url.split('/')[-2]
        filename='quotes-{}.txt'.format(page)
        with open(filename,'w') as f:

            quotes=response.css('.quote')
            for quote in quotes:
                content=quote.css('.text::text').extract()[0]
                author=quote.css('.author::text').extract()[0]
                print('quote:\n',content)
                print('author:\n',author)
                tags=quote.css('.tag::text').extract()
                print('tags:\n',tags)
                f.write('quote:\n{}\n author:{}\n tags:{}\n'.format(content,author,tags))
'''        page=response.url.split('/')[-2]
        filename='quotes-{}.html'.format(page)
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log("Saved file{}".format(filename))'''
