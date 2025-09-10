import numpy as np
import matplotlib.pyplot as plt
import time
# 6x6 nuumpy array
arr6x6=np.arange(50)
random_int=np.random.randint(1,50, (6, 6))
arr_3d=random_int[:2, -3]
even_numbers=arr_3d[arr_3d % 2 == 0]
print("random array:\n",arr6x6)
print ("random\n",random_int)
print("3d array\n",arr_3d)
print("even number\n",even_numbers)
row_1=random_int[:2, :]
print("row 1\n",row_1)
column_1=random_int[:, -3:]
print("column\n",column_1)
even_numbers=random_int[random_int % 2 ==0]
print("even number:\n",even_numbers)

arr_reshape=random_int.reshape(3, 2, 6)
print("Reshaped to:\n",arr_reshape)

identity_mat= np.eye(4)
print("identity matrix;\n",identity_mat)
diagonal=np.arange(10, 40, 10)
print("diagonal num:\n",diagonal)
diag_replace=np.diag([10,20, 30, 40])
print("replace diag:\n",diag_replace)

range_3x4=np.arange(10)
print("range:\n",range_3x4)
a=np.random.randint(1,10,(3, 4))
print("A:\n",a)
range_4x3=np.arange(10)
print("range:\n",range_4x3)
b=np.random.randint(1,10,(4, 3))
print("B:\n",b)
result=np.dot(a,b)
print("Result:\n",result)

#defining a function
def array_2d(arr):
    transform_arr=np.where(arr%2==0,arr**2,-1)
    return transform_arr
new_array=array_2d(result)
print("transformed:\n",new_array)
