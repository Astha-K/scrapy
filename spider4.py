import scrapy
class Spider(scrapy.Spider):
    name = 'spider4'
    start_urls = ['https://www.gmac-cambodia.org/our_member']

    def parse(self, response):
        all_members = response.css('div.ml-2')
        #('//div[@class="ml-2"]')
        #print(all_members.getall())


        for member in all_members:
            name = member.css('h4::text').get()
            product = member.xpath('//p/a/text()[0]').get()
            #workers = member.xpath('.//p/br/text()').extract_first()
            #location = member.xpath('.//p/br/text()').extract_first()'''

            yield {
                'Name': name,
                'product': product,
                #'No. of Workers': workers,
                #'Location'=location
            }