import asyncio
from dataclasses import dataclass, field
import json
import random

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
import producer_server

BROKER_URL = "PLAINTEXT://localhost:9092"
TOPIC = "com.udacity.dep.police.service"

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})
    c.subscribe([topic_name])

    while True:
        messages = c.consume(5, timeout=1.0)
        print(f"consumed {len(messages)} messages")
        for message in messages:
            print(f"consume message {message.key()}: {message.value()}")
        await asyncio.sleep(0.01)

def main():
    try:
        asyncio.run(produce_consume(TOPIC))
    except KeyboardInterrupt as e:
        print("shutting down")


async def produce_consume(topic_name):
    """Runs the Producer and Consumer tasks"""
    t2 = asyncio.create_task(consume(topic_name))
    await t2

if __name__ == "__main__":
    main()
