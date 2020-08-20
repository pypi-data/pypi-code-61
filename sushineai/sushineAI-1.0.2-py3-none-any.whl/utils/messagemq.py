"""
@author: zhangX
@license: (C) Copyright 1999-2019, NJ_LUCULENT Corporation Limited.
@contact: 494677221@qq.com
@file: messagemq.py
@time: 2020/4/11 15:21
@desc:
"""
import json

from kafka import KafkaProducer, KafkaConsumer, TopicPartition


class MessageMq:
    pass


class KafkaProducers:
    def __init__(self, args):
        self.kafkaProducer = KafkaProducer(
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            bootstrap_servers=['{0}:{1}'
                                   .format(args.get('kafkaHost'),
                                           args.get('kafkaPort'))])
        self.kafkaTopic = args.get('kafkaTopic')

    def send(self, **kwargs):
        self.kafkaProducer.send(self.kafkaTopic, kwargs.get('data'), partition=0)


class KafkaConsumers:
    def __init__(self, args):
        self.kafkaConsumer = KafkaConsumer(
            value_deserializer=json.loads,
            bootstrap_servers=['{0}:{1}'
                                   .format(args.get('kafkaHost'),
                                           args.get('kafkaPort'))])
        self.kafkaTopic = args.get('kafkaTopic')
        self.tp = TopicPartition(self.kafkaTopic, 0)
        self.kafkaConsumer.assign([self.tp])

    def get_batch(self):
        self.kafkaConsumer.seek(self.tp,
                                max(self.kafkaConsumer.end_offsets([self.tp]).get(self.tp) - 1, 0))
        for msg in self.kafkaConsumer:
            return msg.value

    def get_stream(self):
        self.kafkaConsumer.seek_to_end()
        return self.kafkaConsumer
