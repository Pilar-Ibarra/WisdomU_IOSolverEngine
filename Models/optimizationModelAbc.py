from abc import ABC, abstractmethod
from typing import List
class OptimizationModel:
    def __init__(self, n: int):
        self.n = n
    @abstractmethod
    def objective_function(self,x:list[float])->float:
        pass
    @abstractmethod
    def cumple_restricciones(self,x:list[float])->bool:
        pass
    def no_negatividad(self,x:list[float])->bool:
        for i in range(self.n):
            if x[i]<0:
                return False
        return True