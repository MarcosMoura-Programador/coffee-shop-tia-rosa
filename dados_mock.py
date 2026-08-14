"""
Carrega dados de exemplo (mock data) no sistema para permitir testes
imediatos, sem precisar cadastrar tudo manualmente na primeira execução.
"""


def carregar_dados_iniciais(sistema):
    """Popula o sistema com produtos e clientes de exemplo."""

    # --- Produtos ---
    sistema.cadastrar_produto(
        nome="Café Expresso",
        preco=6.50,
        ingredientes=["café", "água"],
        categoria="Bebidas Quentes",
        estoque=100,
    )
    sistema.cadastrar_produto(
        nome="Cappuccino",
        preco=9.90,
        ingredientes=["café", "leite", "espuma de leite", "canela"],
        categoria="Bebidas Quentes",
        estoque=60,
    )
    sistema.cadastrar_produto(
        nome="Café Gelado",
        preco=10.50,
        ingredientes=["café", "gelo", "leite"],
        categoria="Bebidas Frias",
        estoque=40,
    )
    sistema.cadastrar_produto(
        nome="Pão de Queijo",
        preco=5.00,
        ingredientes=["polvilho", "queijo", "ovo", "leite"],
        categoria="Salgados",
        estoque=50,
    )
    sistema.cadastrar_produto(
        nome="Croissant",
        preco=8.00,
        ingredientes=["farinha", "manteiga", "fermento"],
        categoria="Salgados",
        estoque=30,
    )
    sistema.cadastrar_produto(
        nome="Bolo de Cenoura",
        preco=7.50,
        ingredientes=["cenoura", "farinha", "açúcar", "chocolate"],
        categoria="Doces",
        estoque=20,
    )
    sistema.cadastrar_produto(
        nome="Brigadeiro",
        preco=3.50,
        ingredientes=["chocolate", "leite condensado", "granulado"],
        categoria="Doces",
        estoque=45,
    )

    # --- Clientes ---
    sistema.cadastrar_cliente(nome="Maria Silva", telefone="(11) 91234-5678", cpf="111.111.111-11")
    sistema.cadastrar_cliente(nome="João Pereira", telefone="(11) 99876-5432", cpf="222.222.222-22")
    sistema.cadastrar_cliente(nome="Ana Souza", telefone="(11) 90000-1111", cpf="333.333.333-33")
