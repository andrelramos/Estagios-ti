#-*- coding: utf-8 -*-

import scrapy

class BancoNacionalDeEmpregos(scrapy.Spider):
    name = 'bne.com.br'
    start_urls = ['http://www.bne.com.br/resultado-pesquisa-avancada-de-vagas/88371966']

    def parse(self, response):
        for vaga in response.css('.vaga'):
            yield {
                'titulo': vaga.css('.link::text').extract(),
                'localizacao': vaga.css('span[itemprop="addressLocality"]::text').extract(),
                'descricao': vaga.css('.container_atribuicao').css('.atribuicao::text').extract(),
                'link': vaga.css('.vaga').css('.link::attr(href)').extract(),
            }

        self.log('Crawl em %s terminado' % response.url)

        proximo_link = response.css(u'a[title="Próxima Página"]::attr(href)').extract()
        if proximo_link:
            self.log('Indo para %s' % proximo_link[0])
            yield scrapy.Request(response.urljoin('http://www.bne.com.br' + proximo_link[0]))
