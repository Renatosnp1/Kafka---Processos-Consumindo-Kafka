from kafka import KafkaConsumer
import json


class Consumer:

    def __init__(self) -> None:
        self.ProdutosReservado = []


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
            if message.value['N_PEDIDO'] not in self.ProdutosReservado:
                self.ProdutosReservado.append(message.value['N_PEDIDO'])
            yield message.value




    def reservandoProdutoEstoque(self):
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


            


    def envioNotificacaoCliente(self):
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



if __name__ == "__main__":
    for i in Consumer().envioNotificacaoCliente():
        print(i)