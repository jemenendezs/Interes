"""
MIT License

Copyright (c) 2024 Jorge Menéndez S.

Se concede permiso, de manera gratuita, a cualquier persona que obtenga una copia de este software y archivos de documentación asociados (el "Software"), a utilizar el Software sin restricciones, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

    - El aviso de copyright anterior y este aviso de permiso deben incluirse en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITÁNDOSE A GARANTÍAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O LOS TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR CUALQUIER RECLAMO, DAÑO O OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRA ACCIÓN, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO O CUALQUIER OTRO TIPO DE INTERACCIÓN CON EL SOFTWARE.

"""

def calcular_interes_simple(P, r, t):
    """Calcula el interés simple."""
    I = P * r * t
    return I

def calcular_interes_compuesto(P, r, t, n):
    """Calcula el monto total con interés compuesto."""
    A = P * (1 + r/n)**(n*t)
    return A - P  # Interés compuesto generado

def main():
    print("Selecciona el tipo de cálculo de interés:")
    print("1. Interés Simple")
    print("2. Interés Compuesto")
    
    eleccion = input("Ingresa '1' para interés simple o '2' para interés compuesto: ")
    
    if eleccion not in ['1', '2']:
        print("Selección inválida. Por favor, ingresa '1' o '2'.")
        return
    
    P = float(input("Ingresa el capital inicial: "))
    r = float(input("Ingresa la tasa de interés anual (en porcentaje): ")) / 100
    t = float(input("Ingresa el tiempo (en años): "))

    if eleccion == '1':
        # Calcular interés simple
        interes_simple = calcular_interes_simple(P, r, t)
        print(f"El interés simple generado es: ${interes_simple:.2f}")
    
    elif eleccion == '2':
        n = int(input("Ingresa la frecuencia de composición por año (p.ej., 12 para mensual, 1 para anual): "))
        interes_compuesto = calcular_interes_compuesto(P, r, t, n)
        print(f"El interés compuesto generado es: ${interes_compuesto:.2f}")

if __name__ == "__main__":
    main()
