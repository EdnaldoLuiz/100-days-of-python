def calculadora(expressao):
    """
    Calcula o resultado de uma expressão matemática.
    """
    try:
        resultado = eval(expressao)
    except (NameError, SyntaxError, ZeroDivisionError) as e:
        resultado = f"Erro: {e}"
    return resultado

if __name__ == '__main__':
    expressao = input("Digite uma expressão matemática: ")
    resultado = calculadora(expressao)
    print(f"Resultado: {resultado}")