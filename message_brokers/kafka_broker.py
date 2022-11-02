from typing import Type
from kafka import KafkaProducer, KafkaConsumer

class KafkaClient:
    
    def __init__(self,bootstrap_server="localhost:9092"):
        self.bootstrap_server = bootstrap_server
        

    def send_message(self, topic, messages: list):

        if not isinstance(messages, list):
            raise TypeError
            
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_server)
        for message in messages:
            producer.send(topic, bytes(message,'utf-8'))
            print(f'Message: {message}')
    
    def consume_message(self, topic):
        consumer = KafkaConsumer(topic, self.bootstrap_server)
        for msg in consumer:
            print(msg.value.decode('utf-8'))


        

    