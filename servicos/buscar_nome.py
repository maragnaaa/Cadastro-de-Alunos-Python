import validacoes.tem_aluno as tem_aluno
import servicos.buscar as buscar
from modelos.alunos import alunos

def buscar_nome():
    if not tem_aluno.tem_aluno(alunos):
        print("\nNão há alunos registrados\n")
        return

    aluno = buscar.buscar()
    if aluno:
        print("\nAluno encontrado")
        print("\nNome:" ,aluno["nome"])
        print("Nota Final:" ,aluno["nota"])
        print("Ativo:" ,aluno["ativo"])
        print("-------------------------------")
    else:
        print("Aluno não encontrado")