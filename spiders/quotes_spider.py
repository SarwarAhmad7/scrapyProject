import scrapy
from ..items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://www.amazon.com/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1739779676&rnid=1250225011&ref=sr_nr_p_n_publication_date_0"
        ]

    def parse(self, response):

        books = response.css('.puisg-row')

        for book in books:
            items = TutorialItem()

            product_name = book.css('.a-color-base.a-text-normal span').css('::text').get()
            product_author = book.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').getall()
            product_price = book.css('.puis-price-instructions-style span ').css('::text').extract_first()
            product_imagelink = book.css('.s-image::attr(src)').get()

            items['product_name'] = product_name
            items['product_author'] = product_author
            items['product_price'] = product_price
            items['product_imagelink'] = product_imagelink

            yield items
            
















        
        # product_name = response.css('.a-color-base.a-text-normal span').css('::text').get()
        # product_author = response.css('.a-color-secondary .a-row .a-size-base+ .a-size-base').css('::text').getall()
        # product_price = response.css('.puis-price-instructions-style .a-price span span').css('::text').get()
        # product_imagelink = response.css('.s-image::attr(src)').get()

        # items['product_name'] = product_name
        # items['product_author'] = product_author
        # items['product_price'] = product_price
        # items['product_imagelink'] = product_imagelink

        # yield items