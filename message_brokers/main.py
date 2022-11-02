from all_brokers import brokers

broker_name = 'kafka'
broker_client = brokers[broker_name]()

broker_client.send_message('test_topic', list(range(100)))
