import tem_aluno

def listar_alunos():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    for aluno in alunos:
        print("\nNome:" ,aluno["nome"])
        print("Nota Final:" ,aluno["nota"])
        print("Ativo:" ,aluno["ativo"])
        print("-------------------------------")