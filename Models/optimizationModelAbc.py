import json
from abc import ABC, abstractmethod
from typing import List
class OptimizationModel(ABC):
    def __init__(self,name):
        self.name=name
        self.nVariables=[]
        self.type_model=""
    @abstractmethod
    def to_json(self,file):
              #metodo abstracto para guardar el modelo en un archivo json
        pass
    @abstractmethod
    def from_json(self,file):
        pass #metodo para cargar el modelo desde un archivo json.
    #getters
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
    def get_max_or_min(self):
        pass
    @abstractmethod
    def get_constraints_types(self):
        pass
    @abstractmethod
    #metodos para verificar restricciones y factibilidad
    def check_dimension_constraints(self,x:List[float])->bool:
        pass
    @abstractmethod
    def check_matemathic_constraints(self,x:List[float])->bool:
        pass
    @abstractmethod
    def constraints_report(self,x)->tuple[bool,str]:
        pass
    def check_non_negativity(self, x: List[float]) -> bool:
        return all(val >= 0 for val in x)