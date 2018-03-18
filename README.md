# LotteSimulator

The goal is to simulate Lotte appointment events with fake data in order to build anomaly detection solutions on the dsh

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
docker <https://docs.docker.com/install/>
git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>
```

### Installing

A step by step series of examples that tell you have to get a development env running

Clone the repository

```
$ git clone <https://github.com/Arend-Jan/LotteSimulator>
```

Change ip address to  your assigned ip address (needs to be fixed)

```
/docker-compose.yml change "KAFKA_ADVERTISED_HOST_NAME: 192.168.2.12" with own ip address
/producer/app.py change "producer = KafkaProducer(bootstrap_servers='192.168.2.12:9092')" with own ip address
/anomalyconsumer/app.py change "consumer = KafkaConsumer('my-topic', bootstrap_servers=['192.168.2.12:9092'])" with own ip address
```

Building the simulator and running it

```
$ docker-compose build && docker-compose up
```

## Authors

* **Arend-Jan Oosterveld** - *Initial work* - [Arend-Jan](https://github.com/Arend-Jan/)
