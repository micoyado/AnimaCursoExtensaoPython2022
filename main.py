#comando input(): quero permitir que o usuário digite algo
nome = input("Usuário, digite o seu nome: ")

#pede a idade para o usuário
idade = int(input("\nUsuário, digite a sua idade: "))

#comando de saída (exibir na tela nome do usuário)
print(f"\nOi, seu nome é {nome}")

#comando de saída (exibir na tela idade do usuário)
print(f"\n{nome}, sua idade é {idade}")

#e se eu quisesse mostrar o dobro da idade informada?
dobro = idade * 2
print(f"\nO dobro da sua idade é {dobro}")