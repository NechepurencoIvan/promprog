import pika
import sys
import time


def on_message(ch, method, properties, body):
    print(body.decode(), flush=True)


params = pika.URLParameters("amqp://guest:guest@rabbit:5672/%2F")

for try_numb in range(10):
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.queue_declare(queue='homework')
        channel.basic_consume(on_message, 'homework')
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        print('Buye', file=sys.stderr)
        break
    except Exception:
        print('Consumer failed to connect', file=sys.stderr)
        channel.start_consuming()
