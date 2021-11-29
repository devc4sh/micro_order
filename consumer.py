import pika
import django, os, json

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'order.settings')
django.setup()
from user_order.models import Order




params = pika.URLParameters('amqps://gmswhovt:fs9IP-Yabz4JY36S5q62r8LKqv1C7DNe@dingo.rmq.cloudamqp.com/gmswhovt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    id = json.loads(body)
    print(id)
    order = Order.objects.get(id=id)
    order.delivery_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='order', on_message_callback=callback,  auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()