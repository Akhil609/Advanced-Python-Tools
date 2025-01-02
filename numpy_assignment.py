import numpy as np
print('''1. Create a 1D NumPy array with integers from 1 to 20. Perform the following operations:  
  a. Calculate the sum, mean, median, and standard deviation of the elements in the array.  
  b. Find the indices of elements greater than 10 in the array.  
''') 
#creating new array 
arr_1d=np.arange(1,21)
# performing different operations like sum, mean, median, and standard deviation of the elements in the array.
sum_arr=np.sum(arr_1d)
#here sum_arr is the variable to store result 
# np.sum() is the numpy function.
mean_arr=np.mean(arr_1d)
med_arr=np.median(arr_1d)
std_dev_arr = np.std(arr_1d)


print("1D Array:", arr_1d)
print("Sum:", sum_arr)
print("Mean:", mean_arr)
print("Median:", med_arr)
print("Standard Deviation:", std_dev_arr)

# Part 01 (b)
#Find the indices of elements greater than 10 in the array. 
indices_greater_than_10=np.where(arr_1d>10)[0]  # here [0] is used to avoid tuple structure
print(indices_greater_than_10)

print('''\n2. Create a 2D NumPy array of shape 4 X 4 with numbers ranging from 1 to 16.  
  a. Print the array.  
  b. Find the transpose of the array.  
  c. Calculate the row-wise and column-wise sums of the array.  
''')

# a.) Create a 2D NumPy array of shape 4 X 4 with numbers ranging from 1 to 16. 

arr_2d=np.arange(1,17).reshape(4,4)
print("created array :","\n",arr_2d)

#b. Find the transpose of the array.  
transpose_arr_2d=np.transpose(arr_2d)
print("Transpose of array is :  ", "\n",transpose_arr_2d)

#c. Calculate the row-wise and column-wise sums of the array.
row_sum=np.sum(arr_2d,axis=1)
col_sum=np.sum(arr_2d,axis=0)

print("\nRow-wise Sum:", row_sum)
print("Column-wise Sum:", col_sum)


print('''\n---3. Create two 3 X 3 arrays filled with random integers between 1 and 20.  
  a. Perform element-wise addition, subtraction, and multiplication.  
  b. Compute the dot product of the two arrays.----''')
#a. Perform element-wise addition, subtraction, and multiplication. 
arr_1=np.random.randint(1,21 ,size=(3,3))
arr_2=np.random.randint(1,21,size=(3,3))
print("\n3d array01 :\n",arr_1)
print("\n3d array02 :\n",arr_2)

addition=arr_1+arr_2
substraction=arr_1-arr_2
mult=arr_1*arr_2
print("\n addition :\n",addition)
print("\n substraction :\n",substraction)
print("\n mult :\n",mult)

# b. Compute the dot product of the two arrays.

dot_product=np.dot(arr_1,arr_2)
print("\n dot_product: \n",dot_product)


'''
4.)Reshape a 1D array of size 12 into a 3 X 4 2D array and slice the first two rows and last two columns.
'''
print('\n---4.)Reshape a 1D array of size 12 into a 3 X 4 2D array and slice the first two rows and last two columns.---')
arr=np.arange(1,13).reshape(3,4)
print("resulted array\n",arr)

sliced_arr=arr[:2,-2:]
sliced_arr

