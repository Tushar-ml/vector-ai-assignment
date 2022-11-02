import json
from kafka import KafkaProducer, KafkaConsumer

bootstrap_server = "localhost:9092"


class KafkaClient:

    @staticmethod
    def send_message(topic, messages: list):

        if not isinstance(messages, list):
            raise TypeError

        producer = KafkaProducer(bootstrap_servers=bootstrap_server)
        for message in messages:
            message = json.dumps(message).encode("utf-8")
            producer.send(topic, message)
            print(f'Message: {message}')

    @staticmethod
    def consume_message(topic, callback_function):
        print("Consumer Started")
        consumer = KafkaConsumer(
            topic, bootstrap_servers=bootstrap_server, auto_offset_reset='earliest', enable_auto_commit=True)
        for msg in consumer:
            callback_function(msg.value.decode('utf-8'))
