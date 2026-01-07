import re

def validar_status(texto):
    padrao = r"^[sSnN]$"
    return bool(re.fullmatch(padrao, texto))