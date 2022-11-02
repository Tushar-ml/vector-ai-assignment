from message_brokers.kafka_broker import KafkaClient
from message_brokers.google_pubsub_broker import GPubSubClient

brokers = {
    'kafka': KafkaClient,
    'google_pub_sub': GPubSubClient
}
