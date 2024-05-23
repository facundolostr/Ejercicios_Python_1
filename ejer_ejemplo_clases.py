"""
Implementar la clase caramelera, que recibe en su constructor la cantidad de caramelos que puede contener, y tiene el siguiente comportamiento:

c = Caramelera(20)
c.poner_caramelos(10)
c.sacar_caramelos(4)
c.caramelos()

print(c)
"caramelera con 6/20 caramelos



"""


class Caramelera:
    def __init__(self, capacidad:int) -> None:
        if capacidad is None or not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("la capacidad de la caramelera esta mal o no esta!")
        self.__capacidad = capacidad
        self.__cantidad = 0

    def __hay_lugar(self,cantidad:int) -> bool:
        return cantidad <= self.__capacidad - self.__cantidad

    def poner_caramelos(self, cantidad:int)-> None:
        if cantidad is None or not isinstance(cantidad,int) or not self.__hay_lugar(cantidad):
            raise ValueError("No queda lugar para tantos caramelos")
        self.__cantidad += cantidad

    def sacar_caramelos(self, cantidad:int)-> None:
        if cantidad is None or not isinstance(cantidad,int):
            raise ValueError("la cantidad esta mal o no esta!")
        else:
            if cantidad > self.__cantidad:
                raise ValueError("No quedan tantos caramelos")
            else:
                self.__cantidad -= cantidad

    def __str__(self) -> str:
        return f"Caramelera con {self.__cantidad}/{self.__capacidad} caramelos"

def main():
    c = Caramelera(10)

    try:

        c.poner_caramelos(5)
        c.sacar_caramelos(25)

    except ValueError as e:
        print(f"Error: {e}")

    else:
        print(c)


if __name__ == '__main__':
    main()