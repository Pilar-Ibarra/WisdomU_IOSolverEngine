import json
from typing import List
from .optimizationModelAbc import OptimizationModel

class LinearModel(OptimizationModel):
    def __init__(self, name):
        super().__init__(name)
        self.type_model = "Linear"
        self.c: List[float] = []        # Coeficientes de la función objetivo
        self.A: List[List[float]] = []  # Matriz de coeficientes de las restricciones
        self.b: List[float] = []        # Vector de términos independientes
        self.symbols: List[str] = []    # Tipos de restricciones (<=, >=, =)
        self.max_or_min: str = "max"    # max o min
        self.non_negativity: bool = True

    def from_json(self, archive):
        with open(archive, 'r') as f:
            data = json.load(f)
        self.c = data['objective']["coefficients"] 
        self.A = [r['coefficients'] for r in data['constraints']]
        self.b = [r['rhs'] for r in data['constraints']]
        self.symbols = [r.get("type", "<=") for r in data['constraints']]
        self.non_negativity = data.get("non_negativity", True)
        return self

    def get_objective_coefficients(self) -> List[float]:
        return self.c.copy()
    def get_constraint_matrix(self) -> List[List[float]]:
        return [fila.copy() for fila in self.A]
    def get_rhs_vector(self) -> List[float]:
        return self.b.copy()
    def get_constraints_types(self) -> List[str]:
        return self.symbols.copy()

    def objective_function(self, x: List[float]) -> float:
        if len(x) != len(self.c):
            raise ValueError("Decision vector dimension mismatch.")
        return sum(self.c[i] * x[i] for i in range(len(self.c)))
    def check_constraints(self, x: List[float]) -> tuple[bool, str]:
        if not self.A:
            return False, "No constraints defined"
        for i, row in enumerate(self.A):
            if len(row) != len(x):
                return False, f"Number of variables in constraint {i} mismatch"
        if len(self.b) != len(self.A):
            return False, "Number of constraints mismatch"
        return True, "Check passed"
    def check_non_negativity(self, x: List[float]) -> bool:
        for val in x:
            if val < 0:
                return False
        return True
    def is_feasible(self, x: List[float]) -> bool:
        return self.check_constraints(x)[0] and (not self.non_negativity or self.check_non_negativity(x))
