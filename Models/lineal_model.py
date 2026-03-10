import json
import numpy
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
        self.max_or_min: str = "max"  # "max" or "min"        self.non_negativity: bool = True
        #mueve el json hacia otra capa
    model = Linear_Model_parser.from_json("problem.json")

    def get_objective_coefficients(self) -> List[float]:
        return self.c.copy()
    def get_constraint_matrix(self) -> List[List[float]]:
        return [fila.copy() for fila in self.A]
    def get_rhs_vector(self) -> List[float]:
        return self.b.copy()
    def get_constraints_types(self) -> List[str]:
        return self.symbols.copy()

    def objective_function(self, x: List[float]) -> float:
     return float(numpy.dot(self.c, x))
    def check_dimension_constraints(self,x:List[float])->bool:
        #validación de dimensiones
        for i, row in enumerate(self.A):
            if len(row) != len(x):
                return False, f"Number of variables in constraint {i} mismatch"
        if len(self.b) != len(self.A):
            return False, "Number of constraints mismatch"
        return True, "Check passed"
    #validación matematica:D-> crea ese metodo
    def check_mathematic_constraints(self, x: List[float]):
        for i, row in enumerate(self.A):
            lhs = sum(a * xi for a, xi in zip(row, x))
            rhs = self.b[i]
            symbol = self.symbols[i]

            if symbol == "<=" and lhs > rhs + 1e-9:
                return False, f"Constraint {i} violated: {lhs} > {rhs}"

            elif symbol == ">=" and lhs < rhs - 1e-9:
                return False, f"Constraint {i} violated: {lhs} < {rhs}"

            elif symbol == "=" and abs(lhs - rhs) > 1e-9:
                return False, f"Constraint {i} violated: {lhs} != {rhs}"

        return True, "All constraints satisfied"
    def check_matemathic_constraints(self, x):
        return super().check_matemathic_constraints(x)
    def is_feasible(self, x: List[float]) -> bool:
        return self.check_constraints(x)[0] and (not self.non_negativity or self.check_non_negativity(x))
    def to_json(self, file):
        data={
            "name":self.name,
            "type_model":self.type_model,
            "objective":{
                "coefficients":self.c
            },
            "constraints":[{
                "coefficients":self.A[i],
                "rhs":self.b[i],
                 "type": self.symbols[i]
            }
            for i in range(len(self.A))
            ],
            "non_negativity":self.non_negativity,
            "max_or_min":self.max_or_min
        }
        with open(file,"w")as f:
         json.dump(data,f,indent=4)
  