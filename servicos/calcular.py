import validacoes.tem_aluno as tem_aluno
from modelos.alunos import alunos

def calcular():
    if not tem_aluno.tem_aluno(alunos):
        print("\nNão há alunos registrados\n")
        return
    
    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    return soma / len(alunos)
