import numpy as np
import pandas as pd

import gensim
from gensim import downloader
import spacy
import torch
import transformers as ppb


class Vectorizer:
    def __init__(self, sentences):
        self.sentences = sentences
        self.words = []

    def bert(self):
        batch = pd.DataFrame(self.sentences)

        model_class, tokenizer_class, pretrained_weights = (ppb.DistilBertModel, ppb.DistilBertTokenizer, 'distilbert-base-uncased')
        tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
        model = model_class.from_pretrained(pretrained_weights)
        tokenized = batch[0].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))

        max_len = 0
        for i in tokenized.values:
            if len(i) > max_len:
                max_len = len(i)

        padded = np.array([i + [0] * (max_len - len(i)) for i in tokenized.values])
        attention_mask = np.where(padded != 0, 1, 0)
        input_ids = torch.tensor(np.array(padded)).type(torch.LongTensor)
        attention_mask = torch.tensor(attention_mask).type(torch.LongTensor)

        with torch.no_grad():
            last_hidden_states = model(input_ids)

        vectors = last_hidden_states[0][:, 0, :].numpy()

        return vectors

    def w2v(self, pretrained_model='glove-wiki-gigaword-300', ensemble_method='mean'):
        batch = pd.DataFrame(self.words)
        model = gensim.downloader.load(pretrained_model)

        vectors = []
        for index, row in batch.iterrows():
            temp = []
            for word in row['Words']:
                temp.append(model[word])

            if ensemble_method == 'mean':
                vectors.extend([np.mean(temp, axis=0)])

        return vectors

    def sent2words(self, **kwargs):
        add_stop_words = kwargs.get('add_stop_words', [])
        remove_stop_words = kwargs.get('remove_stop_words', [])
        language_model = kwargs.get('language_model', 'en_core_web_sm')

        nlp = spacy.load(language_model)
        for w in add_stop_words:
            nlp.vocab[w].is_stop = True
        for w in remove_stop_words:
            nlp.vocab[w].is_stop = False

        columns = ['Sentence', 'Tokens', 'Words', 'Entities']
        df = pd.DataFrame(columns=columns)
        for i, sentence in enumerate(self.sentences):
            doc = nlp(sentence.lower())
            df.loc[i, 'Sentence'] = sentence
            df.loc[i, 'Tokens'] = [token.orth_ for token in doc if not token.is_punct | token.is_space]
            df.loc[i, 'Words'] = [token.lemma_ for token in doc if not token.is_punct | token.is_space | token.is_stop]
            df.loc[i, 'Entities'] = [(entity.text, entity.label_) for entity in doc.ents]

        self.words = df.loc[:, 'Words']
