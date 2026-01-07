def validar_aluno(nome, alunos):
    nome = nome.strip().lower()

    for aluno in alunos:
        nome_salvo = aluno["nome"].strip().lower()
        if nome == nome_salvo:
            return True
    
    return False
