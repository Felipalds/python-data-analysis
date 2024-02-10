import numpy as np

list1 = [10, 20, 30, 40, 50, 60]
vector1 = np.array(list1)
print(vector1)

list2 = [[2], [4], [6], [10], [12]]
vector2 = np.array(list2)
print(vector2)

print("Sum of vectors: ")
vector_sum = vector1 + vector2
print(vector_sum)

list3 = [1, 2, 3]
list4 = [4, 5, 6]
vector3 = np.array(list3)
vector4 = np.array(list4)
vector_sum_2 = vector3 - vector4
print(vector_sum_2)

print("Product of vectors: ")
vector_product = vector3 * vector4
print(vector_product)

vector_product_2 = vector1 * vector2
print(vector_product_2)

print("Division of vectors: ")
vector_division = vector1 / vector2
print(vector_division)

print("Vector dot product: ")
vector_dot_product = vector4.dot(vector3)
print(vector_dot_product)