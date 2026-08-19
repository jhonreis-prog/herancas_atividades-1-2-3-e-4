import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

class Funcionario:
    def __init__(self, nome: str, cpf: str, salario: float):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    def aumentar_salario(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def exibir_dados(self):
        print(f"O Funcionario {self.nome} com o cpf {self.cpf} recebe o salário de {self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def receber_bonificacao(self):
        bonificacao = self.salario * 0.10
        self.salario += bonificacao
        print(f"Bonificação de R${bonificacao:.2f} recebida. Novo salário: R${self.salario:.2f}")

def main():
    print("testando")


joao = Funcionario("João Silva", "123.456.789-00", 2500.00)
joao.exibir_dados()
joao.aumentar_salario(10)
joao.exibir_dados()

if __name__ == "__main__":
    main()