import os

os.environ['MY_VARIABLE'] = 'some_value'

my_variable = os.environ.get('MY_VARIABLE')
print(f"MY_VARIABLE: {my_variable}")

if 'MY_VARIABLE' in os.environ:
    print("MY_VARIABLE está definida")

del os.environ['MY_VARIABLE']

my_variable = os.environ.get('MY_VARIABLE')
print(f"MY_VARIABLE após remoção: {my_variable}")