"""Modelos que representam um pedido e seus itens."""

from datetime import datetime


class ItemPedido:
    """Representa uma linha do pedido: um produto e a quantidade pedida."""

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return (
            f"{self.quantidade}x {self.produto.nome} "
            f"(R$ {self.produto.preco:.2f} cada) = R$ {self.subtotal():.2f}"
        )


class Pedido:
    """Representa um pedido completo, associado a um cliente e seus itens."""

    def __init__(self, id_pedido, cliente):
        self.id = id_pedido
        self.cliente = cliente
        self.itens = []
        self.data_hora = datetime.now()
        self.desconto_aplicado = 0.0
        self.finalizado = False

    def adicionar_item(self, produto, quantidade):
        """Adiciona um item ao pedido, validando estoque disponível."""
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if not produto.esta_disponivel(quantidade):
            raise ValueError(
                f"Estoque insuficiente para '{produto.nome}'. "
                f"Disponível: {produto.estoque}."
            )
        self.itens.append(ItemPedido(produto, quantidade))

    def subtotal(self):
        """Soma dos itens, sem descontos."""
        return sum(item.subtotal() for item in self.itens)

    def calcular_total(self):
        """Total final do pedido, já com desconto de fidelidade aplicado."""
        return max(0.0, self.subtotal() - self.desconto_aplicado)

    def aplicar_desconto_fidelidade(self):
        """
        Se o cliente tiver pontos suficientes, resgata o desconto
        e o aplica a este pedido. Retorna o valor de desconto aplicado.
        """
        if self.cliente.tem_desconto_disponivel():
            self.desconto_aplicado = self.cliente.resgatar_desconto()
        return self.desconto_aplicado

    def __str__(self):
        linhas = [f"--- Pedido #{self.id} | Cliente: {self.cliente.nome} ---"]
        for item in self.itens:
            linhas.append(f"  {item}")
        linhas.append(f"  Subtotal: R$ {self.subtotal():.2f}")
        if self.desconto_aplicado:
            linhas.append(f"  Desconto fidelidade: -R$ {self.desconto_aplicado:.2f}")
        linhas.append(f"  TOTAL: R$ {self.calcular_total():.2f}")
        return "\n".join(linhas)
