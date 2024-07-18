# Desafio 34

Implementando uma calculadora de expressões matemáticas usando `eval`

## Explicação

### Ferramentas Utilizadas

- `eval()`: Função padrão do Python para avaliar expressões Python a partir de uma string.

### Funções Principais

- `eval(expressao)`: Avalia a expressão matemática fornecida como string.
- `try`/`except`: Bloco para capturar e lidar com exceções.

## Resultado

```py
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