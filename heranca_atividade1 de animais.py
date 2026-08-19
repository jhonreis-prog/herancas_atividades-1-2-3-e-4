class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print("O animal fez um som")

    def __str__(self):
        return (f"O(a) {self.nome} da raça {self.raca} fez um som")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "Canino")
        self.nome = nome
        self.raca = raca

    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "Felino")
        self.nome = nome
        self.raca = raca

    def fazer_som():
        print("Miau !")

class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "Bovino")
        self.nome = nome
        self.raca = raca

    def fazer_som():
        print("Muuuu")



cachorro = Cachorro("Bug", "Pinscher")
gato = Gato("Mel", "Sphynx")
vaca = Vaca("Bernadete", "Nelore")

print(cachorro)
print(gato)
print(vaca)