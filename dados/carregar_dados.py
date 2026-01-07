import json

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r") as arq:
            alunos = json.load(arq)
    except FileNotFoundError:
        alunos = []