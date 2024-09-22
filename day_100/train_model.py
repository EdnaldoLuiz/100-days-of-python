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

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

joblib.dump(modelo, model_path)
print("Modelo treinado e salvo como 'model.pkl'")