from typing import List
from .solverAbc import Solver
from Models.lineal_model import lineal_model
class GraphicMetod(Solver):
      def __init__(self,model:lineal_model):
        self.model=model
      def check_twoVar (self,x):
        if self.model.num_variables != 2:
            raise ValueError("El problema debe tener solo 2 variables")
      def convert_constraints_to_lines(self):
        pass
      def calculate_slope(self):
        pass
      def calculate_y_intercept(self):
        pass
      def calculate_intersection_points(self):
        pass
      def filter_feasible_points(self):
          pass
      def calculate_objective_function_at_feasible_points(self):
          pass
#investigar cierre convexo
      def find_optimal_solution(self):
         pass
      def solve(self):
         self.check_twoVar(self.model)
         lines = self.convert_constraints_to_lines()
         points = self.calculate_intersection_points(lines)
         feasible_points = self.filter_feasible_points(points)
         return self.find_optimal_solution(feasible_points)