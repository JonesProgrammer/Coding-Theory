import numpy as np

#Matriz generadora
G=np.array([1,1,1,1,1])
print('La generadora G=', G)

#Codigos lineales
C=np.array(([0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2]))
print('Los codigos lineales C=', C)
k,n=C.shape
print('Numero de filas:', k)
print('Numero de columnas:', n)

#Longitud
len_C=len(C)
print('La longitud es igual a:', len_C)

#Dimension
print('La dimension es igual a:', np.size(C))
 
#Distancia minima o peso minimo
d=np.nonzero(C)
dmin=np.shape(d[0])[0]
print('La distancia minima es:', int(dmin/2))

#Matriz de control H
H=np.transpose(G)
H=H%2
print('La matriz de control es:', H)

#Clases laterales
nclases=np.power(3,n-k)
print('El numero de clases son:', nclases)
V_0=np.zeros(n)
Clase0=V_0+C
Clase1=np.mod([1,0,0,0,0],2)
Clase2=np.mod([0,1,0,0,0],2)
Clase3=np.mod([0,0,1,0,0],2)
Clase4=np.mod([0,0,0,1,0],2);
Clase5=np.mod([0,0,0,0,1],2);
Clase6=np.mod([1,0,0,0,1],2);
Clase7=np.mod([1,1,0,0,0],2);
Clase8=np.mod([0,0,1,1,1],2);

#Decodificacion del vector 12222 con sindromes
def verificar(A,B):
  aux=0
  for i in range(len(A)):
    if A[i]==B[i]:
      aux +=1
    else:
      aux=aux
  if aux == len(A):
    return True
  else:
    return False
Lide=[1,0,0,0,0]
S=np.mod(H*np.transpose(Lide),2)
St=np.transpose(S);
V=np.array([1,2,2,2,2]);
Sv=np.transpose(np.mod(H*np.transpose(V),2));
x=1
L=[0,0,0,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[1,0,0,0,1],[1,1,0,0,0],[0,0,1,1,1]
for x in range(9):
    if(verificar(Sv,St)):
    	V2=(V-L[x])%2
print('El codeword corregido es igual a:', V2)
