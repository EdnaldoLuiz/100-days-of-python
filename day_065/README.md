# Desafio 65

Criando testes automatizados com a biblioteca `unittest`

## Explicação

### Ferramentas Utilizadas

- `unittest`: Biblioteca padrão do Python para criação de testes automatizados.

### Funções Principais

- `unittest.TestCase`: Classe base para criação de testes.
- `self.assertEqual()`: Verifica se dois valores são iguais.
- `unittest.main()`: Executa os testes.

## Resultado

```py
import unittest

def soma(a, b):
    return a + b

class Testes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(2, 2), 4)
        self.assertEqual(soma(3, 2), 5)

if __name__ == '__main__':
    unittest.main()