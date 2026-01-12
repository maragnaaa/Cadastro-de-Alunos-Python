import validacoes.validar_nome as validar_nome
import validacoes.validar_aluno as validar_aluno
import validacoes.validar_nota as validar_nota
import validacoes.validar_status as validar_status
import dados.salvar_dados as salvar_dados
from modelos.alunos import alunos

def cadastrar_alunos():
    while True:
        nome = input("\nInsira o nome do aluno: ")

        if not validar_nome.validar_nome(nome):
            print("\nNome inválido, tente novamente.")
            continue

        if validar_aluno.validar_aluno(nome, alunos):
            print("\nEsse aluno já está cadastrado.")
            continue

        break

    while True:

        nota_texto = input("Insira a nota final do aluno: ")

        if not validar_nota.validar_nota(nota_texto):
            print("\nNota inválida, tente novamente.")
            continue
        else:
            nota = float(nota_texto)
        
        break

    while True:

        status = input("O aluno está ativo? (S/N): ")

        if not validar_status.validar_status(status):
            print("\nOpção inválida, tente novamente.")
            continue
        else:
            if status == "s":
                ativo = True
            else:
                ativo = False

        break

    aluno = {
        "nome" : nome,
        "nota" : nota,
        "ativo" : ativo
    }

    alunos.append(aluno)
    salvar_dados.salvar_dados()