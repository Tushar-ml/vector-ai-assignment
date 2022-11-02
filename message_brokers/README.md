# Message Broker

This section deals with implementation of streaming message brokers like Apache Kafka, and Google Cloud Pub/Sub and how you can add your own custom message brokers easily.

## File Structure

- **kafka_broker.py** : This contans kafka implementation. It is having KafkaClient class having two `@staticmethod` methods `send_message` and `consume_message`. This structure must be followed all brokers (your custom brokers as well). Some config variable are:

  - bootstrap_servers = list of servers, default:"localhost:9092"

- **google_pubsub_broker.py** : This contains Google Pub/Sub Implementation. It is having GPubSubClient class having two `@staticmethod` methods `send_message` and `consume_message`. Some config variables are:

  - "GOOGLE_APPLICATION_CREDENTIALS": your-service-account credentials json file

  - PUB_SUB_PROJECT: GCP Project Name or ID

- **all_brokers.py** : This file contains all imports of different broker clients, so that we just based on string like 'kafka' and 'google_cloud_pub_sub' we can import whole implementation in our `main.py` file.

- **main.py** : This file will be the interface for the message broker section. Just assign what broker you need to `broker_name` variable. In the back-end it is prepared for you to serve. No need to change anything and send anything with `broker_client.send_message('topic',message)`

## How to add custom broker

1. Create a class with two `@staticmethod` decorator methods `send_message` and `consume_message` with following arguments:

   - send_message: It is a publisher of your broker

     - topic: topic to which publisher will send
     - message: message to be sent by publisher

   - consume_message: It is a subscriber module of your broker
     - topic: topic/subscription from which it needs to consume message

   Take an hint from `kafka_broker.py` and `google_pubsub_broker.py`

2. After that, add your client `brokers` dict variable in `all_brokers.py`

That's it you have **successfully added** your custom broker

## Run the Code

Just change message, broker to be send and run `python3 main.py` from message_brokers directory
