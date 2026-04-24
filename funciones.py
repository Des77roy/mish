a = float(input("Primer número: "))
b = float(input("Segundo número: "))

print("\n¿Qué operación deseas realizar?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("\nSelecciona una opción (1-4): ")


if opcion == '1':
    print(f"Resultado de la Suma: {a + b}")
elif opcion == '2':
    print(f"Resultado de la Resta: {a - b}")
elif opcion == '3':
    print(f"Resultado de la Multiplicación: {a * b}")
elif opcion == '4':
    if b != 0:
        print(f"Resultado de la División: {a / b}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, intenta de nuevo.")