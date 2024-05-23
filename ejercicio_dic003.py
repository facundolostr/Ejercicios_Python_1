


import sys
sys.path.insert(0,'resourses/')
import datos

def obtener_dic(lista):
    dic = {}
    #("2001", "Leche", 1.20, "ref")
    for _ , nombre , _ ,categoria in lista:
        if categoria in dic.keys():
            dic[categoria].append(nombre)
        else:
            dic[categoria] = [nombre]
    return dic


def main():
    lista_productos = datos.ARTICULOS_ALMACEN[:]
    dic = obtener_dic(lista_productos)
    for cat,lista in dic.items():
        print(f"Categoria: {cat}" )
        for nombre in lista:
            print(f"--{nombre}")


main()