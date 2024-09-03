import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

print(f'Coeficiente: {model.coef_[0]}')
print(f'Intercepto: {model.intercept_}')

for i, (pred, actual) in enumerate(zip(y_pred, y_test)):
    print(f'Previsão {i+1}: {pred:.2f}, Valor Real: {actual}')