# entrada de dados
print("Bem vindo ao Trem Fantasma!!!")

nome = input("Informe o nome:")
idade = int(input("Informe a idade:"))
peso = float(input("Informe seu peso:"))

# autorizar a entrada no parque
if idade >= 10 and peso <= 150:
    print(f"{nome} bem vindo, pode entrar")
else:
    print(f"{nome} desculpe, você não pode entrar!")