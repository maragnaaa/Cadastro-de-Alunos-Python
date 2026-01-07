import json
from modelos.alunos import alunos

def salvar_dados():
    with open("dados/alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4, ensure_ascii=False)