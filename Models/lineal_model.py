from typing import List
from .optimizationModelAbc import OptimizationModel

class LinearModel(OptimizationModel):

    def __init__(self, A: List[List[float]], b: List[float], c: List[float]):
        """
        A: matriz m x n (m restricciones, n variables)
        b: vector tamaño m
        c: vector tamaño n
        """
        m = len(A)
        if m == 0:
            raise ValueError("Constraint matrix A cannot be empty.")
        n = len(A[0])
        if len(c) != n:
            raise ValueError("Objective coefficient vector size must match number of variables.")
        if len(b) != m:
            raise ValueError("RHS vector size must match number of constraints.")
        for row in A:
            if len(row) != n:
                raise ValueError("All rows in matrix A must have the same length.")
        super().__init__(n)
        self.A= A #matriz de restricciones
        self.b = b #vector de términos independientes
        self.c = c #vector de coeficientes de la función objetivo
        self.m = m  # número de restricciones
        self.n = n  # número de variables
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
