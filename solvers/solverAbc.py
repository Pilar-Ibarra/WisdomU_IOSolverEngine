from abc import ABC, abstractmethod
class Solver(ABC):
    @abstractmethod
    def objective(self,x): #dado un vector x ¿cuanto gano? cada solver va a tener su propia implementacion de esta funcion
        pass
    def maxtomin(self,x):#en dado caso queramos minimizar en vez de maximizar, esta funcion convierte el problema de maximizar a minimizar
        return -self.objective(x)
    @abstractmethod
    def is_feasible(self,x):#cada solver tiene sus reglas para determinar si una solucion es factible o no
        pass
    