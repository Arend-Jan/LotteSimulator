from kafka import KafkaConsumer
from time import sleep

print("Consumer: hello!")

sleep(10.0) # Time waiting for kafka service and topics are available in seconds.

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('test', bootstrap_servers=['192.168.2.12:9092'])
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

print("Consumer: Good bye!")
