from message_brokers.all_brokers import brokers
from utils import stream_model_api

broker_client = brokers['kafka']
broker_client.consume_message('test_topic', stream_model_api)
