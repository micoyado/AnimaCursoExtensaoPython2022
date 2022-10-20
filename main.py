# para comentar em linha

# print() = comando de saída
print("Hello, World!\n")

# quando quiser guardar uma string (frase)
nome = "Milena Porto"

# quando quiser guardar um número inteiro
idade = 18

# exibir o que está dentro da variável nome
print("Meu nome é " + str(nome) + "\n")

# quando quiser exibir a frae "minha idade é " completando com o conteúdo da variável "idade"
print("Eu tenho " + str(idade) + " anos\n")

# agora os dois juntos!
print("Meu nome é " + nome + " e tenho " + format(idade) + " anos\n")

#usando o format() e {}
print ("Meu nome é {} e tenho {} anos" .format(nome, idade))