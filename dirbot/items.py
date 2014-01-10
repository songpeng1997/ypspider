from scrapy.item import Item, Field


class YPWebsite(Item):

    business = Field()
    street = Field()
    city = Field()
    state = Field()
    website = Field()
    phone = Field()
    email = Field()
