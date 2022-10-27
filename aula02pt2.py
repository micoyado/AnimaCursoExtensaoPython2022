#pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "{nome}, você é bichão, mesmo..."
nome = input("• Usuário, informe o seu nome: ")
nota = float(input(f"\n• {nome}, digite sua nota: "))

if (nota == 10):
  print(f"\n{nome}, você é o bichão mesmo! Parabéns e continue estudando :D")

elif (nota >= 6 and nota < 10):
  print(f"\n{nome}, bom trabalho! Mas sei que você consegue melhorar :)")

else:
  print(f"\n{nome}, essa nota não está legal :/")