# RELATÓRIO TÉCNICO — SISTEMA DE GESTÃO COFFEE SHOP TIA ROSA

Este relatório documenta o sistema de gestão desenvolvido em Python para o Coffee Shop Tia Rosa, uma aplicação de linha de comando responsável pelo controle de pedidos, estoque e fidelização de clientes, construída apenas com recursos da biblioteca padrão da linguagem.

## 1 DESCRIÇÃO DO SISTEMA

### 1.1 Contexto e problema

O Coffee Shop Tia Rosa ainda opera de forma manual, com pedidos anotados em papel e estoque controlado de memória, o que gera erros nos horários de pico e nenhuma forma de fidelizar clientes recorrentes. Como a equipe tem pouca familiaridade com tecnologia, optou-se por uma interface simples de linha de comando, com menus numerados.

### 1.2 Arquitetura do sistema

O código foi dividido em três camadas: as classes de domínio (Produto, Cliente, Pedido), que cuidam dos próprios dados; a classe SistemaCoffeeShop, responsável pelas regras de negócio e pela busca de produtos e clientes em dicionários; e a camada de interface, que só lida com entrada e saída de dados no terminal, sempre por meio dos métodos da classe principal. Essa separação facilita testes e futuras mudanças, como substituir o terminal por outra interface sem alterar a lógica de negócio. O projeto não usa bibliotecas externas, apenas o módulo datetime da biblioteca padrão.

## 2 EXPLICAÇÃO DO CÓDIGO

### 2.1 Produto

Representa um item do cardápio, com nome, preço, ingredientes, categoria e estoque. Os métodos principais verificam disponibilidade e dão baixa no estoque, impedindo vendas acima da quantidade disponível.

### 2.2 Cliente

Guarda os dados do cliente e os pontos de fidelidade. As regras do programa de pontos ficam centralizadas em constantes da classe, facilitando ajustes futuros.

### 2.3 Pedido e ItemPedido

Um pedido reúne um cliente e uma lista de itens, cada um com produto e quantidade. A classe calcula o subtotal, aplica desconto de fidelidade quando disponível e nunca permite total negativo.

### 2.4 SistemaCoffeeShop

Centraliza as regras de negócio. Ao finalizar um pedido, primeiro confere se há estoque suficiente para todos os itens e só depois efetua a baixa, evitando inconsistências. Em seguida aplica o desconto, credita pontos ao cliente e registra a venda para o resumo diário de faturamento e itens mais vendidos.

### 2.5 Interface de linha de comando

Contém funções de leitura segura de texto e números, que pedem a informação novamente em caso de erro, sem interromper o programa. O fluxo de novo pedido verifica clientes e produtos cadastrados, adiciona itens um a um e só finaliza após confirmação, exibindo o total e os pontos atualizados do cliente.

### 2.6 Dados de exemplo e ponto de entrada

O arquivo de dados de exemplo carrega produtos e clientes fictícios, permitindo testar o sistema sem cadastro manual prévio. O ponto de entrada apenas inicializa o sistema, carrega esses dados e chama o menu principal.

## 3 CONCLUSÃO

### 3.1 Impacto esperado

O sistema deve reduzir erros no registro de pedidos, manter o estoque atualizado automaticamente e dar visibilidade diária sobre faturamento e produtos mais vendidos. O programa de fidelidade cria um incentivo concreto para o retorno de clientes, e a interface simples favorece a adoção pela equipe.

### 3.2 Limitações e melhorias futuras

Os dados não são persistidos entre execuções, não há controle de qual atendente registrou cada venda, e o resumo de vendas cobre apenas o dia atual. Esses pontos são os próximos passos naturais para evoluir o sistema.

### 3.3 Aprendizados

O projeto reforçou a importância de dividir responsabilidades entre classes bem definidas, o que facilitou testes e correções, além de destacar a necessidade de tratar entradas inválidas como parte central do projeto, dado o público que vai operar o sistema no dia a dia.
