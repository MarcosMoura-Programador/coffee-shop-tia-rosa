"""
Camada de apresentação (CLI) do sistema.

Todas as funções aqui cuidam apenas de exibir informações e capturar
entradas do usuário de forma segura (tratando erros de digitação).
A lógica de negócio em si vive em SistemaCoffeeShop — este módulo
nunca acessa dicionários internos diretamente.
"""


# ----------------------------------------------------------------------
# Funções auxiliares de entrada segura (evitam que o programa quebre
# com entradas inválidas, conforme exigido pela restrição de usabilidade)
# ----------------------------------------------------------------------

def ler_texto_nao_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("⚠️  Este campo não pode ficar em branco. Tente novamente.")


def ler_inteiro(mensagem, minimo=None):
    while True:
        entrada = input(mensagem).strip()
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"⚠️  Digite um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠️  Entrada inválida. Digite um número inteiro.")


def ler_float(mensagem, minimo=None):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"⚠️  Digite um valor maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("⚠️  Entrada inválida. Digite um número (ex.: 9.90).")


def pausar():
    input("\nPressione ENTER para continuar...")


def exibir_titulo(texto):
    print("\n" + "=" * 50)
    print(texto.center(50))
    print("=" * 50)


# ----------------------------------------------------------------------
# Menus
# ----------------------------------------------------------------------

def menu_principal(sistema):
    while True:
        exibir_titulo("☕ COFFEE SHOP TIA ROSA ☕")
        print("1. Cardápio / Produtos")
        print("2. Clientes")
        print("3. Novo Pedido")
        print("4. Resumo de Vendas do Dia")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            menu_produtos(sistema)
        elif opcao == "2":
            menu_clientes(sistema)
        elif opcao == "3":
            fluxo_novo_pedido(sistema)
        elif opcao == "4":
            exibir_resumo_vendas(sistema)
        elif opcao == "0":
            print("\nAté logo! ☕ Obrigado por usar o sistema da Tia Rosa.")
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")
            pausar()


# --- Produtos --------------------------------------------------------

def menu_produtos(sistema):
    while True:
        exibir_titulo("📋 CARDÁPIO / PRODUTOS")
        print("1. Listar produtos")
        print("2. Consultar produto por código")
        print("3. Cadastrar novo produto")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos(sistema)
            pausar()
        elif opcao == "2":
            consultar_produto(sistema)
            pausar()
        elif opcao == "3":
            cadastrar_produto(sistema)
            pausar()
        elif opcao == "0":
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")
            pausar()


def listar_produtos(sistema):
    produtos = sistema.listar_produtos()
    if not produtos:
        print("\nNenhum produto cadastrado ainda.")
        return
    print("\n--- Produtos disponíveis ---")
    for produto in produtos:
        print(produto)


def consultar_produto(sistema):
    id_produto = ler_inteiro("\nDigite o código do produto: ", minimo=1)
    produto = sistema.consultar_produto(id_produto)
    if produto is None:
        print(f"⚠️  Produto com código {id_produto} não encontrado.")
    else:
        print("\n--- Detalhes do Produto ---")
        print(produto)


def cadastrar_produto(sistema):
    print("\n--- Cadastro de Novo Produto ---")
    nome = ler_texto_nao_vazio("Nome do produto: ")
    preco = ler_float("Preço (R$): ", minimo=0)
    ingredientes_texto = ler_texto_nao_vazio("Ingredientes (separados por vírgula): ")
    ingredientes = [i.strip() for i in ingredientes_texto.split(",") if i.strip()]
    categoria = ler_texto_nao_vazio("Categoria (ex.: Bebidas, Salgados, Doces): ")
    estoque = ler_inteiro("Estoque inicial: ", minimo=0)

    try:
        produto = sistema.cadastrar_produto(nome, preco, ingredientes, categoria, estoque)
        print(f"\n✅ Produto cadastrado com sucesso! Código: {produto.id}")
    except ValueError as erro:
        print(f"⚠️  Erro ao cadastrar produto: {erro}")


# --- Clientes ----------------------------------------------------------

