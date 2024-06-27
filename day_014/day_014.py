class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def __str__(self):
        return f"{self.nome} é um animal da raça {self.raca}"

class Cachorro (Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca)
        self.idade = idade

    def __str__(self):
        return f"{self.nome} é um cachorro da raça {self.raca} e tem {self.idade} anos"
    
class Gato (Animal):
    def __init__(self, nome, raca, idade):
        super().__init__(nome, raca)
        self.idade = idade

    def __str__(self):
        return f"{self.nome} é um gato da raça {self.raca} e tem {self.idade} anos"
    
if __name__ == '__main__':
    cachorro = Cachorro("Rex", "Pastor Alemão", 5)
    gato = Gato("Bichano", "Siamês", 3)
    
    print(cachorro)
    print(gato)