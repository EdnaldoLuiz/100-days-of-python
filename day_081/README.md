# Desafio 81

Criando modelos preditivos simples com scikit-learn

## Explicação

### Ferramentas Utilizadas

- `numpy`: Biblioteca para computação numérica eficiente.
- `scikit-learn`: Biblioteca para aprendizado de máquina em Python.

### Funções Principais

- `train_test_split()`: Divide os dados em conjuntos de treino e teste.
- `LinearRegression()`: Cria um modelo de regressão linear.
- `model.fit()`: Treina o modelo com os dados de treino.
- `model.predict()`: Faz previsões com os dados de teste.
- `mean_squared_error()`: Calcula o erro quadrático médio.

## Resultado

```py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Dados de exemplo
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria o modelo de regressão linear
model = LinearRegression()

# Treina o modelo com os dados de treino
model.fit(X_train, y_train)

# Faz previsões com os dados de teste
y_pred = model.predict(X_test)

# Calcula o erro quadrático médio
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio: {mse}")

# Exibe as previsões
print(f"Previsões: {y_pred}")