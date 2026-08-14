"""
Classe fachada (Facade) que centraliza toda a lógica de negócio do sistema:
cadastro de produtos e clientes, criação de pedidos, controle de estoque
e geração de relatórios de vendas.

O menu da CLI (cli/menu.py) só conversa com esta classe — ele nunca
manipula diretamente dicionários internos ou objetos de outros módulos.
"""

from datetime import date

from models.produto import Produto
from models.cliente import Cliente
from models.pedido import Pedido


class SistemaCoffeeShop:
    def __init__(self):
        self.produtos = {}   # id -> Produto
        self.clientes = {}   # id -> Cliente
        self.pedidos = []    # lista de Pedido finalizados

        self._proximo_id_produto = 1
        self._proximo_id_cliente = 1
        self._proximo_id_pedido = 1

    # ------------------------------------------------------------------
    # Produtos
    # ------------------------------------------------------------------
    def cadastrar_produto(self, nome, preco, ingredientes, categoria, estoque):
        if preco < 0 or estoque < 0:
            raise ValueError("Preço e estoque não podem ser negativos.")
        produto = Produto(self._proximo_id_produto, nome, preco, ingredientes, categoria, estoque)
        self.produtos[produto.id] = produto
        self._proximo_id_produto += 1
        return produto

    def listar_produtos(self):
        return list(self.produtos.values())

    def consultar_produto(self, id_produto):
        return self.produtos.get(id_produto)

    # ------------------------------------------------------------------
    # Clientes
    # ------------------------------------------------------------------
    def cadastrar_cliente(self, nome, telefone, cpf):
        if any(c.cpf == cpf for c in self.clientes.values()):
            raise ValueError(f"Já existe um cliente cadastrado com o CPF {cpf}.")
        cliente = Cliente(self._proximo_id_cliente, nome, telefone, cpf)
        self.clientes[cliente.id] = cliente
        self._proximo_id_cliente += 1
        return cliente

    def listar_clientes(self):
        return list(self.clientes.values())

    def buscar_cliente_por_id(self, id_cliente):
        return self.clientes.get(id_cliente)

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes.values():
            if cliente.cpf == cpf:
                return cliente
        return None

    # ------------------------------------------------------------------
    # Pedidos
    # ------------------------------------------------------------------
    def criar_pedido(self, id_cliente):
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            raise ValueError(f"Cliente com id {id_cliente} não encontrado.")
        pedido = Pedido(self._proximo_id_pedido, cliente)
        self._proximo_id_pedido += 1
        return pedido

    def finalizar_pedido(self, pedido, usar_desconto_fidelidade=True):
        """
        Confirma o pedido: dá baixa no estoque de cada item, aplica desconto
        de fidelidade (se solicitado e disponível), credita pontos ganhos
        e registra o pedido no histórico de vendas.
        """
        if not pedido.itens:
            raise ValueError("Não é possível finalizar um pedido sem itens.")

        # Valida disponibilidade de TODOS os itens antes de alterar qualquer estoque,
        # para não deixar o estoque inconsistente em caso de erro no meio do processo.
        for item in pedido.itens:
            if not item.produto.esta_disponivel(item.quantidade):
                raise ValueError(
                    f"Estoque insuficiente para '{item.produto.nome}' "
                    f"no momento da finalização."
                )

        for item in pedido.itens:
            item.produto.reduzir_estoque(item.quantidade)

        if usar_desconto_fidelidade:
            pedido.aplicar_desconto_fidelidade()

        pontos_ganhos = pedido.cliente.calcular_pontos_ganhos(pedido.calcular_total())
        pedido.cliente.adicionar_pontos(pontos_ganhos)

        pedido.finalizado = True
        self.pedidos.append(pedido)
        return pedido

    # ------------------------------------------------------------------
    # Relatórios
    # ------------------------------------------------------------------
    def pedidos_do_dia(self, dia=None):
        dia = dia or date.today()
        return [p for p in self.pedidos if p.data_hora.date() == dia]

    def resumo_vendas_do_dia(self, dia=None):
        """Retorna um dicionário com faturamento total e itens mais vendidos do dia."""
        pedidos_hoje = self.pedidos_do_dia(dia)
        faturamento = sum(p.calcular_total() for p in pedidos_hoje)

        contagem_itens = {}  # nome_produto -> quantidade vendida
        for pedido in pedidos_hoje:
            for item in pedido.itens:
                contagem_itens[item.produto.nome] = (
                    contagem_itens.get(item.produto.nome, 0) + item.quantidade
                )

        mais_vendidos = sorted(contagem_itens.items(), key=lambda par: par[1], reverse=True)

        return {
            "quantidade_pedidos": len(pedidos_hoje),
            "faturamento": faturamento,
            "mais_vendidos": mais_vendidos,
        }
