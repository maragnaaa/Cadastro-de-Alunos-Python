import re

def validar_menu(texto):
    padrao_menu = r"^[1-5]$"
    return bool(re.fullmatch(padrao_menu, texto))

def validar_nome(texto):
    padrao_nome = r"^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$"
    return bool(re.fullmatch(padrao_nome, texto))

def validar_nota(texto):
    padrao_notas = r"^(10(\.0+)?|[0-9](\.\d+)?)$"
    return bool(re.fullmatch(padrao_notas, texto))