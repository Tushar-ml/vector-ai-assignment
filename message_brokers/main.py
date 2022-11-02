from all_brokers import brokers

broker_name = 'kafka'
broker_client = brokers[broker_name]()

for i in range(100):
    broker_client.send_message('test_topic', str(i))
