import json
import pika

params = pika.URLParameters('amqps://gmswhovt:fs9IP-Yabz4JY36S5q62r8LKqv1C7DNe@dingo.rmq.cloudamqp.com/gmswhovt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='boss', body=json.dumps(body), properties=properties)