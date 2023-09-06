# Differential equation : d2y/dx2 + p(x)dy/dx + q(x)y = f(x)

import numpy as np
# import matplotlib.pyplot as plt
from input_function import f
from support import C_ij


x0 = 0.01
xn = 5
n = 10#**6

x = np.linspace(x0, xn, n)
A = np.zeros((n, n))
B = f(x)

for i in range(n):
    A[i] = C_ij(i, x)

# for i in range(n):
#     print(x[i], end=' ')
# print()

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()


