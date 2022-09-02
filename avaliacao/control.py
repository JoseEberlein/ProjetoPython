from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n" +
              "\n0. Sair" +
              "\n1. Cadastrar" +
              "\n2. Consultar Avaliações" +
              "\n3. Atualizar Nome" +
              "\n4. Atualizar telefone" +
              "\n5. Atualizar endereco" +
              "\n6. Atualizar data de nascimento" +
              "\n7. Atualizar cpf" +
              "\n8. Atualizar deficiência" +
              "\n9. Registrar avaliação" +
              "\n10. Excluir"
              )
        self.setOpcao(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()
            elif self.getOpcao() == 4:
                self.atualizarTelefone()
            elif self.getOpcao() == 5:
                self.atualizarEndereco()
            elif self.getOpcao() == 6:
                self.atualizarData()
            elif self.getOpcao() == 7:
                self.atualizarCpf()
            elif self.getOpcao() == 8:
                self.atualizarDeficiencia()
            elif self.getOpcao() == 9:
                self.registrarAvaliacao()
            else:
                print("Opção escolhida invalida! Tente novamente!")

    def cadastrar(self):
        print("Informe o seu nome: ")
        nome = input()
        print("Informe seu telefone: ")
        telefone = input()
        print("Informe o seu endereço: ")
        endereco = input()
        print("Informe a sua data de nascimento: ")
        dataDeNascimento = input()
        print("Informe o seu cpf: ")
        cpf = input()
        print("Informe sua deficiencia: ")
        deficiencia = input()
        print("Escreva sua primeira avaliação")
        avaliacao = input()
        print("Informe o local onde esteve.")
        loval = input()

        print(self.modelo.inserir(nome, telefone, endereco,self.transformarData(dataDeNascimento), cpf, deficiencia, avaliacao, loval))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo nome")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))


    def atualizarTelefone(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo telefone: ")
        tel = input()
        print(self.modelo.atualizar("telefone", tel, codigo))

    def atualizarEndereco(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo endereço: ")
        end = input()
        print(self.modelo.atualizar("endereco", end, codigo))

    def atualizarData(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe a nova data: ")
        data = self.transformarData(input())
        print(self.modelo.atualizar("dataDeNascimento", data, codigo))

    def atualizarCpf(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe o novo cpf")
        cp = input()
        print(self.modelo.atualizar("cpf", cp, codigo))

    def atualizarDeficiencia(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe a deficiência: ")
        defi = input()
        print(self.modelo.atualizar("deficiencia", defi, codigo))

    def registrarAvaliacao(self):
        print("Digite seu código para fazer uma nova avalição do último local que visitou!!")
        codigo = int(input())
        print("Local onde Esteve:")
        loval = input()
        print("Deixe sua avaliação:")
        avaliacao = input()
        print(self.modelo.avaliar(codigo, avaliacao, loval))

    def excluir(self):
        print("Informe o código do dado que deseja excluir: ")
        cod = int(input())
        print(self.modelo.excluir(cod))