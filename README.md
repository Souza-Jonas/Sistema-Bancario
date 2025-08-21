# Sistema-Bancario


📋 Funcionalidades Principais
- Depósito (d):
O usuário informa um valor positivo, que é adicionado ao saldo e registrado no extrato.
- Saque (s):
O usuário pode sacar um valor, desde que:
- Tenha saldo suficiente
- O valor não ultrapasse o limite de saque (R$ 500)
- Não tenha excedido o número máximo de saques diários (3)
- Extrato (e):
Exibe todas as movimentações realizadas (depósitos e saques), além do saldo atual.
- Sair (q):
Encerra o programa com uma mensagem de despedida.

🧠 Estrutura do Código
1. Constantes e Variáveis Globais
MENU = """..."""
LIMITE_SAQUE = 500
MAX_SAQUES_DIARIOS = 3
saldo = 0
extrato = []
numero_saques = 0


- Define o menu de opções e os limites operacionais.
- saldo, extrato e numero_saques são usados para controlar o estado da conta.
2. Função depositar(valor)
- Valida se o valor é positivo.
- Atualiza o saldo e registra no extrato.
- Exibe mensagem de sucesso ou erro.
3. Função sacar(valor)
- Verifica se o valor é válido e se atende às regras de saque.
- Atualiza o saldo e o número de saques.
- Registra no extrato e exibe mensagens apropriadas.
4. Função mostrar_extrato()
- Exibe todas as movimentações registradas.
- Mostra o saldo atual.
- Se não houver movimentações, informa ao usuário.
5. Loop Principal (while True)
- Exibe o menu e aguarda a escolha do usuário.
- Chama a função correspondente à opção selecionada.
- Trata entradas inválidas com try/except para evitar erros de conversão.

##########################################################################################
DOCUMENTAÇÃO V3


🧾 Visão Geral
Este sistema implementa uma estrutura de banco digital com suporte a:
- Cadastro de clientes (Pessoa Física)
- Criação de contas correntes
- Realização de transações (depósitos e saques)
- Registro de histórico de transações
- Exibição de extrato bancário

🏗️ Estrutura de Classes
Cliente
Representa um cliente genérico do banco.
- Atributos:
- endereco: endereço do cliente
- contas: lista de contas associadas
- Métodos:
- realizar_transacao(conta, transacao): executa uma transação em uma conta
- adicionar_conta(conta): adiciona uma conta à lista do cliente

PessoaFisica(Cliente)
Especialização de Cliente para pessoas físicas.
- Atributos adicionais:
- nome
- data_nascimento
- cpf

Conta
Classe base para contas bancárias.
- Atributos:
- _saldo: saldo da conta
- _numero: número da conta
- _agencia: agência fixa "0001"
- _cliente: referência ao cliente dono da conta
- _historico: instância de Historico
- Métodos:
- nova_conta(cliente, numero): método de fábrica para criar nova conta
- sacar(valor): realiza saque, com validações
- depositar(valor): realiza depósito, com validações

ContaCorrente(Conta)
Especialização de Conta com regras específicas de saque.
- Atributos adicionais:
- _limite: valor máximo por saque
- _limite_saques: número máximo de saques permitidos
- Métodos sobrescritos:
- sacar(valor): verifica limites antes de permitir saque
- __str__(): retorna representação textual da conta

Historico
Armazena o histórico de transações de uma conta.
- Atributos:
- _transacoes: lista de dicionários com tipo, valor e data
- Métodos:
- adicionar_transacao(transacao): registra uma nova transação

Transacao (ABC)
Classe abstrata para representar uma transação.
- Métodos abstratos:
- valor: propriedade que retorna o valor da transação
- registrar(conta): método que executa a transação na conta

Saque(Transacao) e Deposito(Transacao)
Implementações concretas de transações.
- Atributos:
- _valor: valor da transação
- Métodos:
- registrar(conta): executa a operação e registra no histórico

🧮 Funções Utilitárias
- menu(): exibe o menu de opções
- filtrar_cliente(cpf, clientes): busca cliente pelo CPF
- recuperar_conta_cliente(cliente): retorna a primeira conta do cliente
- depositar(clientes): fluxo de depósito
- sacar(clientes): fluxo de saque
- exibir_extrato(clientes): mostra extrato da conta
- criar_cliente(clientes): cadastra novo cliente
- criar_conta(numero_conta, clientes, contas): cria nova conta corrente
- listar_contas(contas): exibe todas as contas cadastradas

🧠 Observações Técnicas
- O sistema não permite o cliente escolher entre múltiplas contas (FIXME no código).
- O uso de abstractclassmethod e abstractproperty está obsoleto; o correto seria @abstractmethod com @classmethod ou @property.
- O menu é interativo via terminal, ideal para testes locais.
- O histórico de transações registra data e hora, mas o formato de hora usa %s, que não é válido para segundos.





