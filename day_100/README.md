# Desafio 100

Desenvolvendo uma API de machine learning com FastAPI

## Explicação

### Ferramentas Utilizadas

- `FastAPI`: Framework para criação de APIs rápidas e eficientes.
- `pydantic`: Biblioteca para validação de dados.
- `joblib`: Biblioteca para serialização de objetos Python.
- `pandas`: Biblioteca para manipulação de dados.
- `sklearn`: Biblioteca para aprendizado de máquina.

### Funções Principais

- `FastAPI()`: Cria uma aplicação FastAPI.
- `BaseModel`: Classe base para definição de modelos de dados.
- `joblib.load()`: Carrega um modelo serializado.
- `app.post()`: Define um endpoint POST.

## Resultado

### Executando o modelo (DAY_100.PY)

```py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

base_path = os.path.abspath(os.path.dirname(__file__))
assets_path = os.path.join(base_path, 'assets')
model_path = os.path.join(assets_path, 'model.pkl')

modelo = joblib.load(model_path)
app = FastAPI()

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisData):
    df = pd.DataFrame([data.dict()])
    df.columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    
    pred = modelo.predict(df)
    
    classes = ['setosa', 'versicolor', 'virginica']
    result = classes[pred[0]]
    
    return {"prediction": result}
```
### Treinamento do Modelo (TRAIN_MODEL.PY)

```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

base_path = os.path.abspath(os.path.dirname(__file__))
assets_path = os.path.join(base_path, 'assets')
os.makedirs(assets_path, exist_ok=True)
model_path = os.path.join(assets_path, 'model.pkl')

# Carrega o conjunto de dados Iris
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treina o modelo de RandomForest
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Salva o modelo treinado
joblib.dump(modelo, model_path)
print(f"Modelo salvo em: {model_path}")
```