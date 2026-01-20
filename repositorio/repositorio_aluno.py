class RepositorioAlunos:
    def __init__(self, persistencia):
        self.persistencia = persistencia
        self.alunos = self.persistencia.carregar_alunos()

    def buscar_por_nome(self, nome):
        nome = nome.strip().lower()
        for aluno in self.alunos:
            if aluno.nome.lower() == nome:
                return aluno
        return None
    
    def adicionar_aluno(self, aluno):
        if self.buscar_por_nome(aluno.nome):
            raise ValueError("Aluno já cadastrado")
        self.alunos.append(aluno)
        self.persistencia.salvar_alunos(self.alunos)

    def remover_aluno(self, nome):
        aluno = self.buscar_por_nome(nome)
        if not aluno:
            raise ValueError("Aluno não encontrado")
        self.alunos.remove(aluno)
        self.persistencia.salvar_alunos(self.alunos)

    def calcular_media(self):
        soma = 0
        contador = 0

        for aluno in self.alunos:
            if aluno.participa_da_media():
                soma += aluno.nota
                contador += 1

        if contador == 0:
            return None
        
        return soma / contador
    
    def listar_aprovados(self):
        return [a for a in self.alunos if a.nota >=6]