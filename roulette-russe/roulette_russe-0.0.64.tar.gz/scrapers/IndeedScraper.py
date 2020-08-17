import requests
from bs4 import BeautifulSoup
from roulette_russe.Scraper import Scraper


class IndeedScraper(Scraper):
    def __init__(self, input_config, output_datasets, rr=None):
        super(IndeedScraper, self).__init__(input_config, output_datasets, rr)

    def _extract_features(self, soup, feature):
        divs = soup.findAll('a', {'class': 'cmp-CompactHeaderMenuItem-link cmp-u-noUnderline'})
        for div in divs:
            if feature in div['href']:
                if len(div.findAll('div', {'class': 'cmp-CompactHeaderMenuItem-count'})) == 1:
                    return div.findAll('div', {'class': 'cmp-CompactHeaderMenuItem-count'})[0].text
        trs = soup.findAll('tr', {"class": "cmp-RatingCategory cmp-RatingCategory--md"})
        for tr in trs:
            if len(tr.findAll('td')) == 3:
                if feature in tr.findAll('td')[2].text:
                    return tr.findAll('td')[0].text
        return '-'

    def _extract_ceoRating(self, soup):
        if len(soup.findAll('div', {"class": "cmp-CeoWidgetWithRating-percent"})) == 1:
            return soup.findAll('div', {"class": "cmp-CeoWidgetWithRating-percent"})[0].text
        return '-'

    def _extract_rating(self, soup):
        return float(soup.findAll('span', {'class': 'cmp-CompactHeaderCompanyRatings-value'})[0].text.replace(',','.'))

    def _extract_name(self, soup):
        return soup.findAll('span', {'class': 'cmp-CompactHeaderCompanyName'})[0].text

    def query_company_main_infos(self, link):
        r = requests.get(link, proxies=self.get_proxies()).text
        soup = BeautifulSoup(r, 'html.parser')
        return {
            'name': self._extract_name(soup),
            'rating': self._extract_rating(soup),
            'reviews_number': self._extract_features(soup, 'reviews'),
            'salaries_number': self._extract_features(soup, 'salaries'),
            'jobs_number': self._extract_features(soup, 'jobs'),
            'photos_number': self._extract_features(soup, 'photos'),
            'direction': self._extract_features(soup, 'Direction'),
            'culture_entreprise': self._extract_features(soup, 'Culture d\'entreprise'),
            'equilibre_pro_perso': self._extract_features(soup, 'Équilibre vie professionnelle / personnelle'),
            'salaire_avantages': self._extract_features(soup, 'Salaire/Avantages sociaux'),
            'securite_emploi': self._extract_features(soup, 'Sécurité de l\'emploi/Évolution de carrière'),
            'ceo_rating': self._extract_ceoRating(soup)
        }


    def scrap(self):
        tmp_list = []
        for link in self.input_config['links']:
            tmp_list.append(self.query_company_main_infos(link))
        self.output_datasets['profiles'] = self.output_datasets['profiles'].append(tmp_list, ignore_index=True)

    def quality_check(self):
        pass