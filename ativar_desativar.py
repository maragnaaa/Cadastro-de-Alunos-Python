import validacoes.tem_aluno as tem_aluno
import dados.salvar_dados as salvar_dados
import buscar

def ativar_desativar():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return

    aluno = buscar()
    if aluno:
        print("\nAluno encontrado:", aluno["nome"])
        status = (input("\nO aluno está ativo? (S/N): ")).lower()
        if status == "s":
            aluno["ativo"] = True
        else:
            aluno["ativo"] = False

        salvar_dados()   
    else:
        print("Aluno não encontrado")
