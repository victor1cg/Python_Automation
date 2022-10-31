
#! Clonando uma pagina HTML.

import scrapy

#CamelCase - Dentro dessa classe vamos herdar o Spider.
class QuotesToScrapeSpider(scrapy.Spider):
    name = 'frasebot'
    #Request
    def start_requests(self):
        urls =  ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(
                url = url,
                callback= self.parse
            )            
            #yield - retorna os resultado sem precisar esperar todo o loop;
            #callback - funçao de retorno. Parse é extrair os dados de uma pagina;
        return super().start_requests()
    
    #Response
    def parse(self,response):
        with open('pagina.html','wb') as arquivo:
            arquivo.write(response.body)