#Lineal model
Modelo de Optimización de ProducciónBasado en la metodología de Hillier & Lieberman (9na Edición)
## 1. Función Objetivo ($Z$) -
 El objetivo principal es maximizar las ganancias totales
  (profits).$$Z = c_1x_1 + c_2x_2 + \dots + c_nx_n$$$Z$:
  - Ganancia total a optimizar.$c_n$: 
  - Profit (margen de contribución) unitario del producto $n$.$x_n$: 
  - Cantidad óptima a producir (Variables de decisión).
  2. Restricciones Técnicas -
  El modelo amolda los datos en una matriz de coeficientes que describe el consumo de recursos.
  Limitaciones de Capacidad
  Representan el techo operativo del sistema (ej. horas disponibles):
  $$a_{i1}x_1 + a_{i2}x_2 \leq b_i$$$a_{ij}$: 
  Coeficiente tecnológico (cuánto consume el producto $j$ del recurso $i$).$b_i$: 
  Disponibilidad total del recurso (Input).
  Condición de No Negatividad
  Garantiza que el Solver solo considere soluciones lógicas en el mundo real:
  $$x_j \geq 0, \text{ para todo } j=1, 2, \dots, n$$