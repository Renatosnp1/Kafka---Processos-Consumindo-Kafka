from datetime import datetime
import time
import random



class SimulaPedidoVenda:    

    def simulaPedido(self):
            
        time.sleep(random.randint(4, 12))

        numero_pedido = f'{random.randint(100, 999999)}'.zfill(8)

        now = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

        pedido = {'TIPO':'NOVO_PEDIDO', 'N_PEDIDO': numero_pedido, 'DATA_HORA_PEDIDO': now, 'METODOS_PAGAMENTO': self.__metodoDePagamento()}

        return pedido



    def __metodoDePagamento(self):
        randInt = random.randint(0, 100)

        if randInt > 85 or randInt < 15:
            return "CARTAO CREDITO"
        
        else:
            return "DINHEIRO"



if __name__ == '__main__':

    for i in range(10):
        s = SimulaPedidoVenda().simulaPedido()   
        print(s) 


