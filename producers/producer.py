# pip install kafka-python-ng
# pip install kafka-python


from kafka import KafkaProducer
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Crie um produtor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer
)

# Simule o envio de mensagens para um tópico
topic_name = 'meu_topico'

for i in range(100):  # Simula o envio de 100 mensagens
    message = {
        'id': i,
        'message': f'Mensagem de teste {i}',
        'timestamp': time.time()
    }
    producer.send(topic_name, message)
    print(f'Mensagem {i} enviada com sucesso!')
    time.sleep(1)  # Pausa de 1 segundo entre o envio de mensagens

# Feche o produtor
producer.flush()
producer.close()
