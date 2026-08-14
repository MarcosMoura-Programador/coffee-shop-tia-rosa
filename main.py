"""
Ponto de entrada do sistema Coffee Shop Tia Rosa.

Execução:
    python main.py
"""

from sistema.sistema_coffee_shop import SistemaCoffeeShop
from dados_mock import carregar_dados_iniciais
from cli.menu import menu_principal


def main():
    sistema = SistemaCoffeeShop()
    carregar_dados_iniciais(sistema)

    try:
        menu_principal(sistema)
    except KeyboardInterrupt:
        # Permite encerrar o programa com Ctrl+C sem gerar um traceback assustador.
        print("\n\nPrograma encerrado pelo usuário. Até logo!")


if __name__ == "__main__":
    main()
