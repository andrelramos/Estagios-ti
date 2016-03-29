import scrapy

class Vagas(scrapy.Spider):
    name = 'infojobs.com.br'
    start_urls = ['http://www.infojobs.com.br/empregos-de-informatica-ti-telecomunicacoes.aspx?TipoContrato=4&Page=1']

    def parse(self, response):
        for vaga in response.css('.unstyled.left'):
            yield {
                'titulo': vaga.css('h2[itemprop="title"]::text').extract(),
                'localizacao': vaga.css('li[class="location2"]::attr(title)').extract(),
                'empresa': vaga.css('span[itemprop="name"]::text').extract(),
                'descricao': vaga.css('li[itemprop="description"]::text').extract(),
                'link': vaga.css('.vagaTitle::attr(href)').extract(),
            }

        self.log('Crawl em %s terminado' % response.url)

        proximo_link = response.css('.lnkNext::attr(href)').extract()
        if proximo_link:
            self.log('Indo para %s' % proximo_link[0])
            yield scrapy.Request(response.urljoin(proximo_link[0]))
