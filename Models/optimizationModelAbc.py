from abc import ABC, abstractmethod
from typing import list
class OptimizationModel(ABC):
    def __init__(self, n: int):
        self.n = n
    @abstractmethod
    def objective_function(self,x:list[float])->float:
        pass
    @abstractmethod
    def get_objective_coefficients(self) -> list[float]:
        pass

    @abstractmethod
    def get_constraint_matrix(self) -> list[list[float]]:
        pass

    @abstractmethod
    def get_rhs_vector(self) -> list[float]:
        pass
    @abstractmethod
    def check_constraints(self,x:list[float])->bool:
        pass
    def check_non_negativity(self,x:list[float])->bool:
        for i in range(self.n):
            if x[i]<0:
                return False
        return True