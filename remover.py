import validacoes.tem_aluno as tem_aluno
import dados.salvar_dados as salvar_dados
from cadastrar_alunos import alunos
import buscar

def remover():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    aluno = buscar()
    if aluno:
        escolha = input(f"\nVocê deseja remover {aluno['nome']}? (S/N): ")
        if escolha.strip().lower() == "s":
            alunos.remove(aluno)
            salvar_dados()
            print("\nAluno removido com sucesso")
    else:
        print("Aluno não encontrado")