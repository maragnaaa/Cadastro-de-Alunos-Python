import re

def validar_menu(texto):
    padrao = r"^[1-5]$"
    return bool(re.fullmatch(padrao, texto))
