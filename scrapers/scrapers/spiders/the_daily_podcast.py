import scrapy
from scrapy_playwright.page import PageMethod


class TheDailyPodcastSpider(scrapy.Spider):
    name = 'the-daily-podcast'
   

    def start_requests(self):
        url = 'https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zaW1wbGVjYXN0LmNvbS81NG5BR2NJbA'
        yield scrapy.Request(url, meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods=[PageMethod('wait_for_selector', 'div[id=latest-stories]')],
            errback=self.errback,
        ))

    async def parse(self, response):
        page = response.meta["playwright_page"]

        url = response.url

        screenshot = await page.screenshot(path=f"{name(url)}.png", full_page=True)

        with open(f'./imgs/{name(url)}.png', 'wb') as f:
            f.write(screenshot)
