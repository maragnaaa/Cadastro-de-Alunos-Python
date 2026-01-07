import validacoes.tem_aluno as tem_aluno
from cadastrar_alunos import alunos

def listar_aprovados():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    contador = 0

    for aluno in alunos:
        if aluno["nota"] >= 6.0:
            print("Nome:" ,aluno["nome"])
            print("Aprovado! :)\n")
            contador += 1
    
    print("\nAlunos aprovados:" ,contador, "\n")