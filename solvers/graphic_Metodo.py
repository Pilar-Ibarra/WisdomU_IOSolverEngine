from typing import List
from .solverAbc import Solver
from Models.lineal_model import lineal_model
class GraphicMetod(Solver):
      def __init__(self,model:lineal_model):
        self.model=model
      def two_desitions (self,x):
        if self.model.num_variables != 2:
            raise ValueError("El problema debe tener solo 2 variables")
      def convertir_restricciones_a_rectas(self):
        pass
      def calcular_pendientes(self):
        pass
      def calcular_ordenadas_al_origen(self):
        pass
      def calcular_puntos_de_interseccion(self):
        pass
      def filtrar_puntos_validos(self):
          pass
      def calcular_funcion_objetivo_en_puntos_validos(self):
          pass
#investigar convexos
      def encontrar_solucion_optima(self):
         pass
      def solve(self):
         self._validate_two_variables()
         rectas = self._convert_constraints()
         puntos = self._compute_intersections(rectas)
         puntos_validos = self._filter_feasible(puntos)
         return self._select_best(puntos_validos)