def decorator(funcao):
    def wrapper():
        print("Antes da função decorada")
        funcao()
        print("Depois da função decorada")
    return wrapper

@decorator
def funcao_decorada():
    n = 2 + 2
    print(f"Resultado: {n}")

funcao_decorada()