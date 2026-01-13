import re

def validar_menu(texto):
    padrao = r"^[1-9]$"
    return bool(re.fullmatch(padrao, texto))
