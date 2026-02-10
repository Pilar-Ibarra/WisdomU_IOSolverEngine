from abc import ABC, abstractmethod
class Solver(ABC):
    @abstractmethod
    def objective(self,x):
        pass
    @abstractmethod
    def is_feasible(self,x):
        pass
    