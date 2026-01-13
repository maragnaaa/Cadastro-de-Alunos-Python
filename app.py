import dados.carregar_dados as carregar_dados
import validacoes.validar_menu as validar_menu
from modelos.modelo_menu import menu
from controladores.controle_menu import executar_opcao
import shutil

carregar_dados.carregar_dados()

largura = shutil.get_terminal_size().columns

while True:
    for linha in menu:
        print(linha.center(largura))

    texto_opcao = input("\nInsira sua opção: ")
    if not validar_menu.validar_menu(texto_opcao):
        print("Opção inválida, digite novamente")
        continue
    else:
        opcao = int(texto_opcao)

    if not executar_opcao(opcao):
        print("\nEncerrado! :)\n")
        break
