from persistencia.salvar_carregar_alunos import AlunoJSON
from repositorio.repositorio_aluno import RepositorioAlunos
import servicos.servicos_menu as menu
from validacoes.validar_menu import validar_menu
from modelos.modelo_menu import display
import shutil

persistencia = AlunoJSON("dados/alunos.json")
repo = RepositorioAlunos(persistencia)
largura = shutil.get_terminal_size().columns

while True:
    for d in display:
        print(d.center(largura))

    texto_opcao = input("\nInsira sua opção: ")
    if not validar_menu(texto_opcao):
        print("Opção inválida, digite novamente")
        continue
    else:
        opcao = int(texto_opcao)

    try:
        if opcao == 1:
            menu.cadastrar_aluno(repo)
        elif opcao == 2:
            menu.listar_alunos(repo)
        elif opcao == 3:
            menu.media(repo)
        elif opcao == 4:
            menu.aprovados(repo)
        else:
            print("\nEncerrado :)\n")
            break
    except ValueError as e:
        print("Erro:", e)