import json
import re

def tem_aluno():
    return len(alunos) > 0






def calcular():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    return soma / len(alunos)



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



def editar_nota():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return

    while True:
        aluno = buscar()
        if aluno:
            print("\nAluno encontrado:", aluno["nome"])
            while True:

                nota_texto = input("Insira a nota final do aluno: ")

                if not validar_nota(nota_texto):
                    print("\nNota inválida, tente novamente.")
                    continue
                else:
                    aluno["nota"] = float(nota_texto)
                
                break
            salvar_dados()
            break
        else:
            print("Aluno não encontrado")
        



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
