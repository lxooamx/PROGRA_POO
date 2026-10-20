# Reto de Estructuras — Clínica veterinaria 

## Descripción
Programa de Python que gestiona solicitudes de una clínica veterinaria en memoria usando una lista enlazada, una pila y una cola.

## Datos de prueba
- V01: Vacuna
- V02: Control
- V03: Emergencia

## Requisitos
Python 3 instalado. No necesita bases de datos ni librerías externas.

## Cómo ejecutar
1. Abre la carpeta del proyecto en PyCharm.
2. Abre `Caso num2.py`.
3. Ejecuta el archivo con el botón **Run** o desde una terminal con:
   ```bash
   python Caso num2.py
   ```

## Estructuras implementadas
- **Lista enlazada:** agrega nodos al final y muestra todos los registros.
- **Pila (LIFO):** `apilar` agrega al final y `desapilar` retira el último elemento agregado.
- **Cola (FIFO):** `encolar` agrega al final y `desencolar` retira el primer elemento agregado.
- **Reto individual:** si la cola está vacía, `desencolar` muestra un mensaje y devuelve `None`, sin producir un error.

## Verificación
Al ejecutar el programa, revisa que:
- La lista muestre V01, V02 y V03.
- La pila retire primero V03 (último agregado).
- La cola retire primero V01 (primero agregado).
- Al intentar retirar de una cola vacía, aparezca un mensaje y el programa continúe sin error.
