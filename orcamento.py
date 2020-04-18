from abc import ABC, abstractmethod

class Etado_de_um_orcamento(ABC):


    @abstractmethod
    def aplica_desconto_extra(self,orcamento):
        pass

    @abstractmethod
    def aprova(self,orcamento):
        pass

    @abstractmethod
    def reprova(self,orcamento):
        pass

    @abstractmethod
    def finaliza(self,orcamento):
        pass


class Em_aprovacao(Etado_de_um_orcamento):

    def aplica_desconto_extra(self,orcamento):

        orcamento.adiciona_desconto_extra(orcamento.valor*0.02)

    def aprova(self,orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self,orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self,orcamento):
        raise Exception('Orçamento em aprovação não pode ser finalizado!')



class Aprovado(Etado_de_um_orcamento):

    def aplica_desconto_extra(self,orcamento):

        orcamento.adiciona_desconto_extra(orcamento.valor*0.05)

    def aprova(self,orcamento):
        raise Exception('Orçamento já está aprovado!')

    def reprova(self,orcamento):
        raise Exception('Orçamento já está aprovado não pode ser reprovado!')

    def finaliza(self,orcamento):
        orcamento.estado_atual = Finalizado()





class Reprovado(Etado_de_um_orcamento):

    def aplica_desconto_extra(self,orcamento):

        raise Exception('Orçamentos Reprovados!')    


    def aprovado(self,orcamento):
        raise Exception('Orçamento está reprovado!')

    def reprovado(self,orcamento):
        raise Exception('Orçamento já está reprovado!')

    def finalizado(self,orcamento):
        orcamento.estado_atual = Finalizado()



class Finalizado(Etado_de_um_orcamento):

    def aplica_desconto_extra(self,orcamento):

        raise Exception('Orçamentos Finalizados!')    


    def aprova(self,orcamento):
        raise Exception('Orçamento está finalizado!')

    def reprova(self,orcamento):
        raise Exception('Orçamento está finalizado!')

    def finaliza(self,orcamento):
        raise Exception('Orçamento já está finalizado!')


class Orcamento():
    
    def __init__(self):

        self.__itens = []

        self.estado_atual = Em_aprovacao()

        self.__desconto_extra = 0

    def aprova(self):

        self.estado_atual.aprova(self)

    def reprova(self):

        self.estado_atual.reprova(self)

    def finaliza(self):

        self.estado_atual.finaliza(self)

    
    def aplica_desconto_extra(self):

        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self,desconto):

        self.__desconto_extra += desconto

    @property
    def valor(self):

        total = 0

        for item in self.__itens:

            total+=item.valor

        return total - self.__desconto_extra

    
    def obter_itens(self):

        return tuple(self.__itens)


    @property
    def total_itens(self):

        return len(self.__itens)


    def adiciona_item(self,item):

        self.__itens.append(item)


    
class Item():

    def __init__(self,nome,valor):

        self.__nome = nome

        self.__valor = valor

    @property
    def valor(self):

        return self.__valor

    @property
    def nome(self):

        return self.__nome


if __name__ == '__main__':

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('item1',100))
    orcamento.adiciona_item(Item('item2',50))
    orcamento.adiciona_item(Item('item3',400))

    #orcamento.aplica_desconto_extra()
    print(orcamento.valor)
    orcamento.aprova()
    orcamento.reprova()