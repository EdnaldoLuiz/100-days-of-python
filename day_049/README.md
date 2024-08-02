# Desafio 49

Trabalhando com números complexos e operações matemáticas avançadas

## Explicação

### Ferramentas Utilizadas

- `cmath`: Biblioteca padrão do Python para operações matemáticas com números complexos.

### Funções Principais

- `cmath.rect(r, phi)`: Converte coordenadas polares para um número complexo.
- `cmath.polar(z)`: Converte um número complexo para coordenadas polares.
- `cmath.phase(z)`: Retorna o ângulo de fase de um número complexo.
- `cmath.sqrt(z)`: Calcula a raiz quadrada de um número complexo.

## Resultado

```py
import cmath

# Converte coordenadas polares para um número complexo
z = cmath.rect(2, cmath.pi / 2)
print(z)

# Converte um número complexo para coordenadas polares
polar = cmath.polar(z)
print(polar)

# Retorna o ângulo de fase de um número complexo
fase = cmath.phase(z)
print(fase)

# Calcula a raiz quadrada de um número complexo
raiz = cmath.sqrt(z)
print(raiz)