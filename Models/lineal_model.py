import json
from typing import List
from .optimizationModelAbc import OptimizationModel
class LinearModel(OptimizationModel):
    def __init__(self,nombre):
      super().__init__(nombre)
      self.type_model="Lineal"
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
        return self.c.copy()# Devolvemos una copia para evitar modificaciones externas
    def get_constraint_matrix(self) -> List[List[float]]:
        return [fila.copy() for fila in self.A]
    def get_rhs_vector(self) -> List[float]:
        return self.b.copy()
    def get_Symbols(self):
        return self.symbols
    def get_constraints_types(self):
        return super().get_constraints_types()
    def objective_function(self, x: List[float]) -> float:
        if len(x) != self.n:
            raise ValueError("Decision vector dimension mismatch.")
        return sum(self.c[i] * x[i] for i in range(self.n))
    def check_constraints(self, x):
        if len(self.A[0]):
            return False,"number of variables in constraints mismatch"
        for i,row in enumerate(self.A):
            if len(row)!=len(x):
                return False,f"number of variables in constraint {i} mismatch"
        if len(self.b)!=len(self.A):
            return False,"number of constraints mismatch"
        return True,"Check passed"
    def check_non_negativity(self,x:List[float])->bool:
        return super().check_non_negativity(x)
        
    def is_feasible(self, x: List[float]) -> bool:
        return self.check_constraints(x)[0] and self.check_non_negativity(x)