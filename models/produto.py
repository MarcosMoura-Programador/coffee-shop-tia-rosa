"""Modelo que representa um item do cardápio da cafeteria."""


class Produto:
    """Representa um produto do cardápio (ex.: Café Expresso, Pão de Queijo)."""

    def __init__(self, id_produto, nome, preco, ingredientes, categoria, estoque):
        self.id = id_produto
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes  # lista de strings
        self.categoria = categoria
        self.estoque = estoque

    def esta_disponivel(self, quantidade=1):
        """Verifica se há estoque suficiente para a quantidade solicitada."""
        return self.estoque >= quantidade

    def reduzir_estoque(self, quantidade):
        """Dá baixa no estoque após a venda. Lança erro se não houver saldo."""
        if not self.esta_disponivel(quantidade):
            raise ValueError(
                f"Estoque insuficiente para '{self.nome}'. "
                f"Disponível: {self.estoque}, solicitado: {quantidade}."
            )
        self.estoque -= quantidade

    def repor_estoque(self, quantidade):
        """Adiciona unidades ao estoque (reposição/compra de insumos)."""
        if quantidade <= 0:
            raise ValueError("A quantidade de reposição deve ser positiva.")
        self.estoque += quantidade

    def __str__(self):
        ingredientes_str = ", ".join(self.ingredientes)
        return (
            f"[{self.id}] {self.nome} - R$ {self.preco:.2f} "
            f"({self.categoria}) | Estoque: {self.estoque} "
            f"| Ingredientes: {ingredientes_str}"
        )
