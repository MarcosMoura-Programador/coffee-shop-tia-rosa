# ☕ Coffee Shop Tia Rosa — Sistema de Gestão

Sistema de gestão via linha de comando (CLI) desenvolvido em Python puro para a cafeteria **Coffee Shops Tia Rosa**, criado para resolver problemas operacionais causados pela falta de automação: pedidos em papel, ausência de controle de estoque e vendas, e falta de um programa de fidelização de clientes.

A interface foi desenhada para ser **simples, numerada e à prova de falhas**, pensando em uma equipe com pouca familiaridade com tecnologia.

## Funcionalidades

- **Cardápio / Produtos**
  - Cadastrar produtos (nome, preço, ingredientes, categoria, estoque)
  - Listar todos os produtos disponíveis
  - Consultar um produto específico por código
- **Clientes & Fidelização**
  - Cadastrar clientes (nome, telefone, CPF)
  - Acúmulo automático de pontos de fidelidade a cada compra (1 ponto a cada R$ 10,00 gastos)
  - Desconto automático de R$ 5,00 ao atingir 100 pontos acumulados
- **Pedidos & Vendas**
  - Registrar um novo pedido associando itens do cardápio a um cliente
  - Validação de estoque antes de confirmar o pedido
  - Baixa automática de estoque ao finalizar o pedido
  - Cálculo automático do total, com aplicação de desconto de fidelidade
  - Resumo de vendas do dia: faturamento total e itens mais vendidos
- **Interface CLI amigável**
  - Menus numerados e navegação simples
  - Tratamento de exceções em todas as entradas (o programa nunca quebra com digitação inválida)

## Requisitos

- Python 3.8 ou superior (não utiliza nenhuma dependência externa — apenas biblioteca padrão)

## Como executar

```bash
# Clone ou baixe o projeto, depois entre na pasta:
cd coffee-shop-tia-rosa

# Execute o sistema:
python main.py
```

O sistema já inicia com **dados de exemplo pré-carregados** (produtos e clientes), permitindo testar todas as funcionalidades imediatamente, sem necessidade de cadastro manual prévio.

## Estrutura do projeto

```
coffee-shop-tia-rosa/
│
├── main.py                        # Ponto de entrada da aplicação
├── dados_mock.py                  # Dados de exemplo (produtos e clientes)
│
├── models/                        # Entidades do domínio (POO)
│   ├── produto.py                  # Classe Produto
│   ├── cliente.py                  # Classe Cliente (regras de fidelidade)
│   └── pedido.py                   # Classes Pedido e ItemPedido
│
├── sistema/
│   └── sistema_coffee_shop.py      # Classe SistemaCoffeeShop (regras de negócio)
│
├── cli/
│   └── menu.py                     # Menus e interação com o usuário no terminal
│
├── README.md
└── relatorio_tecnico.md           # Relatório técnico do projeto
```

## Exemplo de uso rápido

1. Ao abrir o sistema, escolha a opção `3` (Novo Pedido)
2. Selecione o código do cliente na lista exibida
3. Informe os códigos dos produtos desejados e as quantidades
4. Digite `0` para encerrar a lista de itens
5. O sistema calcula o total automaticamente, aplica desconto de fidelidade (se disponível) e credita pontos ao cliente

## Regras de negócio

| Regra | Descrição |
|---|---|
| Pontos de fidelidade | 1 ponto a cada R$ 10,00 gastos no pedido finalizado |
| Desconto por fidelidade | A cada 100 pontos acumulados, o cliente recebe R$ 5,00 de desconto automático no próximo pedido |
| Controle de estoque | Todo item do pedido é validado contra o estoque disponível antes da finalização; o estoque é atualizado automaticamente |

## Autoria

Projeto acadêmico/prático desenvolvido para a disciplina/atividade referente ao sistema de gestão do **Coffee Shops Tia Rosa**.
