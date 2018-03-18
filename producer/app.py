from kafka import KafkaProducer
from time import sleep

print("Producer: hello!")

sleep(10.0) # Time waiting for kafka service and topics are available in seconds.

producer = KafkaProducer(bootstrap_servers='192.168.2.12:9092')
topic = "test"


count = 0
while (count < 100):
    producer.send(topic, b'test message')
    print("producer message:", count)
    sleep(0.1)
    count = count + 1

print("Good bye!")
