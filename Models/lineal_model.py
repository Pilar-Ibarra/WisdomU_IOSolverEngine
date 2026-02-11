
from typing import List
from .optimizationModelAbc import OptimizationModel
class Lineal_Model(OptimizationModel):
    #self es el equivalente a this en otros lenguajes
    def __init__(self,consumption_matrix:List[List[float]],avaibility_resources: List[float],profit_vector: List[float]):
        super().__init__(len(consumption_matrix))
        self.consumption_matrix = consumption_matrix #matriz de consumo de recursos por producto
        self.avaibility_resources = avaibility_resources #vector de disponibilidad de recursos
        self.profit_vector = profit_vector #vector de ganancia por producto
        self.n = len(consumption_matrix) #numero de productos

    def objective_function(self,x:list[float])->float:#dado un vector x ¿cuanto gano? 
        z=0.0
        for i in range(self.n): 
#ganancia por producto i multiplicado por la cantidad de producto i que se va a producir
            z+=self.profit_vector[i]*x[i] 
        return z
    def check_constraints(self,x:list[float])->bool:
      for j in range(len(self.avaibility_resources)): #para cada recurso
        total_consumption=0.0
        for i in range(self.n): #para cada producto
            total_consumption+=self.consumption_matrix[i][j]*x[i] #consumo del recurso j por el producto i multiplicado por la cantidad de producto i que se va a producir
        if total_consumption>self.avaibility_resources[j]:
            return False
        return True
        