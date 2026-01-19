class Aluno:
    def __init__(self, nome, nota, ativo=True):
        if not nome.strip():
            raise ValueError("Nome inválido")

        if nota < 0:
            raise ValueError("Nota inválida")

        self.nome = nome
        self.nota = nota
        self.ativo = ativo

    def ativar_aluno(ativo):
        ativo = True

    def desativar_aluno(ativo):
        ativo = False

    def alterar_nota(self, nova_nota):
        if nova_nota < 0:
            raise ValueError("Nota inválida")      
        self.nota = nova_nota

    def to_dict(self):
        return {
            "nome": self.nome,
            "nota": self.nota,
            "ativo": self.ativo
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["nota"],
            dados["ativo"]
        )