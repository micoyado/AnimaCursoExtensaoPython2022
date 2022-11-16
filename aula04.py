#1o passo: importar a biblioteca sqlite3
import sqlite3

#2o passo: vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3o passo = criar um objeto do tipo cursor
cursor = conexao.cursor