from kafka import KafkaConsumer
import json

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Crie um consumidor Kafka
consumer = KafkaConsumer(
    'meu_topico',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='meu_grupo',
    value_deserializer=json_deserializer
)

# Consuma as mensagens do tópico
for message in consumer:
    print(f'Mensagem recebida: {message.value}')
