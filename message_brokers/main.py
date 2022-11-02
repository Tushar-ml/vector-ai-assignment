from all_brokers import brokers

broker_name = 'google_pub_sub'
broker_client = brokers[broker_name]

broker_client.send_message('test_topic', list(range(100)))
