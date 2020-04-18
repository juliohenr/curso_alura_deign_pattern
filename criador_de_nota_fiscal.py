from datetime import date
from observadores import imprime,envia_por_email,salva_no_banco


class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal():

    def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes,observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens


        for i in observadores:

            i(self)



    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes





class Criador_de_nota_fiscal():

    def __init__(self):

        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__itens = None
        self.__detalhes = None

    def com_razao_social(self,razao_social):

        self.__razao_social = razao_social

        return self

    def com_cnpj(self,cnpj):

        self.__cnpj = cnpj

        return self

    def com_data_de_emissao(self,data_de_emissao):

        self.__data_de_emissao = data_de_emissao

        return self

    def com_itens(self,itens):

        self.__itens = itens

        return self

    def com_detalhes(self,detalhes):

        self.__detalhes = detahes

        return self

    def constroi(self):

        if self.__razao_social is None:

            raise Exception('Razão social deve ser preenchida')
        
        if self.__cnpj is None:

            raise Exception('CNPJ deve ser preenchido')

        if self.__itens is None:

            raise Exception('Itens devem se preenchidos')

        if self.__data_de_emissao is None:

            self.__data_de_emissao = date.today()

        
        if self.__detalhes is None:

            self.__detalhes = ''

        return Nota_fiscal(razao_social=self.__razao_social,
                            cnpj=self.__cnpj,
                            data_de_emissao=self.__data_de_emissao,
                            itens=self.__itens,
                            detalhes=self.__detalhes,observadores=[imprime,envia_por_email,salva_no_banco,salva_no_banco])



if __name__ == '__main__':

    nota_fiscal = (Criador_de_nota_fiscal()
                    .com_razao_social('qualquerRS')
                    .com_cnpj('747939763')
                    .com_data_de_emissao('12345')
                    .com_itens('0').constroi())