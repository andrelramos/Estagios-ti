import scrapy

class Vagas(scrapy.Spider):
    name = 'vagas.com.br'
    start_urls = ['https://www.vagas.com.br/vagas-de-estagio-trainee?a[]=24&pet[]=T']

    def parse(self, response):
        site_root = 'https://www.vagas.com.br'
        for vaga in response.css('.vaga'):
            yield {
                'titulo': vaga.css('a::attr(title)').extract(),
                'localizacao': vaga.css('span[itemprop="addressLocality"]::text').extract(),
                'empresa': vaga.css('span[itemprop="name"]::text').extract(),
                'descricao': vaga.css('p[itemprop="description"]::text').extract(),
                'link': site_root + vaga.css('a[class="link-detalhes-vaga"]::attr(href)').extract()[0],
            }
