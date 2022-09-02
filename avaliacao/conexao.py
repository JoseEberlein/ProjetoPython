import mysql.connector #Elemento que faz a conexão com o Banco de Dados
from mysql.connector import errorcode

class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost',
                                                         user='root',
                                                         password='',
                                                         database='saal')
            print('Conectado com sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o banco de dados não exista!
                print('Banco de dados não existe!\n Erro: {}'.format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Há um erro de usuário
                print('Nome de usuário ou senha invalido! \n Erro: {}'.format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close() #Fechando a conexão com o banco de dados