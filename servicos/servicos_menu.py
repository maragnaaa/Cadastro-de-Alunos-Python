from modelos.aluno import Aluno

def cadastrar_aluno(repo):
    nome = input("Insira o nome do aluno: ")
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

