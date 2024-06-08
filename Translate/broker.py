import pika
import json

from translate import english_to_farsi
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('broker', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='translate_queue')
channel.queue_declare(queue='farsi_text_queue')

def publish_translated_text(file):
    channel.basic_publish(exchange='',
                    routing_key='farsi_text_queue',
                    body=json.dumps({"status": "done",'ftext': file}))
    message = {"status": "done", "ftext": file }
    
    return message


def on_etext_message(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    logging.info(data)
    if data['etext']:
        ftext= english_to_farsi(data['etext'])
        return publish_translated_text(ftext)
        


channel.basic_consume(queue='translate_queue', on_message_callback=on_etext_message, auto_ack=True)
channel.start_consuming()
