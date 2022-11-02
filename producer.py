from message_brokers.all_brokers import brokers
from keras.datasets import fashion_mnist

broker_name = 'kafka'
(trainX, trainy), (testX, testy) = fashion_mnist.load_data()

broker_client = brokers[broker_name]
for data in trainX[:100]:
    broker_client.send_message('test_topic', data)