def menu_clientes(sistema):
    while True:
        exibir_titulo("👤 CLIENTES")
        print("1. Listar clientes")
        print("2. Cadastrar novo cliente")
        print("0. Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_clientes(sistema)
            pausar()
        elif opcao == "2":
            cadastrar_cliente(sistema)
            pausar()
        elif opcao == "0":
            break
        else:
            print("⚠️  Opção inválida. Tente novamente.")
            pausar()


def listar_clientes(sistema):
    clientes = sistema.listar_clientes()
    if not clientes:
        print("\nNenhum cliente cadastrado ainda.")
        return
    print("\n--- Clientes cadastrados ---")
    for cliente in clientes:
        print(cliente)


def cadastrar_cliente(sistema):
    print("\n--- Cadastro de Novo Cliente ---")
    nome = ler_texto_nao_vazio("Nome do cliente: ")
    telefone = ler_texto_nao_vazio("Telefone: ")
    cpf = ler_texto_nao_vazio("CPF: ")

    try:
        cliente = sistema.cadastrar_cliente(nome, telefone, cpf)
        print(f"\n✅ Cliente cadastrado com sucesso! Código: {cliente.id}")
    except ValueError as erro:
        print(f"⚠️  Erro ao cadastrar cliente: {erro}")


# --- Pedidos -------------------------------------------------------------

def fluxo_novo_pedido(sistema):
    exibir_titulo("🧾 NOVO PEDIDO")

    if not sistema.listar_clientes():
        print("⚠️  Não há clientes cadastrados. Cadastre um cliente primeiro.")
        pausar()
        return
    if not sistema.listar_produtos():
        print("⚠️  Não há produtos cadastrados. Cadastre um produto primeiro.")
        pausar()
        return

    listar_clientes(sistema)
    id_cliente = ler_inteiro("\nDigite o código do cliente: ", minimo=1)

    try:
        pedido = sistema.criar_pedido(id_cliente)
    except ValueError as erro:
        print(f"⚠️  {erro}")
        pausar()
        return

    print("\nAdicione itens ao pedido (digite 0 no código do produto para finalizar a lista).")
    while True:
        listar_produtos(sistema)
        id_produto = ler_inteiro("\nCódigo do produto (0 para encerrar itens): ", minimo=0)
        if id_produto == 0:
            break

        produto = sistema.consultar_produto(id_produto)
        if produto is None:
            print(f"⚠️  Produto com código {id_produto} não encontrado.")
            continue

        quantidade = ler_inteiro(f"Quantidade de '{produto.nome}': ", minimo=1)

        try:
            pedido.adicionar_item(produto, quantidade)
            print(f"✅ {quantidade}x {produto.nome} adicionado(s) ao pedido.")
        except ValueError as erro:
            print(f"⚠️  {erro}")

    if not pedido.itens:
        print("\n⚠️  Pedido cancelado: nenhum item foi adicionado.")
        pausar()
        return

    print("\n--- Resumo do Pedido (antes da finalização) ---")
    print(pedido)

    try:
        pedido_finalizado = sistema.finalizar_pedido(pedido, usar_desconto_fidelidade=True)
    except ValueError as erro:
        print(f"\n⚠️  Não foi possível finalizar o pedido: {erro}")
        pausar()
        return

    print("\n✅ Pedido finalizado com sucesso!")
    print(pedido_finalizado)
    print(
        f"\nPontos de fidelidade do cliente agora: "
        f"{pedido_finalizado.cliente.pontos_fidelidade}"
    )
    pausar()


# --- Relatórios ------------------------------------------------------------

def exibir_resumo_vendas(sistema):
    exibir_titulo("📊 RESUMO DE VENDAS DO DIA")
    resumo = sistema.resumo_vendas_do_dia()

    print(f"Pedidos realizados hoje: {resumo['quantidade_pedidos']}")
    print(f"Faturamento do dia: R$ {resumo['faturamento']:.2f}")

    print("\nItens mais vendidos hoje:")
    if not resumo["mais_vendidos"]:
        print("  Nenhuma venda registrada hoje ainda.")
    else:
        for posicao, (nome_produto, quantidade) in enumerate(resumo["mais_vendidos"], start=1):
            print(f"  {posicao}. {nome_produto} — {quantidade} unidade(s)")

    pausar()
