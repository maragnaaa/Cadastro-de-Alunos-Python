import json
from cadastrar_alunos import alunos

def salvar_dados():
    with open("alunos.json", "w") as arq:
        json.dump(alunos, arq)