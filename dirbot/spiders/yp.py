from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import YPWebsite


class YPSpider(BaseSpider):
    name = "yp"
    allowed_domains = ["yellowpages.com.au"]
    start_urls = [
        "http://www.yellowpages.com.au/search/listings?clue=Dentist&locationClue=&lat=&lon=",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)

        sites = hxs.xpath('//*[@class="search-contact-card call-to-actions-4"]')

        items = []

        for site in sites:
            item = YPWebsite()
            item['business'] = site.xpath('table/tr/td/a/div[1]/text()').extract()
            item['street'] = site.xpath('table/tr[2]/td/div/div/div/div/div[2]/div/div/p/text()').extract()
            item['city'] = ''
	    item['state'] = ''
	    item['website'] = ''.join(site.xpath('div/div/div/a[@class="contact contact-main contact-url "]/@href').extract())
	    item['phone'] = ''.join(site.xpath('div/div/div/a[@class="click-to-call contact contact-preferred contact-phone "]/@href').extract())
	    item['email'] = ''.join(site.xpath('div/div/div/a[@class="contact contact-main contact-email "]/@data-email').extract())
            items.append(item)


        return items
