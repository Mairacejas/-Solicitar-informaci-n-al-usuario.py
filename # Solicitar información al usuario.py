# Solicitar información al usuario
nombre = input("maira")
edad = int(input("32"))
altura = float(input("Ingrese su altura en metros: "))
tiene_mascota = input("¿Tiene mascota? (sí/no): ").strip().lower() == "sí"

# Mostrar los datos ingresados
print("\n--- Información ingresada ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Tiene mascota: {'Sí' if tiene_mascota else 'No'}")

