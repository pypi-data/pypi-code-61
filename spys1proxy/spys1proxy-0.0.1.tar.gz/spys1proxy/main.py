import asyncio
import logging
from dataclasses import dataclass, field

from pyppeteer import launch


def process_text_list(l_text: list) -> list:
    if "Squid" in l_text[2] or "Mikrotik" in l_text[2]:
        l_text[1] = f"{l_text[1]} {l_text[2]}"
        del l_text[2]
    del l_text[-5:len(l_text)]
    if ")" in l_text[-1]:
        l_text.append("-")

    try:
        float(l_text[-4])
    except ValueError:
        pass
    else:
        l_text[-4] = float(l_text[-4])
        l_text[3] = " ".join(l_text[3:-4])
        del l_text[4:-4]

    if "%" in l_text[-3]:
        l_text[-3] = int(l_text[-3].strip("%")) / 100
    return l_text


@dataclass
class Spys:
    proxy_list: list = None
    countries: list = field(default_factory=list)
    any_country: bool = False
    europe: bool = False
    north_america: bool = False

    async def search(self):
        if self.any_country:
            self.countries.extend(['DE', 'US', 'FR', 'UA', 'RU', 'PL', 'NL'])
            await self.pyppeteer_get_proxy_list()
        elif not self.any_country and self.countries:
            await self.pyppeteer_get_proxy_list()
        elif self.europe:
            await self.pyppeteer_get_proxy_list(url="http://spys.one/europe-proxy/")
        elif self.north_america:
            await self.pyppeteer_get_proxy_list(url="http://spys.one/north-america-proxy/")

    async def pyppeteer_get_proxy_list(self, url=None):
        country_list = self.countries
        browser = await launch(options={'args': ['--no-sandbox']})
        page = await browser.newPage()
        proxy_table = []
        await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
        if self.europe or self.north_america:
            country_list = ['42']  # if europe or america method will accept url option
        for country in country_list:
            page_url = url or f'http://spys.one/free-proxy-list/{country}/'
            await page.goto(page_url)
            await asyncio.gather(
                page.select('tbody #xpp', '5'),
                page.waitForSelector('tbody #xpp'),
                page.keyboard.press("Enter"),
                page.waitFor(1500)
            )
            table = await page.JJ("tr.spy1xx")
            logging.debug(f"Started working with table: {len(table[1:])} ips")
            for index, item in enumerate(table[1:]):
                str_text = await page.evaluate('(element) => element.innerText', item)
                list_text = str_text.split()
                list_text = process_text_list(list_text)
                proxy_table.append(list_text)
            logging.debug("Finished working with table")
            await asyncio.sleep(3)
        await browser.close()
        self.proxy_list = proxy_table


