import json
from abc import ABC, abstractmethod
from typing import List
class OptimizationModel(ABC):
    def __init__(self,nombre):
        self.nombre=nombre
        self.nVariables=[]
        self.tipo_modelo=""
    @abstractmethod
    def to_json(self,archive):
              #metodo abstracto para guardar el modelo en un archivo json
        pass
    def dataMatrix(self):
        pass
    @abstractmethod
    def objective_function(self,x:List[float])->float:
        pass
    @abstractmethod
    def get_objective_coefficients(self) -> List[float]:
        pass

    @abstractmethod
    def get_constraint_matrix(self) -> List[List[float]]:
        pass

    @abstractmethod
    def get_rhs_vector(self) -> List[float]:
        pass
    @abstractmethod
    def check_constraints(self,x:List[float])->bool:
        pass
    def check_non_negativity(self,x:List[float])->bool:
        for i in range(self.n):
            if x[i]<0:
                return False
        return True