import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()  # Abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar()  # Método que realizar a conexão com o BD
        self.con = self.db_connection.cursor()  # Navegação no banco de dados

    def inserir(self, nome, telefone, endereco, dataDeNascimento, cpf, deficiencia, avaliacao, loval):
        try:
            sql = "insert into pessoa(codigo, nome, telefone,  endereco, dataDeNascimento, cpf, deficiencia, avaliacao, loval) values('', '{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, telefone,endereco, dataDeNascimento, cpf, deficiencia, avaliacao, loval)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Linha Afetada.".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)
            msg = ""

            for (codigo, nome, telefone, endereco, dataDeNascimento, cpf, deficiencia, avaliacao, loval) in self.con:
                msg = msg = "\nCódigo: {}, \nNome: {}, \nTelefone: {}, \nEndereço: {},\n Data de Nascimento: {}, \nCPF: {}, \nTipo de Deficiência: {}, \nAvaliaçãoo: {}, \nLocal: {}".format(codigo, nome, telefone, endereco, dataDeNascimento, cpf, deficiencia, avaliacao, loval)
            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro


    def excluir(self, cod):
        try:
            sql = "delete from  pessoa where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Linha Excluida".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def avaliar(self, cod, avaliacao, loval):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(avaliacao, loval, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "Avaliação Enviada com Sucesso!".format(self.con.rowcount)
        except Exception as erro:
            return erro

