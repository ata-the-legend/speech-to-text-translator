
import pika
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

credentials = pika.PlainCredentials('guest', 'guest')



def publish_for_translate(file):
    connection = pika.BlockingConnection(pika.ConnectionParameters('broker', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='translate_queue')
    logging.info(file)
    channel.basic_publish(exchange='',
                    routing_key='translate_queue',
                    body=json.dumps({"status": "In progress", 'etext': file}))
    message = {"status": "In progress", "text": "" }
    return message




