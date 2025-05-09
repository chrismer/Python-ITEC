# funcion para agregar alumnos, 3 notas (0 al 10) y su promedio
# Determinar si el estudiante aprueba o desaprueba. Se aprueba con un promedio mayor o igual a 6
# Mostrar un mensaje como este:
# "El estudiante Juan tiene un promedio de 7.33 y está aprobado."
# El código debe ser modular y utilizar funciones con parámetros y retornos adecuados.

def agregar_alumno(nombre, notas):
    promedio = sum(notas) / len(notas)
    estado = "aprobado" if promedio >= 6 else "desaprobado"
    return f"El estudiante {nombre} tiene un promedio de {promedio:.2f} y está {estado}."

def solicitar_notas():
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 0 y 10.")
            except ValueError:
                print("Error: debe ingresar un número válido.")
    return notas

def main():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if not nombre.replace(" ", "").isalpha():
            print("Error: el nombre solo puede contener letras y espacios.")
            continue
        
        notas = solicitar_notas()
        resultado = agregar_alumno(nombre, notas)
        print(resultado)
        
        while True:  # Bucle para validar la respuesta del usuario
            continuar = input("¿Desea agregar otro estudiante? (si/no): ").strip().lower()
            if continuar == "si":
                break  # Sale del bucle y continúa con el siguiente estudiante
            elif continuar == "no":
                print("Gracias por usar el sistema de notas.")
                return  # Termina el programa
            else:
                print("Respuesta no válida. Por favor, escriba 'si' o 'no'.")

print("Gracias por usar el sistema de notas.")

if __name__ == "__main__":
    main()