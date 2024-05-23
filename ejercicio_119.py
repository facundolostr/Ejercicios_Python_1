"""
Implemetar una clase Carta, que se crea a partir de un palo y un valor.
Las cartas deben poder implimirse de la forma <valor> de <palo>.
las cartas deben poder compararse entre ellas:
    Una carta vale menos que otra si al ser del mismo palo su valor es menor,
    o si al ser de distinto palos el propio es menor que el palo de la otra carta
    implementar una clase palo,
    que implementa los metodos __eq__, __str__y __lt__ 

"""

import random



class CartaPoker:

    PALOS = ("#","♥️","♦️","♣️","♠️")
    NUMEROS = ("#", "A","1","2","3","4","5","6","7","8", "9","10","J","Q","K")

    def isroja(self) ->bool:
        pass

    def isnegra(self) ->bool:
        pass

    def isas(self) ->bool:
        pass

    def __init__(self,numero:int,palo:int,tapada:bool=False) ->None:
        self.__numero:int = numero
        self.__palo:int = palo
        self.__tapada:bool = tapada

    def get_numero(self) -> int:
        return self.__numero

    def get_palo(self) -> int:
        return self.__palo

    def istapada(self) -> bool:
        return self.__tapada

    def tapar(self) -> None:
        self.__tapada = True

    
    def destapar(self) -> None:
        self.__tapada = False

    def dar_vuelta (self) -> None:
        self.__tapada = not self.__tapada

    def __eq__ (self, __value:object) ->bool:
        if __value is None or not isinstance(__value,CartaPoker):
            return False

        return self.get_numero() == __value.get_numero() and self.get_palo == __value.get_palo()

    def __str__(self) ->str:
        if self.istapada():
            cadena = f"[{CartaPoker.NUMEROS[0]}][{CartaPoker.PALOS[0]}]"            
        else:
            cadena = f"[{CartaPoker.NUMEROS[self.get_numero()]}][{CartaPoker.PALOS[self.get_palo()]}]"
        return cadena

    def __ne__ (self, __value:object) -> bool:
        return not self.__eq__ (__value)



class MazoPoker:
    def __init__ (self,con_cartas:bool=False, tapado:bool=False) ->None:
        self.__cartas:list[CartaPoker] = []
        if con_cartas:
            self.llenar(tapado)

    def __len__ (self) -> int:
        return len(self.__cartas)

    def isvacio (self) ->bool:
        return len(self) == 0

    def poner_carta(self,carta:CartaPoker,index:int=None) -> None:

        if carta is None or not isinstance(carta, CartaPoker):
            raise ValueError(f"{carta} No es una CartaPoker")
        if index:
            self.__cartas.insert(index,carta)
        else:
            self.__cartas.append(carta)

    def sacar_carta(self,index:int=None) -> None:
        if index:
            return self.__cartas.pop(index)
        return self.__cartas.pop(0)

    def llenar(self, tapado:bool=False) -> None:
        if len(self) > 0:
            self.__cartas.clear()

        for n in range(1,14):
            for p in range (1,5):
                self.poner_carta(CartaPoker(n,p,tapado))

    def barajar(self) -> None:
        random.shuffle(self.__cartas)

    def cortar(self) -> None:
        posicion = random.randint(0,len(self)-1)
        pass

    def __str__ (self) -> str:
        return ', '.join( [str(carta) for carta in self.__cartas] )


def main():

    m = MazoPoker(con_cartas=True)
    print(f'Mazo: {str(m)}\n')
    m.barajar()
    print(f'Mazo: {str(m)}\n')


main()