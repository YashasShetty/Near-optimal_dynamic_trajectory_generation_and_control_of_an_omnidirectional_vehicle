from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# Vertices of the cube
A=sym.Matrix([[-1,-1,-1]])
A=A.transpose()

B=sym.Matrix([[-1,1,-1]])
B=B.transpose()

C=sym.Matrix([[1,1,-1]])
C=C.transpose()

D=sym.Matrix([[1,-1,-1]])
D=D.transpose()

E=sym.Matrix([[-1,-1,1]])
E=E.transpose()

F=sym.Matrix([[-1,1,1]])
F=F.transpose()

G=sym.Matrix([[1,1,1]])
G=G.transpose()

H=sym.Matrix([[1,-1,1]])
H=H.transpose()

P_0= sym.Matrix([[0,-sqrt(3),sqrt(3)],
                 [2,-1,-1],
                 [2,2,2]])

P_0=0.5*P_0

# Tilted Cuboid
A1=P_0*A
print(A1[0],A1[1],A1[2])

B1=P_0*B
print(B1[0],B1[1],B1[2])

C1=P_0*C
print(C1[0],C1[1],C1[2])

D1=P_0*D
print(D1[0],D1[1],D1[2])

E1=P_0*E
print(E1[0],E1[1],E1[2])

F1=P_0*F
print(F1[0],F1[1],F1[2])

G1=P_0*G
print(G1[0],G1[1],G1[2])

H1=P_0*H
print(H1[0],H1[1],H1[2])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Compute rotation matrix
def FindTransformationMatrix(theta):
    transformation_matrix = sym.Matrix(
        [[sym.cos(theta), -sym.sin(theta) ,0], 
         [sym.sin(theta), sym.cos(theta) ,0],
         [0, 0, 1]])

    return transformation_matrix



for i in range(0,35): 
    x=[]
    y=[]
    z=[]
    theta1=np.deg2rad(10*i)
    rotation_matrix=FindTransformationMatrix(theta1)
    A2=rotation_matrix*A1
    x.append(A2[0])
    y.append(A2[1])
    z.append(A2[2])
    
    B2=rotation_matrix*B1
    x.append(B2[0])
    y.append(B2[1])
    z.append(B2[2])
   
    C2=rotation_matrix*C1
    x.append(C2[0])
    y.append(C2[1])
    z.append(C2[2])

    D2=rotation_matrix*D1
    x.append(D2[0])
    y.append(D2[1])
    z.append(D2[2])
   
    E2=rotation_matrix*E1
    x.append(E2[0])
    y.append(E2[1])
    z.append(E2[2])
   
    F2=rotation_matrix*F1
    x.append(F2[0])
    y.append(F2[1])
    z.append(F2[2])
   
    G2=rotation_matrix*G1
    x.append(G2[0])
    y.append(G2[1])
    z.append(G2[2])
    
    H2=rotation_matrix*H1
    x.append(H2[0])
    y.append(H2[1])
    z.append(H2[2])

    ax.plot(x,y,z)
    
plt.axis('equal')
plt.show()



