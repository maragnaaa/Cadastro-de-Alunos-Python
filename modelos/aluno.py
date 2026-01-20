class Aluno:
    def __init__(self, nome, nota, estado):
        if not nome.strip():
            raise ValueError("Nome inválido")

        if nota < 0:
            raise ValueError("Nota inválida")

        self.nome = nome
        self.nota = nota
        self.estado = estado

    def ativar_aluno(self):
        self.estado = "ATIVO"

    def desativar_aluno(self):
        self.estado = "INATIVO"

    def pode_editar_nota(self):
        return self.estado == "ATIVO"

    def editar_nota(self, nova_nota):
        if not self.pode_editar_nota():
            print("Aluno inativo não pode alterar a nota")
            return
        if nova_nota < 0:
            raise ValueError("Nota inválida")      
        self.nota = nova_nota

    def to_dict(self):
        return {
            "nome": self.nome,
            "nota": self.nota,
            "estado": self.estado
        }
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["nome"],
            dados["nota"],
            dados["estado"]
        )