from all_brokers import brokers

broker_name = 'kafka'
broker_client = brokers[broker_name]

broker_client.send_message('test_topic', list(range(101)))
val = broker_client.consume_message(
    'test_topic', callback_function=lambda x: print(x))
