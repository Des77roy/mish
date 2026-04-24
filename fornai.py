# v1=0
# v2=0

# v=int(input("cual es la cantidad de votantes :"))
# for i in range(v):
#     voto=int(input(f"por quien votara. 1.candidato 2.Candidato "))
#     if voto==1:
#         v1+=1
#     elif voto==2:
#         v2+=1
#     else:
#         print("voto no valido")
# if v1>v2:
#     print("gano candidato 1")
# else:
#     print("gano el candidato 2")


# print("1.- Opcion 1")
# print("2.- Opcion 2")
# print("3.- Opcion 3")
# op=int(input("Seleccione una opcion: "))
# match op:
#     case 1:
#         print("Seleccionó la opcion 1")
#     case 2:
#         print("Seleccionó la opcion 2")
#     case 3:
#         print("Seleccionó la opcion 3")
#     case _:
#         print("Opcion Invalida")



print("1.- Xbox Series S $250.000")
print("2.- Sony PS5 $ $500.000")
print("3.- LGTV 60 Pulgadas $600.000")
op=int(input("Seleccione una opcion: "))

match op:
    case 1:
        print("El valor a pagar ", 250000*1.19)
    case 2:
        print("El valor a pagar ", 500000*1.19)
    case 3:
        print("El valor a pagar ", 600000*1.19)
    case _:
        print("Opcion Invalida")