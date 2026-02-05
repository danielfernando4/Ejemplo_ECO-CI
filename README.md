# Ejemplo_ECO-CI

Descripción general

El siguiente ejemplo busca comparar el impacto entre dos algoritmos, uno eficiente y otro ineficiente, para encontrar todos los números primos hasta un límite determinado.

Contenido del repositorio

En el repositorio se incluyen dos archivos, cada uno implementando un algoritmo distinto para el cálculo de números primos.

Uso del ejemplo

Para que el ejemplo funcione correctamente:

El archivo que se desea evaluar debe renombrarse como primes.py.

Dependiendo del algoritmo seleccionado, se ejecutará uno de los pipelines definidos.

Pipelines disponibles
Pipeline 1

Este pipeline muestra una tabla de métricas que permite medir el consumo de hardware del algoritmo especificado.
Las métricas evaluadas son:

Utilización de la CPU

Consumo de energía (en Joules)

Potencia eléctrica (en Watts)

Duración total del algoritmo

Pipeline 2

Este pipeline valida el consumo energético total del algoritmo:

El pipeline falla si la energía total del Total run no es menor a 60 Joules.
