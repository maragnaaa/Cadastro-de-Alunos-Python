import re

def validar_nota(texto):
    padrao = r"^(10(\.0+)?|[0-9](\.[0-9]+)?)$"
    return bool(re.fullmatch(padrao, texto))
