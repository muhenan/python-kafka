# python-kafka
python kafka

## Set up Kafka Broker

like a kafka server

Kafka is a Java application, so jdk is required

**Todo!!!: Read https://www.conduktor.io/kafka/kafka-brokers/**

A topic may have more than one partition. Each partition may live on different servers, also known as Kafka brokers.


Things to learn:
* Kafka broker
* Kafka cluster
* Partition
* Topic
* Kafka Client

Set up kafka broker: https://kafka.apache.org/quickstart

Apache ZooKeeper

Apache ZooKeeper is a distributed coordination service that plays a critical role in managing distributed systems and ensuring their reliability. It provides coordination, synchronization, and configuration management for distributed applications. ZooKeeper is often used alongside Apache Kafka and other distributed systems to maintain distributed state and perform leader election.

1. start zookeeper: `PS C:\kafka_2.13-3.5.0\bin\windows> .\zookeeper-server-start.bat ..\..\config\zookeeper.properties`
    * [2023-09-21 01:12:22,369] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
2. start kafka: `PS C:\kafka_2.13-3.5.0\bin\windows> .\kafka-server-start.bat ..\..\config\server.properties`
    * [2023-09-21 01:13:52,384] INFO Awaiting socket connections on 0.0.0.0:9092. (kafka.network.DataPlaneAcceptor)

```bash

PS C:\kafka_2.13-3.5.0\bin\windows> .\kafka-topics.bat --create --topic quickstart-events --bootstrap-server localhost:9092
Created topic quickstart-events.
PS C:\kafka_2.13-3.5.0\bin\windows>
PS C:\kafka_2.13-3.5.0\bin\windows>
PS C:\kafka_2.13-3.5.0\bin\windows> .\kafka-topics.bat --describe --topic quickstart-events --bootstrap-server localhost:9092
Topic: quickstart-events        TopicId: nUORQX4ASROv0NUU0U6gKQ PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: quickstart-events        Partition: 0    Leader: 0       Replicas: 0     Isr: 0
PS C:\kafka_2.13-3.5.0\bin\windows>


```

A topic is like a queue, message queue


## Conclusion

In our project, kafka is server is our own machine, it should be a remote server.

Need to learn more about Distributed System and Kafka.