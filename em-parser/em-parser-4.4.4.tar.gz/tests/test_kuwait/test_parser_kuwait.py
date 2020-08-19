""" Test related to Kuwait """
from em_parser.em_parser import __version__, Parser


class TestParserKuwait:
    """ Suite tests for Kuwait. """

    def test_parse(self):
        """ Bug #1 """

        expected = {
            'AccountName': 'N/A',
            'AdGroupName': r'GS:ar-KU_NB\GE=Cargo/BM',
            'AirlineCode': 'KU',
            'AirlineName': 'Kuwait',
            'Audience': 'N/A',
            'CampaignName': r'GS:ar-KU_NB\Generic=Cargo/Geo@KU',
            'CampaignType': 'Generic',
            'Destination': 'N/A',
            'GeoTarget': 'KU',
            'KeywordGroup': 'Cargo',
            'KeywordType': 'Generic',
            'Language': 'ar',
            'LocationType': 'N/A',
            'Market': 'KU',
            'MarketingNetwork': 'Search',
            'MatchType': 'BM',
            'Network': 'N/A',
            'Origin': 'N/A',
            'ParseRegexId': 'EveryMundo-NewGeneric',
            'ParserVersion': '4.4.3',
            'RouteLocale': 'N/A',
            'RouteType': 'N/A',
            'SearchEngine': 'Google',
            'SpecialCampaign': 'N/A'
        }

        result = Parser(cached=False).parse(
            r'GS:ar-KU_NB\Generic=Cargo/Geo@KU',
            r'GS:ar-KU_NB\GE=Cargo/BM',
            airline_name='Kuwait',
            search_engine='Google',
            na=True
        )

        assert result == expected
