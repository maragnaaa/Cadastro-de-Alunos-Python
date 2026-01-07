import dados.carregar_dados as carregar_dados
import servicos.cadastrar_alunos as cadastrar_alunos 
import servicos.listar_alunos as listar_alunos 
import servicos.calcular as calcular 
import servicos.listar_aprovados as listar_aprovados
import servicos.buscar_nome as buscar_nome
import servicos.editar_nota as editar_nota
import servicos.remover as remover
import servicos.ativar_desativar as ativar_desativar

carregar_dados.carregar_dados()

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