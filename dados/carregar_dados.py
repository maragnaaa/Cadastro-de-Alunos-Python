import json
from modelos.alunos import alunos

def carregar_dados():
    try:
        with open("dados/alunos.json", "r", encoding="utf-8") as arq:
            dados = json.load(arq)

        alunos.clear()
        alunos.extend(dados)

    except FileNotFoundError:
        alunos.clear()
    except json.JSONDecodeError:
        alunos.clear()