import aula04pt3 as bd

con, cur = bd.conectar()

nome = input ("Informe o nome do herói/vilão: ")
nome_civil = input ("Informe o nome civil do herói/vilão (sua id. secreta): ")
tipo_numerico: input ("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

#consulta para o valor máximo usado no banco
sql = "SELECT MAX (pessoa_id) FROM pessoa"
cur.execute (sql)
cut.fetchone()
numero = cur.fetchone() [0]

if tipo_numerico =="1":
  tipo = "Herói(na)"

else:
  tipo: "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cur.execute(sql)
con.commit()
con.close()