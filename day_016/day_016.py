import re 

email = 'contatoednaldoluiz@gmail.com'

padrao = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,6}$'

if re.match(padrao, email):
    print('E-mail válido!')
else:
    print('E-mail inválido!')

telefone = '1199999-9999'

padrao = r'^\(?[1-9]{2}\)? ?9?[0-9]{4}-?[0-9]{4}$'

if re.match(padrao, telefone):
    print('Número de telefone válido!')
else:
    print('Número de telefone inválido')