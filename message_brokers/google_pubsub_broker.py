import time
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import json
import os
# Enter your credentials.json for GCP Project
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YYYY.json"


# GCP topic, project & subscription ids
PUB_SUB_TOPIC = "my-python-topic"
PUB_SUB_PROJECT = "XXX"
PUB_SUB_SUBSCRIPTION = "my-python-topic-sub"

timeout = 20
# callback function for processing consumed payloads
# prints recieved payload


class GPubSubClient:

    @staticmethod
    def consumer_callback(message):
        print(f"Received {message.data}.")
        message.ack()

    # producer function to push a message to a topic

    @staticmethod
    def send_message(topic, message):
        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(PUB_SUB_PROJECT, topic)
        data = json.dumps(message).encode("utf-8")
        future = publisher.publish(topic_path, data=data)
        print("Pushed message to topic.")

    # consumer function to consume messages from a topics for a given timeout period
    @staticmethod
    def consume_message():
        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscriber.subscription_path(
            PUB_SUB_PROJECT, PUB_SUB_SUBSCRIPTION)
        print(f"Listening for messages on {subscription_path}..\n")
        streaming_pull_future = subscriber.subscribe(
            subscription_path, callback=GPubSubClient.consumer_callback)

        # Wrap subscriber in a 'with' block to automatically call close() when done.
        with subscriber:
            try:
                # When `timeout` is not set, result() will block indefinitely,
                # unless an exception is encountered first.
                streaming_pull_future.result(timeout=timeout)
            except TimeoutError:
                streaming_pull_future.cancel()
