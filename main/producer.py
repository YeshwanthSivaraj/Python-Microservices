# amqps://nauaddno:u5Q2gBQSIiWwPgRDvE9qulOF5W4ehUvp@hornet.rmq.cloudamqp.com/nauaddno

import pika, json

params = pika.URLParameters('amqps://nauaddno:u5Q2gBQSIiWwPgRDvE9qulOF5W4ehUvp@hornet.rmq.cloudamqp.com/nauaddno')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
