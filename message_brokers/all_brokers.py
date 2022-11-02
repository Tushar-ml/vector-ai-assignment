from kafka_broker import KafkaClient
from google_pubsub_broker import GPubSubClient


brokers = {
    'kafka': KafkaClient,
    'google_pub_sub': GPubSubClient
}
