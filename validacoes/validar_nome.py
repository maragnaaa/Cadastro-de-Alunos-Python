import re

def validar_nome(texto):
    padrao = r"^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$"
    return bool(re.fullmatch(padrao, texto))