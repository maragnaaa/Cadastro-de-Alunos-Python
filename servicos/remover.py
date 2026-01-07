import validacoes.tem_aluno as tem_aluno
import dados.salvar_dados as salvar_dados
from modelos.alunos import alunos
import servicos.buscar as buscar

def remover():
    if not tem_aluno.tem_aluno(alunos):
        print("\nNão há alunos registrados\n")
        return
    
    aluno = buscar.buscar()
    if aluno:
        escolha = input(f"\nVocê deseja remover {aluno['nome']}? (S/N): ")
        if escolha.strip().lower() == "s":
            alunos.remove(aluno)
            salvar_dados.salvar_dados()
            print("\nAluno removido com sucesso")
    else:
        print("Aluno não encontrado")