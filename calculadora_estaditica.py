def calcular_estadisticas(numeros: list[float]) -> dict[str, float]:
    """
    Calcula estadísticas básicas (cantidad, suma, promedio, mínimo y máximo) 
    de una lista de números.

    Args:
        numeros: Una lista de números (enteros o flotantes).

    Returns:
        Un diccionario que contiene las estadísticas calculadas.
        Si la lista está vacía, devuelve un diccionario con valores nulos o 0.
    """
    if not numeros:
        return {
            "cantidad": 0,
            "suma": 0.0,
            "promedio": 0.0,
            "minimo": None,
            "maximo": None
        }

    cantidad = len(numeros)
    suma = sum(numeros)
    promedio = suma / cantidad
    minimo = min(numeros)
    maximo = max(numeros)

    return {
        "cantidad": cantidad,
        "suma": suma,
        "promedio": promedio,
        "minimo": minimo,
        "maximo": maximo
    }


def main():
    """
    Función principal que maneja la interacción con el usuario en la consola.
    """
    print("=== Calculadora de Estadísticas Básicas ===")
    print("Ingresa una lista de números separados por espacios.")
    print("Ejemplo: 10 5.5 8 20 3")
    
    entrada = input("\nNúmeros: ").strip()
    
    if not entrada:
        print("Error: No ingresaste ningún número.")
        return

    # Procesar la entrada del usuario
    try:
        # Convertir la cadena de entrada en una lista de floats usando comprensión de listas
        numeros = [float(x) for x in entrada.split()]
    except ValueError:
        print("Error: Por favor, asegúrate de ingresar solo números válidos separados por espacios.")
        return

    # Calcular estadísticas
    estadisticas = calcular_estadisticas(numeros)

    # Mostrar resultados
    print("\n--- Resultados ---")
    print(f"Cantidad de números : {estadisticas['cantidad']}")
    print(f"Suma total          : {estadisticas['suma']}")
    print(f"Promedio            : {estadisticas['promedio']:.2f}")
    print(f"Valor mínimo        : {estadisticas['minimo']}")
    print(f"Valor máximo        : {estadisticas['maximo']}")


if __name__ == "__main__":
    main()