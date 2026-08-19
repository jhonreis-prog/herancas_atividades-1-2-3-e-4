import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


class Livro(ItemBiblioteca):
    def __init__(self, titulo, codigo, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)

    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)

    def ver_historico(self):
        print(f"Usuário: {self.nome}")
        for item in self.itens_emprestados:
            print(item.titulo)

livro = Livro("Python", 1, "João", 300)

leitor = Usuario("João")

leitor.pegar_item(livro)
leitor.ver_historico()

leitor.devolver_item(livro)
leitor.ver_historico()