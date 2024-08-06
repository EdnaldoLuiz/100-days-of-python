import re

padrao = r"\b\d{3}\b"

texto = "123 456 789 101112 131415 161718 192021"

resultados = re.findall(padrao, texto)
print(resultados)

substituicao = "XXX"
resultado = re.sub(padrao, substituicao, texto)
print(resultado)