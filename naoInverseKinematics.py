import numpy as np
import math as m


# x, y, and z of end-effector in the global coordinate frame.

# x = 0.1479
# y = -0.1398
# z = -0.0063

x = 0.0959
y = -0.2401
z = 0.1743

# x = 0.1104
# y = -0.2731
# z = 0.1692

# Translations to position the joints at the origin of the global frame.
y = (y + 0.098)
z = (z - 0.100) 

# NAO arm joint offsets.
offsetElbow = 0.015
offsetWrist = 0.01231

# Becep and forearm lengths.
a1 = 0.105
a2 = 0.05775 + 0.05595

#############################################################

# Theta 3 calculation.

a22 = m.sqrt(a2**2 + offsetWrist**2)
r = m.sqrt(x**2 + y**2 - offsetElbow**2)

D = (z**2 + r**2 - a1**2 - a22**2)/(2*a1*a22)

phi3 = np.arctan2(m.sqrt(1-D**2),D)
phi3_2 = np.arctan2(-m.sqrt(1-D**2),D)

delta3 = np.arctan2(offsetWrist,a2)

theta3 = delta3 + phi3
theta3_2 = delta3 + phi3_2

# print('theta 3', m.degrees(theta3))

#############################################################

# Theta2 calculation.
rPrime = m.sqrt(a2**2 + offsetWrist**2)
DPrime=(r**2+z**2-a1**2-rPrime**2)/(2*a1*rPrime)

phi2 = m.atan2( y, m.sqrt( (a1 + rPrime*m.cos(phi3))**2 + offsetElbow**2 - y**2))
delta2 = m.atan2( offsetElbow, (a1 + rPrime*m.cos(phi3) ) )

theta2 = phi2 + delta2

# print('theta 2', m.degrees(theta2))

# Theta1 calculation.
alpha1 = a2*m.sin(phi3)
beta1 = a1 + a2*m.cos(phi3)

alpha2 = a2*m.sin(phi3_2)
beta2 = a1 + a2*m.cos(phi3_2)

theta1 = -(m.atan2(z,x) - m.atan2(alpha1,beta1*m.cos(phi2)))
theta1_2 = -(m.atan2(z,x) - m.atan2(alpha2,beta2*m.cos(phi2)))

# print('theta 1', m.degrees(theta1))


print('First set of solutions')
print('theta 1', m.degrees(theta1))
print('theta 2', m.degrees(theta2))
print('theta 3', m.degrees(theta3))
print('\n')

print('Second set of solutions')
print('theta 1', m.degrees(theta1_2))
print('theta 2', m.degrees(theta2))
print('theta 3', m.degrees(theta3_2))

