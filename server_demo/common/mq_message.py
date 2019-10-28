
from server_demo.common.base import Single
from random import randint

import pika


class   MqServer(Single):
    def get_conn(self, url='localhost'):
        conn = pika.BlockingConnection(pika.ConnectionParameters(url))
        return conn


mq_conn = MqServer().get_conn()

def   mq_productor():
    channel = mq_conn.channel()
    channel.exchange_declare('demo.exchange',  exchange_type='direct')
    channel.queue_declare(queue='demo_queue')
    channel.queue_declare(queue='demo_queue2')
    channel.queue_bind('demo_queue', 'demo.exchange',   routing_key='route')
    channel.queue_bind('demo_queue2', 'demo.exchange',   routing_key='demo_route2')
    for i in range(10):
        channel.basic_publish(exchange='demo.exchange', routing_key='route', body=str(randint(1, 9)))
        channel.basic_publish(exchange='demo.exchange', routing_key='demo_route2', body=str(randint(100, 999)))



def mq_comsumer():
    channel = mq_conn.channel()
    channel.queue_declare(queue='demo_queue')
    channel.queue_declare(queue='demo_queue2')

    channel.basic_consume(queue='demo_queue2',  on_message_callback=message_handler, auto_ack = True)
    channel.basic_consume(queue='demo_queue',  on_message_callback=message_handler, auto_ack = True)
    channel.start_consuming()


def message_handler(ch, method, properties, body):
    print(ch, method, properties, body, 'i get the data')


if __name__ == "__main__":
    mq_productor()
    mq_comsumer()