import sys
from confluent_kafka import Producer


# command
# python .\producer_take_arguments.py localhost:9092 quickstart-events my-key my-value

def produce_message(bootstrap_servers, topic, key, value):
    producer_config = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'python-producer'
    }

    producer = Producer(producer_config)

    try:
        # Produce a message to the topic with the specified key and value
        producer.produce(topic, key=key, value=value)
        producer.flush()
        print(f"Produced message with key: {key}, value: {value} to topic: {topic}")
    except Exception as e:
        print(f"Error producing message: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python producer.py <bootstrap_servers> <topic> <key> <value>")
        sys.exit(1)

    bootstrap_servers = sys.argv[1]
    topic = sys.argv[2]
    key = sys.argv[3]
    value = sys.argv[4]

    produce_message(bootstrap_servers, topic, key, value)
