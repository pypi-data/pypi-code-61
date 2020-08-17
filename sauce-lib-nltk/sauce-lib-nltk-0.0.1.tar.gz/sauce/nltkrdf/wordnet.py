from rdflib import Namespace
from nltk.corpus import wordnet as wn
from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib.serializer import Serializer
from nltk.tokenize import TreebankWordTokenizer
from rdflib import URIRef, BNode, Literal

class WordnetEnricher:

	CORE = Namespace('https://vocabularies.sauce-project.tech/core/')
	DEPICTIONS = Namespace('https://api.sauce-project.tech/depictions/')
	ASSETS = Namespace('https://api.sauce-project.tech/assets/')

	query_ns = { 'core': CORE, 'dp': DEPICTIONS, 'assets':ASSETS }

	def __init__(self, asset):
		self.asset = Graph().parse(data=asset, format='json-ld')


	def enrich(self):
		labels = self.asset.query("""SELECT DISTINCT ?depiction ?label WHERE {?depiction a core:Depiction. ?depiction core:label ?label}""",initNs=WordnetEnricher.query_ns)

		for label_row in labels:
			depiction_id = label_row['depiction']
			label = label_row['label']
			for lemma in self.extract_lemmas(label):
				if lemma != label:
					self.enrich_lemma(lemma, depiction_id)	
			for synonym in self.extract_synonyms(label):
				self.enrich_synonym(synonym, depiction_id)

		return self.asset.serialize(format='json-ld')

	def extract_lemmas(self, label):
		lemmas = []
		syn = wn.synsets(label)[0]
		for lemma in syn.lemmas():
			lemmas.append(lemma.name().replace("_"," "))
		return set(lemmas)

	def extract_synonyms(self, label):
		synonyms = []
		for syn in wn.synsets(label):
		    for lemma in syn.lemmas():
		        synonyms.append(lemma.name().replace("_"," "))
		return set(synonyms)
			
	def enrich_lemma(self, lemma, depiction_id):
		self.asset.add((URIRef(depiction_id), WordnetEnricher.CORE.label, Literal(lemma)))
		return self.asset

	def enrich_synonym(self, syn, depiction_id):
		self.asset.add((URIRef(depiction_id), WordnetEnricher.CORE.synonym, Literal(syn)))
		return self.asset