from producers.producer import Producer
from consumers.consumer import Consumer
from controller.venda import SimulaPedidoVenda
from time import sleep
import random
import threading



def novoPedido():
    for i in range(4):
        s = SimulaPedidoVenda().simulaPedido()
        Producer().sendKafka(s, 'NOVO_PEDIDO')




def reservaProduto():
    for msg in Consumer().reservandoProdutoEstoque():     
        if msg['TIPO'] == 'NOVO_PEDIDO':
            print(f"Pedido reservado: {str(msg)}")



def envioNotificacao():
    for msg in Consumer().envioNotificacaoCliente():

        if msg['TIPO'] == 'NOVO_PEDIDO':
            print(f"Notificacao compra: {str(msg)}")

        elif msg['TIPO'] == 'PROCESSO_PAGAMENTO':
            print(f"Notificacao pagamento: {str(msg)}")

        elif msg['TIPO'] == 'SEPARACAO_PRODUTO':
            print(f"Notificacao separacao: {str(msg)}")

        elif msg['TIPO'] == 'FRAUDE_VERIFICADO':
            print(f"Notificacao de fraude: {str(msg)}")

        else:
            pass



def verificandoFraude():
    for msg in Consumer().analise_de_fraude():
        msg['TIPO'] = 'FRAUDE_VERIFICADO'
        msg['EXISTE_FRAUDE'] = random.choice(['SIM', 'NAO'])
        Producer().sendKafka(msg, 'FRAUDE_VERIFICADO')








# Criar threads
thread1 = threading.Thread(target=novoPedido)
thread2 = threading.Thread(target=reservaProduto)
thread3 = threading.Thread(target=envioNotificacao)
thread4 = threading.Thread(target=verificandoFraude)

# Iniciar threads
thread1.start()
thread1.join()


thread2.start()
thread3.start()
thread4.start()

# Esperar até que ambas as threads terminem

thread2.join()
thread3.join()
thread4.join()

print("Execução das threads concluída")