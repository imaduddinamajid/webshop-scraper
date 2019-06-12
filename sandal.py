# -*- coding: utf-8 -*-
import json
import scrapy


class SandalSpider(scrapy.Spider):
    name = "sandal"
    api_url = "https://www.skoringen.dk/sandaler-dame/?page={}"
    start_urls = [api_url.format(1)]

    def parse(self, response):
        if response.status == 404:
            return

        sandals = response.css("div.item__price")
        for sandal in sandals:
            detail_url = sandal.css("a::attr(href)").extract_first()
            detail_url = response.urljoin(detail_url)
            yield scrapy.Request(url=detail_url, callback=self.parse_details)

        # pagination handler
        page_number = (
            int(response.css("div.col::attr(data-pageindex)").extract_first()) + 1
        )
        yield scrapy.Request(url=self.api_url.format(page_number))

    def parse_details(self, response):
        yield {
            "beskrivelse": response.css(
                "div.item-description__content::text"
            ).extract_first(),
            "materiale": response.xpath(
                '//div[contains(.//text(), "Materiale")]//div[contains(@class, "item-pim__value")]//text()'
            ).extract_first(),
            "sål": response.xpath(
                '//div[contains(.//text(), "Sål")]//div[contains(@class, "item-pim__value")]//text()'
            ).extract_first(),
        }
