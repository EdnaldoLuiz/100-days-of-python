# Desafio 82

Trabalhando com pipelines de machine learning

## Explicação

### Ferramentas Utilizadas

- `numpy`: Biblioteca para computação numérica eficiente.
- `scikit-learn`: Biblioteca para aprendizado de máquina em Python.

### Funções Principais

- `load_iris()`: Carrega o conjunto de dados Iris.
- `train_test_split()`: Divide os dados em conjuntos de treino e teste.
- `Pipeline()`: Cria um pipeline de machine learning.
- `StandardScaler()`: Normaliza os dados.
- `KNeighborsClassifier()`: Cria um modelo de classificação KNN.
- `accuracy_score()`: Calcula a acurácia do modelo.

## Resultado

```py
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carrega o conjunto de dados Iris
iris = load_iris()
X, y = iris.data, iris.target

# Adiciona ruído aos dados
np.random.seed(42)
noise = np.random.normal(0, 0.5, X.shape)
X_noisy = X + noise

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_noisy, y, test_size=0.2, random_state=42)

# Cria um pipeline de machine learning
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=3))
])

# Treina o modelo com os dados de treino
pipeline.fit(X_train, y_train)

# Faz previsões com os dados de teste
y_pred = pipeline.predict(X_test)

# Calcula a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy}")

# Exibe as previsões
print(f"Previsões: {y_pred}")