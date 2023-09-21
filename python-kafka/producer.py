from confluent_kafka import Producer

# Define Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
    'client.id': 'python-producer'
}

# Create a Kafka producer instance
producer = Producer(producer_config)

# Define the Kafka topic you want to produce to
topic = 'quickstart-events'

# Produce a message to the topic
message_key = 'key1'
message_value = 'Hello, Kafka!'
producer.produce(topic, key=message_key, value=message_value)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()
