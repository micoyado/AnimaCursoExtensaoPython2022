#comando input(): quero permitir que o usuário digite algo
nome = input("• Usuário, digite o seu nome: ")

#pede a idade para o usuário
idade = int(input(f"\n• {nome}, digite a sua idade: "))

#comando de saída (exibir na tela nome do usuário)
print(f"\nEntão... seu nome é {nome}!")

#comando de saída (exibir na tela idade do usuário)
print(f"{nome}, sua idade é {idade}, certo?")

#e se eu quisesse mostrar o dobro da idade informada?
dobro = idade * 2
print(f"Olha que legal! O dobro da sua idade é {dobro}...")

#estrutura condicional - o famoso "if/else"
#se a pessoa for maior de idade, mostre "você é maior de idade, ótimo!"
if idade >= 18: 
  print("E você é maior de idade! Já pode beber e dirigir :D")

else:
  print("Você ainda é menor de idade, ou seja: vá já para a cama!")

#e se eu quisesse perguntar o gênero (m - masculino e f - feminino)
#mostre e informe se precisa mostrar ou não o serviço militar obrigatório  
  
genero = input(f"\n• {nome}, informe o seu gênero sendo F = Feminino, M = Masculino e O = Outros: ")

if  idade >=18 and genero == "M":
  print("\nVocê é homem e tem mais de 18 anos, então precisa se alistar!")

else:
  print("\nO serviço militar não é obrigatório para mulheres ou outros, então você não precisa se alistar!")
