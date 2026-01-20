import json
from modelos.aluno import Aluno

class AlunoJSON:
    def __init__(self, caminho):
        self.caminho = caminho

    def salvar_alunos(self, alunos):
        with open(self.caminho, "w", encoding="utf-8") as arq:
            json.dump([a.to_dict() for a in alunos], arq, indent=4)

    def carregar_alunos(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                return [Aluno.from_dict(d) for d in dados]
        except FileNotFoundError:
            return []