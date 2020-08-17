import requests 
from importlib import resources # Python 3.7+
import configparser
import os
import json

class SentenceEncoder():
    def __init__(self, server_url=None):
        self.server_url = server_url

    def clean_text(self, sentences):
        sentences = [sent.replace(u'\xa0', u' ') for sent in sentences]
        return sentences

    def encode_qna_questions(self, questions):
        if type(questions) == str:
            questions = [questions]

        headers = {'Content-Type': 'application/json'}
        predict_request = '{"signature_name":"question_encoder", "instances":' +json.dumps(self.clean_text(questions), ensure_ascii=False)+ '}'

        response = requests.post(self.server_url, data=predict_request.encode('utf-8'), headers=headers)

        response.raise_for_status()
        question_embeddings = response.json()['predictions']
        return question_embeddings

    def encode_qna_responses(self, responses, response_contexts):
        headers = {'Content-Type': 'application/json'}
        predict_request = '{"signature_name":"response_encoder", "instances":[{"input":' +json.dumps(self.clean_text(responses), ensure_ascii=False)+ ', "context":' + json.dumps(self.clean_text(response_contexts), ensure_ascii=False)+ '}]}'

        response = requests.post(self.server_url, data=predict_request.encode('utf-8'), headers=headers)

        response.raise_for_status()
        question_embeddings = response.json()['predictions']
        return question_embeddings

