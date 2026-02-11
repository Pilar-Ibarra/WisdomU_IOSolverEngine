# Lineal Model
## Production Optimization Model
*Based on Hillier & Lieberman (9th Edition)*
---
## 1. Objective Function ($Z$)
The main objective is to **maximize total profit**.
$$
Z = \sum_{j=1}^{n} c_j x_j
$$
**Where:**
* $Z$ → Total profit to be maximized
* $c_j$ → Unit contribution margin (profit) of product $j$
* $x_j$ → Decision variable (optimal production quantity of product $j$)
---
## 2. Technical Constraints
The model organizes the data into a **technological coefficient matrix** that represents resource consumption.
### Capacity Constraints
These represent the operational limits of the system (e.g., available hours, materials, labor):
$$\sum_{j=1}^{n} a_{ij} x_j \leq b_i \quad \text{for } i = 1,2,\dots,m$$
**Where:**
* $a_{ij}$ → Technological coefficient (amount of resource $i$ consumed by product $j$)
* $b_i$ → Total availability of resource $i$
---
### Non-Negativity Condition
Ensures that the solver considers only feasible real-world solutions:
$$
x_j \geq 0 \quad \text{for } j = 1,2,\dots,n
$$
---
## Standard Form
Maximize:
Z = c^T x
Subject to:
Ax ≤ b  
x ≥ 0
