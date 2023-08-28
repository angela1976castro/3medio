import random

# Contrastar informacion tecnica, verificando valores nominales de las magnitudes para 
# instalacion de equipos usando instrumentos de medicion de acuerdo a las normas.
# programa simple que simula la verificación de valores nominales de magnitudes en la instalación 
# de equipos que utilizan instrumentos de medición.

calcular_valor_medido = lambda valor_nominal, tolerancia: valor_nominal + random.uniform(-tolerancia, tolerancia)


"""
calcular_valor_medido = lambda valor_nominal, tolerancia: valor_nominal + random.uniform(-tolerancia, tolerancia)
```"""

"""La parte `lambda valor_nominal, tolerancia:` define una función lambda que toma dos argumentos: `valor_nominal` y `tolerancia`.

Dentro de la función lambda, se realiza el cálculo del valor medido:

```python
valor_nominal + random.uniform(-tolerancia, tolerancia)
```

- `valor_nominal` es el valor teórico o de diseño que se espera para la magnitud.
- `tolerancia` es el rango de variación aceptable alrededor del valor nominal.

`random.uniform(-tolerancia, tolerancia)` genera un número aleatorio dentro del rango definido por `-tolerancia` y `tolerancia`. 
Esto simula la variación en la medición de la magnitud en función de la tolerancia establecida. 
Luego, el valor aleatorio generado se suma al `valor_nominal`, lo que simula una medición "realista" que podría estar dentro del rango de tolerancia.

En resumen, esta función lambda simula la obtención de un valor medido basado en un valor nominal y una tolerancia, 
teniendo en cuenta una variación aleatoria dentro del rango de tolerancia."""
def verificar_instalacion(magnitud, valor_nominal, tolerancia):
    try:
        valor_medido = calcular_valor_medido(valor_nominal, tolerancia)
        if abs(valor_medido - valor_nominal) <= tolerancia:
            return f"La medición de {magnitud} es correcta: {valor_medido:.2f}"
        else:
            return f"La medición de {magnitud} es incorrecta. Valor nominal: {valor_nominal}, Medido: {valor_medido:.2f}"
    except Exception as e:
        return f"Error al verificar {magnitud}: {str(e)}"

# Entrada de datos por parte de los estudiantes
magnitud_1 = input("Ingrese la magnitud 1: ")
valor_nominal_1 = float(input("Ingrese el valor nominal 1: "))
tolerancia_1 = float(input("Ingrese la tolerancia 1: "))

magnitud_2 = input("Ingrese la magnitud 2: ")
valor_nominal_2 = float(input("Ingrese el valor nominal 2: "))
tolerancia_2 = float(input("Ingrese la tolerancia 2: "))

# Verificación de instalación
resultado_1 = verificar_instalacion(magnitud_1, valor_nominal_1, tolerancia_1)
resultado_2 = verificar_instalacion(magnitud_2, valor_nominal_2, tolerancia_2)

# Manejo de errores
try:
    resultado_error = 5 / 0
except ZeroDivisionError as zd_error:
    resultado_error = f"Error de división: {str(zd_error)}"

# Imprimir resultados
print(resultado_1)
print(resultado_2)
print(resultado_error)

