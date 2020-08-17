"""
import pytest


@pytest.fixture
def wordnet():
    return WordnetEnricher('
    [{"@id":"https://api.sauce-project.tech/assets/1234","@type":["https://vocabularies.sauce-project.tech/core/Asset"],"https://vocabularies.sauce-project.tech/core/depicts":[{"@id":"https://api.sauce-project.tech/depictions/1234"}]},{"@id":"https://api.sauce-project.tech/depictions/1234","@type":["https://vocabularies.sauce-project.tech/core/Depiction"],"https://vocabularies.sauce-project.tech/core/label":[{"@value":"running"}]},{"@id":"https://vocabularies.sauce-project.tech/core/Asset"},{"@id":"https://vocabularies.sauce-project.tech/core/Depiction"}]
    ')


def test_lemmas(wordnet):
	assert len(wordnet.extract_lemmas('running')) > 0

def test_synonyms(wordnet):
	assert len(wordnet.extract_synonyms('running')) > 0


def test_enrichment(wordnet):
	res = wordnet.enrich()
	assert len(res.query("SELECT ?dep core:label ?label", WordnetEnricher.query_ns)) > 1
	assert len(res.query("SELECT ?dep core:label ?label", WordnetEnricher.query_ns)) > 1
"""

import unittest
import json
from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib.serializer import Serializer
from sauce.nltkrdf.wordnet import WordnetEnricher

class WordnetEnricherTestCase(unittest.TestCase):

    def setUp(self):
    	self.enricher = WordnetEnricher("""[{"@id":"https://api.sauce-project.tech/assets/1234","@type":["https://vocabularies.sauce-project.tech/core/Asset"],"https://vocabularies.sauce-project.tech/core/depicts":[{"@id":"https://api.sauce-project.tech/depictions/1234"}]},{"@id":"https://api.sauce-project.tech/depictions/1234","@type":["https://vocabularies.sauce-project.tech/core/Depiction"],"https://vocabularies.sauce-project.tech/core/label":[{"@value":"running"}]},{"@id":"https://vocabularies.sauce-project.tech/core/Asset"},{"@id":"https://vocabularies.sauce-project.tech/core/Depiction"}]""")

    def test_lemmas(self):
    	assert len(self.enricher.extract_lemmas('running')) > 0

    def test_synonyms(self):
    	assert len(self.enricher.extract_synonyms('running')) > 0

    def test_enrichment(self):
    	json_res = json.loads(self.enricher.enrich())
    	res = Graph().parse(data=json.dumps(json_res), format='json-ld')
    	assert len(res.query("SELECT ?dep ?label WHERE { ?dep core:label ?label }", initNs=WordnetEnricher.query_ns)) > 1
    	assert len(res.query("SELECT ?dep ?label WHERE { ?dep core:synonym ?label }", initNs=WordnetEnricher.query_ns)) > 1