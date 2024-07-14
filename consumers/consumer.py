from kafka import KafkaConsumer
import json


class Consumer:

    def __json_deserializer(self, data):
        return json.loads(data.decode('utf-8'))



    def processo_de_pagamento(self):
        consumer = KafkaConsumer( 
           'FRAUDE_VERIFICADO',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value




    def reservando_produto_estoque(self):
        consumer = KafkaConsumer(
           'NOVO_PEDIDO', 
           'PROCESSO_PAGAMENTO',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value


            


    def envio_notificacao_cliente(self):
        consumer = KafkaConsumer(
           'NOVO_PEDIDO', 
           'PROCESSO_PAGAMENTO',
           'SEPARACAO_PRODUTO',
           'FRAUDE_VERIFICADO',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value




    def analise_de_fraude(self):
        consumer = KafkaConsumer(
           'NOVO_PEDIDO', 
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value




    def analise_e_relatorio(self):
        consumer = KafkaConsumer(
           'NOVO_PEDIDO', 
           'SEPARACAO_PRODUTO',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value





    def separacao_produto(self):
        consumer = KafkaConsumer(
           'PROCESSO_PAGAMENTO',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='meu_grupoA',
            value_deserializer = self.__json_deserializer)
        
        for message in consumer:
            yield message.value










# def json_deserializer(data):
#     return json.loads(data.decode('utf-8'))

# # Crie um consumidor Kafka
# consumer = KafkaConsumer(
#     'NOVO_PEDIDO',
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='meu_grupo',
#     value_deserializer=json_deserializer
# )

# # Consuma as mensagens do tópico
# for message in consumer:
#     print(f'Mensagem recebida: {message.value}')
