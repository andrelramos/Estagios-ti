import scrapy

class Curriculum(scrapy.Spider):
    name = 'curriculum.com.br'
    start_urls = ['http://www.curriculum.com.br/candidatos/vagas-emprego/area-Tecnologia,-Inform%C3%A1tica-e-Internet/de-Estagiario%28a%29-Informatica/', 'http://www.curriculum.com.br/candidatos/vagas-emprego/area-Tecnologia,-Inform%C3%A1tica-e-Internet/de-Estagiario%28a%29-Tecnologia-da-Informacao/']

    def parse(self, response):
        site_root = 'http://www.curriculum.com.br'
        for vaga in response.css('.notice-of-vacancy'):
            yield {
                'titulo': vaga.css('.txt-info-color.mt-05.title').css('a::text').extract(),
                'localizacao': vaga.css('.bold-none::text').extract(),
                'empresa': vaga.css('p[class="text-muted small"]::text').extract(),
                'descricao': vaga.css('.mt-10.text-muted::text').extract(),
                'link': site_root + vaga.css('.txt-info-color.mt-05.title').css('a::attr(href)').extract()[0],
            }

        self.log('Crawl em %s terminado' % response.url)

        proximo_link = scrapy.Selector(text=response.css('.pagination').extract()[0]).xpath("(//li[last()])").extract()
        if proximo_link:
            self.log('Indo para %s' % proximo_link[0])
            yield scrapy.Request(response.urljoin(proximo_link[0]))
