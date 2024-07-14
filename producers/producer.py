# pip install kafka-python-ng
# pip install kafka-python
from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime


class Producer:

    def __init__(self) -> None:
        pass


    def __json_serializer(self, data):
        return json.dumps(data).encode('utf-8')




    def send_kafka(self, msg, topic_name):
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer = self.__json_serializer)


        producer.send(topic_name, msg)
        print(f'Novo pedido Criado com Sucesso! ' + str(msg))
        producer.flush()
        producer.close()



    def simula_pedido(self):
        
        time.sleep(random.randint(4, 12))

        numero_pedido = f'{random.randint(100, 999999)}'.zfill(8)
        now = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        msg = {'TIPO':'NOVO_PEDIDO', 'N_PEDIDO': numero_pedido, 'DATA_HORA_PEDIDO': now, 'METODOS_PAGAMENTO': 'XXXXXX'}
        self.send_kafka(msg, 'NOVO_PEDIDO')



if __name__ == '__main__':

    for i in range(5):
        Producer().simula_pedido()










    # def test(self):
    #     # Crie um produtor Kafka
    #     producer = KafkaProducer(
    #         bootstrap_servers=['localhost:9092'],
    #         value_serializer = self.json_serializer
    #     )


    #     # Simule o envio de mensagens para um tópico
    #     topic_name = 'meu_topico'

    #     for i in range(100):  # Simula o envio de 100 mensagens
    #         message = {
    #             'id': i,
    #             'message': f'Mensagem de teste {i}',
    #             'timestamp': time.time()
    #         }
    #         producer.send(topic_name, message)
    #         print(f'Mensagem {i} enviada com sucesso!')
    #         time.sleep(1)  # Pausa de 1 segundo entre o envio de mensagens


    #     # Feche o produtor
    #     producer.flush()
    #     producer.close()
