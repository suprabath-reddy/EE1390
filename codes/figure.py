import numpy as np
import matplotlib.pyplot as plt

A = np.array([1,2])
B = np.array([-2.33333333,-1.33333333])
C = np.array([-3,-6])
D = np.array([0.33333333 ,-2.66666667])
O = np.array([-1,-2])

len =10
lam_1 = np.linspace(0,1,len)

x_AB = np.zeros((2,len))
x_BC = np.zeros((2,len))
x_CD = np.zeros((2,len))
x_DA = np.zeros((2,len))
x_AC = np.zeros((2,len))
x_BD = np.zeros((2,len))

for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
    temp2 = B + lam_1[i]*(C-B)
    x_BC[:,i]= temp2.T
    temp3 = C + lam_1[i]*(D-C)
    x_CD[:,i]= temp3.T
    temp4 = D + lam_1[i]*(A-D)
    x_DA[:,i]= temp4.T
    temp5 = C + lam_1[i]*(A-C)
    x_AC[:,i]= temp5.T
    temp6 = D + lam_1[i]*(B-D)
    x_BD[:,i]= temp6.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.05), A[1] *(1 - 0.05) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.05), B[1] * (1-0.05) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1+0.05), C[1] * (1+0.03) ,'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.05), D[1] *(1 + 0.1) , 'D')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.05), O[1] *(1 + 0.2) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.show()



print(A,B,C,D)
