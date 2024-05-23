"""
Escribir la clase Partido, que recibe en el constructor dos cadenas que corresponde al nombre del equipo local y el visitante (en ese orden).

ademas, tiene los siguientes metodos:

Cargar_resultado: Recibe dos numeros enteros, que corresponden a los goles convertidos po el local y el visitante (en ese orden).

obtener_ganador: Devuelve el nombre del equipo ganador, o None si hubo un empate.
obtener_perdedor: Similar a obtener_ganador, pero devuelve el perdedor o None

Cargar partido: Recibe un objeto de clase Partido, y guarda los datos necesarios.

obtener_campeon: Devuelve una cadena con el nombre del equipo que mas puntos tiene. Si hay varios equipos que tengan el puntaje maximo, devolver el nombre de cualquiera de ellos.
Se otorgan 3 puntos por partido ganado, 1 po partido empatado y 0 por partido perdido.
Este metodo debe ser lo mas eficiente posible

"""


class Partido:
    pass




class Liga:
    def __init__ (self, nombre) -> None:
        self.__nombre = nombre
        self.__partidos = []

    def agregar_partido(self, partido) -> None:
        self.__partidos.append(partido)




def main():
    pass



main()



