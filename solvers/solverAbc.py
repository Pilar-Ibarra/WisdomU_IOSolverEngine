from abc import ABC, abstractmethod
from Models.optimizationModelAbc import OptimizationModel
class Solver(ABC):
    def __init__(self,model:OptimizationModel):
        self.model=model
    def objective(self,x): #dado un vector x ¿cuanto gano? cada solver va a tener su propia implementacion de esta funcion
        return self.model.objective(x)
    def maxtomin(self,x):#en dado caso queramos minimizar en vez de maximizar, esta funcion convierte el problema de maximizar a minimizar
        return -self.objective(x)
    @abstractmethod
    def is_feasible(self,x):#cada solver tiene sus reglas para determinar si una solucion es factible o no
        pass
    @abstractmethod
    def solve(self):
        pass