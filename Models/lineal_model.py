
from typing import List
from .optimizationModelAbc import OptimizationModel
class Lineal_Model(OptimizationModel):
    #self es el equivalente a this en otros lenguajes
    def __init__(self,consumos: List[List[float]],disponibilidad: List[float],ganancia: List[float]):
        super().__init__(len(consumos))
        self.consumos = consumos #matriz de consumo de recursos por producto
        self.disponibilidad = disponibilidad #vector de disponibilidad de recursos
        self.ganancia = ganancia #vector de ganancia por producto
        self.n = len(consumos) #numero de productos

    def objective_function(self,x:list[float])->float:#dado un vector x ¿cuanto gano? 
        z=0
        for i in range(self.n): 
#ganancia por producto i multiplicado por la cantidad de producto i que se va a producir
            z+=self.ganancia[i]*x[i] 
        return z
    def cumple_restricciones(self,x:list[float])->bool:
       for j in range(len(self.disponibilidad)):
        suma=0
        for i in range(self.n):
#consumo del recurso j por el producto i multiplicado por la cantidad de producto i que se va a producir
            suma +=self.consumos[j][i]*x[i]
            if suma>self.disponibilidad[j]:
                return False
        return True
        