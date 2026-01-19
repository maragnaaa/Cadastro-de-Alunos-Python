from validacoes.validar_nome import validar_nome
from modelos.aluno import Aluno

def cadastrar_aluno(repo):
    while True:
        nome = input("Insira o nome do aluno: ")
        
        if not validar_nome(nome):
            print("Nome inválido, tente novamente")
            continue

        break

    while True:
        nota = float(input("Insira a nota do aluno: "))

        aluno = Aluno(nome, nota)
        repo.adicionar_aluno(aluno)

def listar_alunos(repo):
    for aluno in repo.alunos:
        print(f"{aluno.nome} | {aluno.nota} | {aluno.ativo}")

def media(repo):
    print("A média das notas:", repo.calcular_media())

def aprovados(repo):
    for aluno in repo.listar_aprovados():
        print(aluno.nome)

