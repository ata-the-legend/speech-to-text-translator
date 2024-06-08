import pika
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('broker', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='farsi_text_queue')

def on_ftext_message(ch, method, properties, body):
    data = json.loads(body.decode('utf-8'))
    logging.info(data)
    if data['ftext']:
        print(data)
        with open("translated_data.json", "wb") as f:
            f.write(body)
        return data


channel.basic_consume(queue='farsi_text_queue', on_message_callback=on_ftext_message, auto_ack=True)
channel.start_consuming()