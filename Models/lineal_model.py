
from typing import List
from .optimizationModelAbc import OptimizationModel
class Lineal_Model(OptimizationModel):
    #self es el equivalente a this en otros lenguajes
    def __init__(self,consumption_matrix:List[List[float]],avaibility_resources: List[float],profit_vector: List[float]):
        super().__init__(len(consumption_matrix))
        self.consumption_matrix = consumption_matrix #matriz de consumo de recursos por producto
        if len(profit_vector) != len(consumption_matrix): #el vector de ganancias por producto debe tener el mismo tamaño que el número de productos
            raise ValueError("Profit vector size must match number of products.")
        if len(consumption_matrix[0]) != len(avaibility_resources):#el número de columnas de la matriz de consumo de recursos por producto debe ser igual al tamaño del vector de disponibilidad de recursos
            raise ValueError("Matrix columns must match number of resources.")
        self.avaibility_resources = avaibility_resources #vector de disponibilidad de recursos
        self.profit_vector = profit_vector #vector de ganancia por producto
        self.n = len(consumption_matrix) #numero de productos
    def get_objective_coefficients(self):#devuelve el vector de ganancias por producto
        return self.profit_vector
    def get_constraint_matrix(self): #devuelve la matriz de consumo de recursos por producto
        return self.consumption_matrix
    def get_rhs_vector(self): #devuelve el vector de disponibilidad de recursos
        return self.avaibility_resources
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
        