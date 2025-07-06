# Formulario básico en Python

Este proyecto es un ejemplo simple de cómo tomar entradas del usuario en Python y mostrar la información ingresada.

## 🧾 Descripción

El script solicita al usuario que ingrese:

- Su nombre
- Su edad
- Su altura (en metros)
- Si tiene o no una mascota

Luego, imprime un resumen con los datos proporcionados.

## 💻 Código principal

```python
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))
tiene_mascota = input("¿Tiene mascota? (sí/no): ").strip().lower() == "sí"

print("\n--- Información ingresada ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Tiene mascota: {'Sí' if tiene_mascota else 'No'}")
