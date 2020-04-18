from impostos import ICMS,ISS,ICPP,IKCV


class Calculador_de_impostos():

    def realiza_calculo(self,orcamento,imposto):


        imposto_calculado = imposto.calcula(orcamento)


        print(imposto_calculado)


if __name__=='__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()

    orcamento.adiciona_item(Item('item1',50))
    orcamento.adiciona_item(Item('item2',200))
    orcamento.adiciona_item(Item('item3',250))

    calculador = Calculador_de_impostos()


    calculador.realiza_calculo(orcamento,ISS())
    calculador.realiza_calculo(orcamento,ICMS())

    print('ISS e ICMS')

    calculador.realiza_calculo(orcamento,ISS(ICMS()))

    calculador.realiza_calculo(orcamento,ICPP())
    calculador.realiza_calculo(orcamento,IKCV())


    print('ICPP e IKCV')

    calculador.realiza_calculo(orcamento,ICPP(IKCV()))