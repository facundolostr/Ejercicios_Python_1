"""
Calcula el precio promedio de los productos para cada una de las categorias

"""

import sys
sys.path.insert(0,'resourses/')
import datos

def obtener_promedio_por_categoria(lista_prductos):
    dic = {}

    #("2001", "Leche", 1.20, "ref")

    for _, _, precio, categoria in lista_productos:
        if categoria in dic.keys():
            dic[categoria]['suma'] += precio
            dic[categoria]['contador'] += 1
        else:
            dic[categoria] = {'suma':precio,'contador':1}

    for categoria, info in dic.items():
        dic[categoria] = info['suma']/info['contador']

    return dic




def main():

    lista_prductos = datos.ARTICULOS_ALMACEN[:]

    for categoria,promedio in obtener_promedio_por_categoria(lista_productos).items():
        print(f"{categoria:5} ${promedio:10.2}")



main()

