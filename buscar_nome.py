import validacoes.tem_aluno as tem_aluno
import buscar

def buscar_nome():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return

    aluno = buscar()
    if aluno:
        print("\nAluno encontrado")
        print("\nNome:" ,aluno["nome"])
        print("Nota Final:" ,aluno["nota"])
        print("Ativo:" ,aluno["ativo"])
        print("-------------------------------")
    else:
        print("Aluno não encontrado")