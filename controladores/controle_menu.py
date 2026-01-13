import servicos.cadastrar_alunos as cadastrar_alunos 
import servicos.listar_alunos as listar_alunos 
import servicos.calcular as calcular 
import servicos.listar_aprovados as listar_aprovados
import servicos.buscar_nome as buscar_nome
import servicos.editar_nota as editar_nota
import servicos.remover as remover
import servicos.ativar_desativar as ativar_desativar

def opcao_3():
    media = calcular.calcular()
    if media is not None:
        print("\nA média das notas: ", media, "\n")

opcoes_menu = {
    1: cadastrar_alunos.cadastrar_alunos,
    2: listar_alunos.listar_alunos,
    3: opcao_3,
    4: listar_aprovados.listar_aprovados,
    5: buscar_nome.buscar_nome,
    6: editar_nota.editar_nota,
    7: remover.remover,
    8: ativar_desativar.ativar_desativar
}

def executar_opcao(opcao):
    acao = opcoes_menu.get(opcao)

    if acao:
        acao()
        return True
    
    return False