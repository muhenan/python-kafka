from confluent_kafka import Consumer, KafkaError

# Define Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker(s)
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the Kafka topic
topic = 'quickstart-events'
consumer.subscribe([topic])

# Poll for new messages
while True:
    msg = consumer.poll(1.0)  # Wait for up to 1 second for messages

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event (not an error)
            print(f"Reached end of partition {msg.partition()}")
        else:
            print(f"Error while consuming message: {msg.error()}")
    else:
        # Print the received message key and value
        print(f"Received message: key={msg.key()}, value={msg.value()}")

# Close the consumer to exit the loop gracefully
consumer.close()
