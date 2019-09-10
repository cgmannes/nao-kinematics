import numpy as np
import math as m


# DH Transformation matrix.
def A_matrix(a, alpha, d, theta):

    A = np.array([[m.cos(theta), -m.sin(theta)*m.cos(alpha), m.sin(theta)*m.sin(alpha), a*m.cos(theta)],
                  [m.sin(theta), m.cos(theta)*m.cos(alpha), -m.cos(theta)*m.sin(alpha), a*m.sin(theta)],
                  [0, m.sin(alpha), m.cos(alpha), d],
                  [0, 0, 0, 1]])

    return A

#####################################################################################

# 2D movement.

# ShoulderPitch.
theta_2 = 70

# ElbowRow
theta_3 = 10

# A_matrix(a, alpha, d, theta)
A_1 = A_matrix(0.0/1000, m.radians(-90), 100.0/1000, m.radians(0))

A_2 = A_matrix(105.0/1000, m.radians(180), (-98.0 - 15.0)/1000, m.radians(theta_2))

A_3 = A_matrix(113.7/1000, m.radians(0), -12.31/1000, m.radians(theta_3))

H = np.matmul(A_1, np.matmul(A_2, A_3,))

print('\n')
print('2D transformation matrix.')
print(H)

#####################################################################################

# 3D movement.

# ShoulderPitch.
Theta_1 = 70

# ShoulderRoll.
Theta_2 = 0

# ElbowRow
Theta_3 = 10

# A_matrix(a, alpha, d, theta)
A1 = A_matrix(0.0/1000, m.radians(-90.0), 100.0/1000, m.radians(0))

A2 = A_matrix(0.0/1000, m.radians(90.0), -98.0/1000, m.radians(Theta_1))

A3 = A_matrix(105.0/1000, m.radians(90.0), 0.0/1000, m.radians(Theta_2))

A4 = A_matrix(55.95/1000, m.radians(-90.0), 15.0/1000, m.radians(Theta_3))

A5 = A_matrix(57.75/1000, m.radians(0.0), -12.31/1000, m.radians(0))

T = np.matmul(A1, np.matmul(A2, np.matmul(A3, np.matmul(A4, A5) ) ) )


print('\n')
print('3D transformation matrix.')
print(T)


