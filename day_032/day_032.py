def funcao(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

funcao(1, 2, 3, a=4, b=5)