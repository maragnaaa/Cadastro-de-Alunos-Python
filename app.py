import dados.carregar_dados as carregar_dados
import servicos.cadastrar_alunos as cadastrar_alunos 
import servicos.listar_alunos as listar_alunos 
import servicos.calcular as calcular 
import servicos.listar_aprovados as listar_aprovados
import servicos.buscar_nome as buscar_nome
import servicos.editar_nota as editar_nota
import servicos.remover as remover
import servicos.ativar_desativar as ativar_desativar
import validacoes.validar_menu as validar_menu
from modelos.modelo_menu import menu
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

    if opcao == 1:
        cadastrar_alunos.cadastrar_alunos()
    elif opcao == 2:
        listar_alunos.listar_alunos()
    elif opcao == 3:
        media = calcular.calcular()
        if media is not None:
            print("\nA média das notas: ", media, "\n")
    elif opcao == 4:
        listar_aprovados.listar_aprovados()
    elif opcao == 5:
        buscar_nome.buscar_nome()
    elif opcao == 6:
        editar_nota.editar_nota()
    elif opcao == 7:
        remover.remover()
    elif opcao == 8:
        ativar_desativar.ativar_desativar()
    else:
        print("\nEncerrado! :)\n")
        break