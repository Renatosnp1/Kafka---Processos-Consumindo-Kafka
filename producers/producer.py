# pip install kafka-python-ng
# pip install kafka-python
from kafka import KafkaProducer
import json


class Producer:

    def __init__(self) -> None:
        pass


    def __json_serializer(self, data):
        return json.dumps(data).encode('utf-8')


    def sendKafka(self, msg, topic_name):
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer = self.__json_serializer)


        producer.send(topic_name, msg)
        print(f'Novo pedido Criado com Sucesso! ' + str(msg))
        producer.flush()
        producer.close()



if __name__ == '__main__':
    pass
