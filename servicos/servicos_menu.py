from validacoes.validacoes import validar_nome
from validacoes.validacoes import validar_nota
from modelos.aluno import Aluno

def cadastrar_aluno(repo):
    while True:
        nome = input("Insira o nome do aluno: ")
        
        if not validar_nome(nome):
            print("Nome inválido, tente novamente")
            continue

        break

    while True:
        nota_texto = input("Insira a nota do aluno: ")

        if not validar_nota(nota_texto):
            print("Nota inválida, tente novamente")
            continue
        else:
            nota = float(nota_texto)
        break

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

