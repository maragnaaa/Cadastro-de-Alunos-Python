import dados.carregar_dados as carregar_dados
import cadastrar_alunos 
import listar_alunos 
import calcular 
import listar_aprovados
import buscar_nome
import editar_nota
import remover
import ativar_desativar

carregar_dados()

while True:
    print("-------------------------------")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Calcular média de notas")
    print("4 - Listar alunos aprovados")
    print("5 - Buscar aluno pelo nome")
    print("6 - Editar nota do aluno")
    print("7 - Remover aluno")
    print("8 - Ativar / Desativar aluno")
    print("9 - Encerrar")
    print("-------------------------------")

    opcao = int(input("Insira sua opção: "))

    if opcao == 1:
        cadastrar_alunos()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        media = calcular()
        if media is not None:
            print("\nA média das notas: ", media, "\n")
    elif opcao == 4:
        listar_aprovados()
    elif opcao == 5:
        buscar_nome()
    elif opcao == 6:
        editar_nota()
    elif opcao == 7:
        remover()
    elif opcao == 8:
        ativar_desativar()
    else:
        print("\nEncerrado! :)\n")
        break