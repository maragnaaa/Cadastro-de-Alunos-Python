import validacoes.tem_aluno as tem_aluno
import validacoes.validar_nota as validar_nota
import dados.salvar_dados as salvar_dados
import servicos.buscar as buscar
from modelos.alunos import alunos

def editar_nota():
    if not tem_aluno.tem_aluno(alunos):
        print("\nNão há alunos registrados\n")
        return

    while True:
        aluno = buscar.buscar()
        if aluno:
            print("\nAluno encontrado:", aluno["nome"])
            while True:

                nota_texto = input("Insira a nota final do aluno: ")

                if not validar_nota.validar_nota(nota_texto):
                    print("\nNota inválida, tente novamente.")
                    continue
                else:
                    aluno["nota"] = float(nota_texto)
                
                break
            salvar_dados.salvar_dados()
            break
        else:
            print("Aluno não encontrado")