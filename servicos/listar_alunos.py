import validacoes.tem_aluno as tem_aluno
from modelos.alunos import alunos
import dados.carregar_dados as carregar_dados

carregar_dados.carregar_dados()

def listar_alunos():
    if not tem_aluno.tem_aluno(alunos):
        print("\nNão há alunos registrados\n")
        return
    
    for aluno in alunos:
        print("\nNome:" ,aluno["nome"])
        print("Nota Final:" ,aluno["nota"])
        print("Ativo:" ,aluno["ativo"])
        print("-------------------------------")