import json
alunos = []
import re

def tem_aluno():
    return len(alunos) > 0



def validar_nome(texto):
    padrao = r"^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$"
    return bool(re.fullmatch(padrao, texto))



def validar_aluno(nome):
    nome = nome.strip().lower()

    for aluno in alunos:
        nome_salvo = aluno["nome"].strip().lower()
        if nome == nome_salvo:
            return True
    
    return False



def validar_nota(texto):
    padrao = r"^(10(\.0+)?|[0-9](\.[0-9]+)?)$"
    return bool(re.fullmatch(padrao, texto))



def validar_status(texto):
    padrao = r"^[sSnN]$"
    return bool(re.fullmatch(padrao, texto))



def cadastrar():
    while True:
        nome = input("\nInsira o nome do aluno: ")

        if not validar_nome(nome):
            print("\nNome inválido, tente novamente.")
            continue

        if validar_aluno(nome):
            print("\nEsse aluno já está cadastrado.")
            continue

        break

    while True:

        nota_texto = input("Insira a nota final do aluno: ")

        if not validar_nota(nota_texto):
            print("\nNota inválida, tente novamente.")
            continue
        else:
            nota = float(nota_texto)
        
        break

    while True:

        status = input("O aluno está ativo? (S/N): ")

        if not validar_status(status):
            print("\nOpção inválida, tente novamente.")
            continue
        else:
            if status == "s":
                ativo = True
            else:
                ativo = False

        break

    aluno = {
        "nome" : nome,
        "nota" : nota,
        "ativo" : ativo
    }

    alunos.append(aluno)
    salvar_dados()



def salvar_dados():
    with open("alunos.json", "w") as arq:
        json.dump(alunos, arq)



def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        alunos = []



def listar_alunos():
    if not tem_aluno():
        print("\nNão há alunos registrados\n")
        return
    
    for aluno in alunos:
        print("\nNome:" ,aluno["nome"])
        print("Nota Final:" ,aluno["nota"])
        print("Ativo:" ,aluno["ativo"])
        print("-------------------------------")



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
    
    aluno = buscar()
    if aluno:
        print("\nAluno encontrado:", aluno["nome"])
        aluno["nota"] = float(input("\nInsira a nova nota do aluno: "))
        salvar_dados()
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



carregar_dados()

while True:
    print("-------------------------------")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Calcular média de notas")
    print("4 - Listar alunos aprovados")
    print("5 - Buscar aluno pelo nome")
    print("6 - Editar nota do aluno")
    print("7 - Remover aluno")
    print("8 - Ativar / Desativar aluno")
    print("9 - Encerrar")
    print("-------------------------------")

    opcao = int(input("Insira sua opção: "))

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar_alunos()
    elif opcao == 3:
        media = calcular()
        if media is not None:
            print("\nA média das notas: ", media, "\n")
    elif opcao == 4:
        listar_aprovados()
    elif opcao == 5:
        buscar_nome()
    elif opcao == 6:
        editar_nota()
    elif opcao == 7:
        remover()
    elif opcao == 8:
        ativar_desativar()
    else:
        print("\nEncerrado! :)\n")
        break