import requests
from bs4 import BeautifulSoup
from roulette_russe.Scraper import Scraper


class FigaroInsidersScraper(Scraper):
    def __init__(self, input_config, output_datasets, rr=None):
        super(FigaroInsidersScraper, self).__init__(input_config, output_datasets, rr)

    def extract_feature(self, soup, feature):
        divs = soup.findAll('div', {'class': 'top-flop-item--rating'})
        for div in divs:
            if div.findAll('span')[0].text == feature:
                return div.findAll('small')[0].text
        return 0

    def _get_name(self, soup):
        return soup.findAll('div',{"class": "enterprise-header--information--details--title--name"})[0].findAll('h1')[0].text

    def _get_global_score(self, soup):
        return soup.findAll('div',{'class': 'enterprise-header--information--rating'})[0].findAll('span')[0].text

    def _get_number_of_ratings(self, soup):
        return soup.findAll('span', {'class': 'global-rating-stats--overall--count'})[0].findAll('b')[0].text

    def _get_positive_ratings(self, soup):
        return soup.findAll('div',{'class':'top-flop-full--summary__top'})[0].findAll('b')[0].text

    def _get_neutral_ratings(self, soup):
        return soup.findAll('div',{'class':'top-flop-full--summary__neutral'})[0].findAll('b')[0].text

    def _get_negative_ratings(self, soup):
        return soup.findAll('div',{'class':'top-flop-full--summary__flop'})[0].findAll('b')[0].text



    def query_company_infos(self, link):
        r = requests.get(link+'/notes', proxies=self.get_proxies()).text
        soup = BeautifulSoup(r, 'html.parser')
        return {
            'name': self._get_name(soup),
            'global_score': self._get_global_score(soup),
            'number_of_ratings': self._get_number_of_ratings(soup),
            'positive_ratings': self._get_positive_ratings(soup),
            'neutral_ratings': self._get_neutral_ratings(soup),
            'negative_ratings': self._get_negative_ratings(soup),
            'facilite_acces': self.extract_feature(soup, 'Facilité d\'accès'),
            'avantage_sociaux': self.extract_feature(soup, 'Avantages sociaux'),
            'atteinte_objectifs_entraprise': self.extract_feature(soup, 'Atteinte des objectifs de l\'entreprise'),
            'salaire': self.extract_feature(soup, 'Salaire'),
            'reconnaissance_manager': self.extract_feature(soup, 'Reconnaissance du manager'),
            'responsable_autonomie': self.extract_feature(soup, 'Responsabilité / Autonomie'),
            'espace_travail_equipements': self.extract_feature(soup, 'Espace de travail et équipements'),
            'ambiance_travail': self.extract_feature(soup, 'Ambiance de travail'),
            'formation': self.extract_feature(soup, 'Formation et développement des compétences'),
            'implication_employes': self.extract_feature(soup, 'Implication des employés'),
            'interet_projets': self.extract_feature(soup, 'Intérêts de projets / missions'),
            'valeur_culture': self.extract_feature(soup, 'Valeur et culture'),
            'evolution_crriere': self.extract_feature(soup, 'Evolution de carrière mobilité'),
            'vision_strategie': self.extract_feature(soup, 'Vision / Stratégie'),
            'transparence_information': self.extract_feature(soup, 'Transparence de l\'information'),
            'esprit_equipe': self.extract_feature(soup, 'Esprit d\'équipe'),
            'creativite_innovation': self.extract_feature(soup, 'Créativité / Innovation'),
            'politique_management': self.extract_feature(soup, 'Politique de management'),
            'communication_interne': self.extract_feature(soup, 'Communication interne'),
            'stress_passion': self.extract_feature(soup, 'Stress / Pression')

        }

    def scrap(self):
        tmp_list = []
        for link in self.input_config['links']:
            tmp_list.append(self.query_company_infos(link))
        self.output_datasets['profiles'] = self.output_datasets['profiles'].append(tmp_list, ignore_index=True)

    def quality_check(self):
        pass

