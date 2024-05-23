"""
Invierte las llaves y los valores del diccionario que contiene los cuadrados, de tal manera que los cuadrados sean las llaves y los numeros originales sean los valores
"""


def main():
    dic ={x:x**2 for x in range(1,6)}
    otro_dic = {valor:k for k,valor in dic.items()}
    dic2 ={x**2:x for x in range(1,6)}

    print(dic)
    print(otro_dic)
    print(dic2)

main()







