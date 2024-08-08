import decimal

decimal.getcontext().prec = 4

numero_1 = decimal.Decimal('1.1')
numero_2 = decimal.Decimal('2.2')
resultado = numero_1 + numero_2
print(resultado)

numero_3 = decimal.Decimal('3.3536')
resultado = numero_1 + numero_3
print(resultado)