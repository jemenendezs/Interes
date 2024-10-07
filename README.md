# Calculadora de Interés Simple y Compuesto en Python

Este programa en Python permite al usuario calcular el interés simple o compuesto basado en un capital inicial, una tasa de interés anual y un tiempo dado. El usuario puede elegir entre ambos métodos ingresando la opción correspondiente.

## Funcionalidades

- **Cálculo de Interés Simple**: Utiliza la fórmula del interés simple para calcular el interés generado a partir del capital inicial.
- **Cálculo de Interés Compuesto**: Permite calcular el interés compuesto, con opción de seleccionar la frecuencia de composición por año (mensual, anual, etc.).

### Fórmulas Utilizadas

1. **Interés Simple**:

   $I = P \times r \times t$

   - `P`: Capital inicial (monto invertido o prestado).
   - `r`: Tasa de interés anual (en decimal).
   - `t`: Tiempo (en años).

2. **Interés Compuesto**:

   $A = P \times \left(1 + \frac{r}{n}\right)^{nt}$

   - `P`: Capital inicial.
   - `r`: Tasa de interés anual (en decimal).
   - `n`: Frecuencia de composición (mensual, anual, etc.).
   - `t`: Tiempo (en años).
   - `A - P`: Interés compuesto generado.

## Instrucciones de Uso

1. Ejecuta el programa.
2. Selecciona el tipo de interés que deseas calcular:
   - Ingresa `1` para **Interés Simple**.
   - Ingresa `2` para **Interés Compuesto**.
3. Ingresa los datos requeridos:
   - **Capital inicial**: El monto invertido o prestado.
   - **Tasa de interés anual**: La tasa en porcentaje (p.ej., 7.5 para 7.5%).
   - **Tiempo**: El período de la inversión o préstamo en años.
   - Para interés compuesto, también ingresa la **frecuencia de composición** (p.ej., 12 para mensual).
4. El programa mostrará el interés generado según el tipo de cálculo seleccionado.

## Requisitos

- **Python 3.x**: Asegúrate de tener instalada una versión reciente de Python.

## Ejemplo de Uso

### Interés Simple
```bash
Ingresa '1' para interés simple o '2' para interés compuesto: 1
Ingresa el capital inicial: 1000
Ingresa la tasa de interés anual (en porcentaje): 5
Ingresa el tiempo (en años): 2
El interés simple generado es: $100.00
```

### Interés Compuesto
```bash
Ingresa '1' para interés simple o '2' para interés compuesto: 2
Ingresa el capital inicial: 1000
Ingresa la tasa de interés anual (en porcentaje): 5
Ingresa el tiempo (en años): 2
Ingresa la frecuencia de composición por año (p.ej., 12 para mensual, 1 para anual): 12
El interés compuesto generado es: $104.71
```
### Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


