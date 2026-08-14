"""Modelo que representa um cliente cadastrado no programa de fidelidade."""


class Cliente:
    """Representa um cliente da cafeteria e seus pontos de fidelidade."""

    # Regras do programa de fidelidade (constantes de classe).
    REAIS_POR_PONTO = 10.0      # a cada R$ 10,00 gastos, 1 ponto
    PONTOS_PARA_DESCONTO = 100  # 100 pontos acumulados...
    VALOR_DESCONTO = 5.0        # ...equivalem a R$ 5,00 de desconto

    def __init__(self, id_cliente, nome, telefone, cpf):
        self.id = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.pontos_fidelidade = 0

    def calcular_pontos_ganhos(self, valor_gasto):
        """Calcula quantos pontos o cliente ganha por um valor gasto."""
        return int(valor_gasto // self.REAIS_POR_PONTO)

    def adicionar_pontos(self, quantidade):
        """Credita pontos de fidelidade ao cliente."""
        self.pontos_fidelidade += quantidade

    def tem_desconto_disponivel(self):
        """Indica se o cliente já acumulou pontos suficientes para um desconto."""
        return self.pontos_fidelidade >= self.PONTOS_PARA_DESCONTO

    def resgatar_desconto(self):
        """
        Consome PONTOS_PARA_DESCONTO pontos do cliente e retorna o valor
        de desconto em reais. Deve ser chamado apenas se tem_desconto_disponivel()
        for verdadeiro.
        """
        if not self.tem_desconto_disponivel():
            raise ValueError("Cliente não possui pontos suficientes para desconto.")
        self.pontos_fidelidade -= self.PONTOS_PARA_DESCONTO
        return self.VALOR_DESCONTO

    def __str__(self):
        return (
            f"[{self.id}] {self.nome} | Tel: {self.telefone} | CPF: {self.cpf} "
            f"| Pontos: {self.pontos_fidelidade}"
        )
