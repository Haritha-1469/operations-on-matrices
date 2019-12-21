import numpy as np
from numpy import linalg
#BASIC OPERATIONS ON MATRIX
x=np.matrix([[1,2,3],
[4,5,6],
[7,8,9]])
y=np.matrix([[1,2,3],
[2,5,4],
[1,2,1]])
print("addition of two matrices is:\n",x+y)
print("subtraction of two matrices is:\n",x-y)
print("multiplication of two matrices is:\n",x*y)
# add 1 to every element 
print ("Adding 1 to every element:", x+1)  
# subtract 3 from each element 
print ("Subtracting 3 from each element:", x-3)  
# multiply each element by 10 
print ("Multiplying each element by 10:", x*10)  
# square each element 
print ("Squaring each element:", x**2) 
#same operations using numpy
print ("The element wise addition of matrix is using numpy: ") 
print (np.add(x,y)) 
print ("The element wise subtraction of matrix using numpy is : ") 
print (np.subtract(x,y)) 
print ("The element wise division of matrix using numpy is : ") 
print (np.divide(x,y))
print ("The multiplication of matrices using numpy is : ") 
print (np.dot(x,y))  
print ("The element wise square root using numpy is : ") 
print (np.sqrt(x)) 
#LINEAR ALGEBRA
A = np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]]) 
print("given new matrix is",A)
# Rank of a matrix
print("\nRank of A:", np.linalg.matrix_rank(A))
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A)) 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
#power of matrix A
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))
#transpose of the matrix 
print ("The transpose of given matrix is : ") 
print (A.T) 
# Creating a diagonal matrix
a = np.diag((1, 2, 3)) 
print("diagonal matrix is :\n",a)
#finding eigen values of general matrix
print("eigen values of matrix a:",np.linalg.eigvals(a))
#finding eigen vectors and values of general matrix
print("eigen vectors and values of matrix a:",np.linalg.eigh(a))

   

