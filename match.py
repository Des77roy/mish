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

op=0
total=0
while op!=4:
    print("1.- Xbox Series S $250.000")
    print("2.- Sony PS5 $ $500.000")
    print("3.- LGTV 60 Pulgadas $600.000")
    print("4.- Salir")
    op=int(input("Seleccione una opcion: "))

    match op:
        case 1:
            print("El valor a pagar ", 250000*1.19)
            total+=250000*1.19
        case 2:
            print("El valor a pagar ", 500000*1.19)
            total+=500000*1.19
        case 3:
            print("El valor a pagar ", 600000*1.19)
            total+=600000*1.19
        case 4:
            print("saliendo")
            print(f"tu valor a pagar es: ", total )
        case _:
            print("Opcion Invalida")