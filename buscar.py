import validacoes.tem_aluno as tem_aluno
from cadastrar_alunos import alunos

def buscar():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    nome = input("\nDigite o nome do aluno: ").strip().lower()

    for aluno in alunos:
        nome_salvo = aluno["nome"].strip().lower()
        
        if nome == nome_salvo:
            return aluno   

    return None