import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

np.random.seed(42)
noise = np.random.normal(0, 0.5, X.shape)
X_noisy = X + noise

X_train, X_test, y_train, y_test = train_test_split(X_noisy, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=3))  
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Precisão: {accuracy:.2f}')

for i, (pred, actual) in enumerate(zip(y_pred, y_test)):
    print(f'Previsão {i+1}: {iris.target_names[pred]}, Valor Real: {iris.target_names[actual]}')