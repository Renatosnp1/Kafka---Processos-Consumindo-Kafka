# Projeto Kafka com Python de Mensageria

Este projeto utiliza Kafka para comunicação assíncrona entre microserviços, implementado em Python. A arquitetura é orientada a eventos, utilizando Kafka como o sistema de mensageria para garantir a escalabilidade e a eficiência dos serviços.

## Visão Geral do Projeto

Este projeto foi desenvolvido para gerenciar o fluxo de informações entre diferentes serviços em um sistema de vendas. Utiliza quatro tópicos no Kafka para orquestrar as operações de pedidos, pagamento, verificação de fraude e processo de picking.

### Tópicos do Kafka

1. **Pedido Novo**
   - **Descrição**: Todo pedido que chegar via sistema de venda é publicado neste tópico. Outros serviços podem consumir este tópico para processar novos pedidos.
   - **Utilização**: Notificação de novos pedidos, iniciação do fluxo de processamento.

2. **Processo de Pagamento**
   - **Descrição**: Após um pedido ser processado por outros serviços (como notificação ao cliente ou reserva de produto em estoque), este tópico registra o status da validação do pagamento.
   - **Utilização**: Verificação de pagamento aprovado ou não, atualização de status financeiro.

3. **Fraude Verificado**
   - **Descrição**: Este tópico mantém a informação sobre se o pagamento de um pedido foi identificado como fraude ou não, após a verificação.
   - **Utilização**: Atualização do status de fraude, ações corretivas em caso de fraude.

4. **Processo de Picking**
   - **Descrição**: Contém o status do processo de separação dos pedidos.
   - **Utilização**: Monitoramento do processo de separação de pedidos, otimização logística.
  
   - ## Microsserviços

### Reserva do Produto
- **Descrição**: Este microserviço consome o tópico "Pedido Novo" e, assim que chega um novo pedido, reserva o produto no estoque.
- **Responsabilidade**: Garantir que os produtos sejam reservados assim que um novo pedido é registrado, evitando conflitos de estoque.

### Envio de Notificação
- **Descrição**: Este microserviço consome o tópico "Pedido Novo" para notificar o cliente que o pedido foi recebido. Também escuta o tópico "Processo de Pagamento" para notificar o cliente sobre o status do pagamento e o tópico "Processo de Picking" para informar que o pedido está sendo separado.
- **Responsabilidade**: Manter o cliente informado sobre o status do pedido em todas as etapas do processo.

### Análise de Fraude
- **Descrição**: Este microserviço consome o tópico "Pedido Novo" e realiza uma análise de fraude no pedido. Após a análise, publica no tópico "Fraude Verificado" se o pedido é fraude ou não.
- **Responsabilidade**: Identificar pedidos fraudulentos e atualizar o status de fraude para que ações corretivas possam ser tomadas.

### Análise e Relatórios
- **Descrição**: Este microserviço atualiza o banco de dados de relatórios, como um data warehouse, com informações relevantes dos pedidos e processos.
- **Responsabilidade**: Manter um registro atualizado e detalhado dos pedidos para fins de análise e relatórios.

### Processo de Picking
- **Descrição**: Após consumir o tópico "Processo de Pagamento" e confirmar que o pagamento foi aprovado, este serviço inicia o processo de separação do produto.
- **Responsabilidade**: Gerenciar a logística interna de separação e preparação dos pedidos para envio.

### Processamento de Pagamento
- **Descrição**: Este microserviço executa o pagamento referente ao pedido que chegou, atualizando o status de pagamento conforme necessário.
- **Responsabilidade**: Garantir que os pagamentos sejam processados de forma eficiente e segura, atualizando o sistema com o status do pagamento.

## Estrutura do Projeto

### `producers/`
Contém classes relacionadas aos produtores de mensagens do Kafka.

- **producer_base.py**: Define a estrutura base e métodos comuns para todos os produtores.
- **example_producer.py**: Implementação específica de um produtor que publica mensagens em um tópico.
- **factory.py**: Fábrica que facilita a criação de instâncias de produtores com configurações específicas.

### `consumers/`
Contém classes relacionadas aos consumidores de mensagens do Kafka.

- **consumer_base.py**: Define a estrutura base e métodos comuns para todos os consumidores.
- **example_consumer.py**: Implementação específica de um consumidor que lê mensagens de um tópico.
- **factory.py**: Fábrica que facilita a criação de instâncias de consumidores com configurações específicas.

### `observers/`
Contém classes relacionadas ao padrão Observer, permitindo que múltiplos componentes reajam a eventos de mensagens de forma desacoplada.

- **observer.py**: Interface base para todos os observadores.
- **concrete_observer.py**: Implementação concreta de um observador que reage às mensagens consumidas.

### `utils/`
Contém utilitários e padrões de design auxiliares.

- **circuit_breaker.py**: Implementação do padrão Circuit Breaker para gerenciar falhas de forma resiliente.
- **singleton.py**: Implementação do padrão Singleton para garantir instâncias únicas onde necessário.

### `config/`
Contém arquivos de configuração para o Kafka e outros componentes do sistema.

- **kafka_config.py**: Configurações específicas para produtores e consumidores do Kafka.

### `tests/`
Contém os testes automatizados para o projeto.

- **test_producers.py**: Testes para as classes produtoras.
- **test_consumers.py**: Testes para as classes consumidoras.
- **test_utils.py**: Testes para os utilitários.

### `main.py`
Arquivo principal que inicializa e executa os produtores e consumidores, exemplificando a integração dos componentes do projeto.


## Conclusão

Esta estrutura modular e orientada a eventos permite que cada componente do sistema tenha uma responsabilidade bem definida, promovendo a escalabilidade e a facilidade de manutenção. A utilização de Kafka como sistema de mensageria garante que os serviços possam se comunicar de maneira eficiente e desacoplada, suportando um alto volume de transações e mantendo a integridade dos dados através de tópicos bem definidos. Cada microsserviço desempenha um papel crucial na orquestração do fluxo de pedidos, desde a recepção até a entrega final, garantindo uma operação suave e eficiente.
