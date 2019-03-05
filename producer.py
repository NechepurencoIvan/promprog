import pika
import random
import sys
import time

params = pika.URLParameters("amqp://guest:guest@rabbit:5672/%2F")

for try_numb in range(10):
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='homework')
        for i in range(100):
            number = random.randint(0, 100)
            channel.basic_publish(exchange='', routing_key='homework', body=str(number))
            time.sleep(random.uniform(0.3, 1.3))
    except Exception:
        print('Producer failed to connect', file=sys.stderr)

