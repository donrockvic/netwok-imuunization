import numpy as np
S=[]
f=open('file.txt','r')
A=np.loadtxt(f, delimiter=" ")

Tempeigen_value,Tempeigen_vector=np.linalg.eig(A)
Tempeigen_value=[x for x in Tempeigen_value]

eigen_value=max(Tempeigen_value)
index=Tempeigen_value.index(eigen_value)
eigen_vector=list(Tempeigen_vector[index])
eigen_vector=[x for x in eigen_vector]
print(eigen_value)
print(eigen_vector)

K=int(input("Enter the K value "))
V=[]
for j in range(0,len(eigen_vector)):
	V.append((2*eigen_value-A[j][j])*eigen_vector[j]*eigen_vector[j])

print(V)	

b=np.zeros((len(V),1))

for i in range(K):
	B=np.zeros((len(V),len(S)))
	U=np.zeros((1,len(S)))
	x=0
	for k in range(len(S)):
		for j in range(len(V)):
			B[j][x]=A[j][S[k]]
		x=x+1
	x=0

	for j in range(len(S)):
		U[j]=eigen_vector[S[j]]

	if len(S)!=0:
		b=B*U
	score=[-1 for x in range(len(V))]
	print(score)
	for j in range(len(V)):
		if (j not in S):
			score[j]=V[j]-2*b[j]*eigen_vector[j]

	#print(score)
	S.append(score.index(max(score)))

print('Node to be Removed are ')	
print(S)		


					

	
	



			
		

			



		
			





