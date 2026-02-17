import json
from typing import List
from .optimizationModelAbc import OptimizationModel

class LinearModel(OptimizationModel):

    def __init__(self,nombre):
      super().__init__(nombre)
      self.tipo_modelo="Lineal"
      self.c: List[float] = []  # Coeficientes de la función objetivo
      self.A: List[List[float]] = []  # Matriz de coeficientes de las restricciones
      self.b: List[float] = []  # Vector de términos independientes de las restricciones
      self.symbols: List[str] = []  # Tipos de restricciones (<=, >=, =)
      self.max_or_min: str = "max"  # Indica si es maximización
      def from_json(self,archive):
          with open(archive,'r') as f:
            data=json.load(f)
            self.c = data['objective']["coefficients"]
            self.A = data['constraints']["symbols"]
            self.b = data['nVariables']["names"]
            self.A=[r['coefficients']for r in data['constraints']]
            self.b=[r['rhs']for r in data['constraints']]
            self.symbols=[r.get("type","<=") for r in data['constraints']]
            self.non_negativity=data.get("non_negativity",True)
            return self
    def get_objective_coefficients(self) -> List[float]:
        return self.c
    def get_constraint_matrix(self) -> List[List[float]]:
        return self.A
    def get_rhs_vector(self) -> List[float]:
        return self.b
    def objective_function(self, x: List[float]) -> float:
        if len(x) != self.n:
            raise ValueError("Decision vector dimension mismatch.")
        return sum(self.c[i] * x[i] for i in range(self.n))
    def check_constraints(self, x: List[float]) -> bool:
        if len(x) != self.n:
            raise ValueError("Decision vector dimension mismatch.")

        for j in range(self.m):
            total = sum(self.A[j][i] * x[i] for i in range(self.n))
            if total > self.b[j]:
                return False
        return True
    def is_feasible(self, x: List[float]) -> bool:
        return self.check_constraints(x) and self.check_non_negativity(x)
