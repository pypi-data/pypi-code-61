from sent2vec.vectorizer import Vectorizer

from numpy import dot
from numpy.linalg import norm


def cosine_distance(a, b):
    cos_sim = dot(a, b) / (norm(a) * norm(b))
    return 1 - cos_sim


def test_sent2vec_bert_01():
    sentences = [
        "This is an awesome book to learn NLP.",
        "DistilBERT is an amazing NLP model.",
        "We can interchangeably use embedding or encoding, or vectorizing.",
    ]
    vectorizer = Vectorizer(sentences)
    vectors = vectorizer.bert()
    assert len(vectors[0, :]) == 768


def test_sent2vec_bert_02():
    sentences = [
        "This is an awesome book to learn NLP.",
        "DistilBERT is an amazing NLP model.",
        "We can interchangeably use embedding, encoding, or vectorizing.",
    ]
    vectorizer = Vectorizer(sentences)
    vectors = vectorizer.bert()
    dist_1 = cosine_distance(vectors[0], vectors[1])
    dist_2 = cosine_distance(vectors[0], vectors[2])
    assert dist_1 < dist_2


def test_sent2vec_w2v():
    sentences = [
        "This is an awesome book to learn NLP.",
        "DistilBERT is an amazing NLP model.",
        "We can interchangeably use embedding, encoding, or vectorizing.",
    ]
    vectorizer = Vectorizer(sentences)
    vectorizer.sent2words(add_stop_words=['distilbert'])
    vectors = vectorizer.w2v()
    dist_1 = cosine_distance(vectors[0], vectors[1])
    dist_2 = cosine_distance(vectors[0], vectors[2])
    assert dist_1 < dist_2


def test_sent2vec_w2v_bert():
    sentences = [
        "Alice is in the Wonderland.",
        "Alice is not in the Wonderland.",
    ]
    vectorizer = Vectorizer(sentences)
    vectorizer.sent2words(remove_stop_words=['no', 'not'])
    vectors = vectorizer.w2v()
    dist_w2v = cosine_distance(vectors[0], vectors[1])
    vectors = vectorizer.bert()
    dist_bert = cosine_distance(vectors[0], vectors[1])
    assert dist_w2v > dist_bert
