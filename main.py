from producers.producer import Producer
from consumers.consumer import Consumer
from time import sleep
import random

import threading







def verificando_fraude():
    for msg in Consumer().analise_de_fraude():
        n_pedido = msg['N_PEDIDO']
        print(f"Analisando Fraude - Pedido: {n_pedido}")
        msg['TIPO'] = random.choice(['NAO_FRAUDE', 'FRAUDE'])
        Producer().send_kafka(msg, 'FRAUDE_VERIFICADO')



def reserva_produto():
    for msg in Consumer().reservando_produto_estoque():     
        if msg['TIPO'] == 'NOVO_PEDIDO':
            n_pedido = msg['N_PEDIDO']
            print(f"Pedido: {n_pedido} com produtos reservados!!!")

        elif msg['TIPO'] == 'PROCESSO_PAGAMENTO':
            pass









# Criar threads
thread1 = threading.Thread(target=reserva_produto)
thread2 = threading.Thread(target=verificando_fraude)

# Iniciar threads
thread1.start()
thread2.start()

# Esperar até que ambas as threads terminem
thread1.join()
thread2.join()

print("Execução das threads concluída")