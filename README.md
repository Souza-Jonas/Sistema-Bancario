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



