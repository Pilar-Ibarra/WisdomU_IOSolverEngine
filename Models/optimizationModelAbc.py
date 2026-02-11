from abc import ABC, abstractmethod
from typing import list
class OptimizationModel:
    def __init__(self, n: int):
        self.n = n
    @abstractmethod
    def objective_function(self,x:list[float])->float:
        pass
    @abstractmethod
    def check_constraints(self,x:list[float])->bool:
        pass
    def check_non_negativity(self,x:list[float])->bool:
        for i in range(self.n):
            if x[i]<0:
                return False
        return True