from faker import Faker

faker = Faker('pt_BR')

nome = faker.name()
print(f"Nome: {nome}")

endereco = faker.address()
print(f"Endereço: {endereco}")

cpf = faker.cpf()
print(f"CPF: {cpf}")

telefone = faker.phone_number()
print(f"Telefone: {telefone}")

email = faker.email()
print(f"E-mail: {email}")

data_nascimento = faker.date_of_birth()
print(f"Data de Nascimento: {data_nascimento}")

nome_empresa = faker.company()
print(f"Nome da Empresa: {nome_empresa}")

cnpj = faker.cnpj()
print(f"CNPJ: {cnpj}")

endereco_empresa = faker.address()
print(f"Endereço da Empresa: {endereco_empresa}")

url = faker.url()
print(f"URL: {url}")

endereco_ip = faker.ipv4()
print(f"Endereço IP: {endereco_ip}")

cartao_credito = faker.credit_card_number()
print(f"Cartão de Crédito: {cartao_credito}")

validade_cartao = faker.credit_card_expire()
print(f"Validade do Cartão: {validade_cartao}")

codigo_seguranca = faker.credit_card_security_code()
print(f"Código de Segurança: {codigo_seguranca}")

latitude = faker.latitude()
longitude = faker.longitude()
print(f"Coordenadas: ({latitude}, {longitude})")

cidade = faker.city()
print(f"Cidade: {cidade}")

estado = faker.state()
print(f"Estado: {estado}")

pais = faker.country()
print(f"País: {pais}")

nome_produto = faker.word()
print(f"Nome do Produto: {nome_produto}")

preco_produto = faker.pricetag()
print(f"Preço do Produto: {preco_produto}")

descricao_produto = faker.sentence()
print(f"Descrição do Produto: {descricao_produto}")