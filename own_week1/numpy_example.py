import numpy as np
import math

# a = np.array([[1,2,3], [4,5,6]])
# print(a, a.ndim)
# print(a.shape, a.dtype)

# b = np.zeros((2,3))
# b = np.ones((3,2))
# b = np.random.rand(2,3)
# b = np.full((2,3), 20)
# print(b)

# c = np.arange(10,20,3)
# c = np.linspace(10,20,3)
# print(c)


# # ELEMENT-WISE OPERATIONS
# farenheit = np.array([0,-10,-5,-15,0])
# celcius = (farenheit - 32) * (5/9)
# print(celcius)
# print(celcius > -20)

# a = np.arange(1,7).reshape(2,3)
# b = np.array([[1,2,3], [4,5,6]])
# print(a*b)

# # MATRIX-WISE OPERATIONS
# print(a.transpose()@b)
# print(a@b.transpose())

# # AGGREGATION
# print(a.sum(), a.max(), a.min(), a.mean())


# # INDEXING
# a = np.arange(1,28).reshape(3,3,3)
# print(a, a[1,0])
# print(a[[0,1,2], [0,1,1]])

# print(a[a>10])

# WITH DATASETS
graduate_admission = np.genfromtxt('../resources/week-1/datasets/Admission_Predict.csv', delimiter=',', skip_header=1)
graduate_admission[:,-3] = graduate_admission[:,-3] *4.3/10
avg_cgpa = graduate_admission[:, -3].mean()
print(avg_cgpa)
print(graduate_admission[graduate_admission[:,-3]>avg_cgpa][-1].mean())
print(graduate_admission[graduate_admission[:,-3]<avg_cgpa][-1].mean())