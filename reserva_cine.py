# Crear matriz asientos[3][4]
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Escribir "Ingrese fila (0 a 2):"
f = int(input("Ingrese fila (0 a 2): "))

# Escribir "Ingrese columna (0 a 3):"
c = int(input("Ingrese columna (0 a 3): "))

# asientos[f][c] = 1
asientos[f][c] = 1

# Escribir "Estado de la sala:"
print("Estado de la sala:")

# Para i desde 0 hasta 2
for i in range(3):

    # Para j desde 0 hasta 3
    for j in range(4):

        # Escribir asientos[i][j] sin salto de línea
        print(asientos[i][j], end=" ")

    # Escribir salto de línea
    print()
    
    