"""Solutions for the NumPy Laboratory Practice question sheet.

Run this file with: python numpy_lab_solutions.py
The examples use NumPy arrays directly; no file handling or interactive input is used.
"""

import numpy as np

print("NumPy version:", np.__version__)


# 1. Array Creation & Properties


# 1. Create an array and check its basic properties
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)


# 2. Create a 3 × 4 array with values from 1 to 12
matrix = np.arange(1, 13).reshape(3, 4)
print(matrix)


# 3. Create zeros, ones, and an identity matrix
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
identity = np.eye(3)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Identity matrix:\n", identity)


# 4. Generate even numbers between 10 and 50
even_numbers = np.arange(10, 51, 2)
print(even_numbers)


# 5. Generate 10 equally spaced numbers from 0 to 1
equally_spaced = np.linspace(0, 1, 10)
print(equally_spaced)


# 2. Array Arithmetic


# 6. Perform element-wise arithmetic on two arrays
first = np.array([12, 24, 36, 48])
second = np.array([2, 4, 6, 8])

print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)
print("Division:", first / second)


# 7. Find the square and cube of each element
numbers = np.array([2, 3, 4, 5])

print("Squares:", numbers ** 2)
print("Cubes:", numbers ** 3)


# 8. Increase every element by 15%
prices = np.array([100, 250, 400, 800])
updated_prices = prices * 1.15
print("Updated values:", updated_prices)


# 9. Find the element-wise maximum and minimum
first = np.array([14, 28, 9, 42])
second = np.array([20, 18, 12, 35])

print("Maximum:", np.maximum(first, second))
print("Minimum:", np.minimum(first, second))


# 3. Indexing & Slicing


# 10. Select different parts of an array
numbers = np.arange(21)

print("First five:", numbers[:5])
print("Last five:", numbers[-5:])
print("Index 5 to 15:", numbers[5:16])
print("Every second element:", numbers[::2])


# 11. Replace the first five elements with 100
numbers = np.arange(1, 11)
numbers[:5] = 100
print(numbers)


# 12. See the difference between a view and a copy
original = np.array([10, 20, 30, 40, 50])
view = original[1:4]
copy = original[1:4].copy()

view[0] = 999
print("Original after changing the view:", original)
print("View:", view)

copy[1] = 777
print("Original after changing the copy:", original)
print("Copy:", copy)


# 13. Reverse an array using slicing
numbers = np.array([5, 10, 15, 20, 25])
print(numbers[::-1])


# 4. 2-D Array Indexing & Slicing


# 14. Extract a row, a column, and one element
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Second row:", matrix[1, :])
print("Third column:", matrix[:, 2])
print("Element 50:", matrix[1, 1])


# 15. Extract the requested 2 × 2 sub-matrix
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

sub_matrix = matrix[0:2, 1:3]
print(sub_matrix)


# 16. Select parts of a 5 × 5 matrix
matrix = np.arange(1, 26).reshape(5, 5)

print("Full matrix:\n", matrix)
print("First row:", matrix[0, :])
print("Last column:", matrix[:, -1])
print("Middle element:", matrix[2, 2])
print("Top-left 3 × 3:\n", matrix[:3, :3])


# 5. Reshaping & Transpose


# 17. Reshape values 1–12 into a 3 × 4 matrix
numbers = np.arange(1, 13)
matrix = numbers.reshape(3, 4)
print(matrix)


# 18. Reshape a one-dimensional array into 2 × 5
numbers = np.arange(1, 11)
matrix = numbers.reshape(2, 5)
print(matrix)


# 19. Convert a 3 × 4 matrix into a 4 × 3 matrix using transpose
matrix = np.arange(1, 13).reshape(3, 4)
transposed = matrix.transpose()

print("Original shape:", matrix.shape)
print("Transposed shape:", transposed.shape)
print(transposed)


# 20. Use transpose() and swapaxes() on a 3-D array
array_3d = np.arange(1, 25).reshape(2, 3, 4)

transposed = array_3d.transpose(0, 2, 1)
swapped = np.swapaxes(array_3d, 0, 2)

print("Original shape:", array_3d.shape)
print("After transpose:", transposed.shape)
print(transposed)
print("After swapaxes:", swapped.shape)
print(swapped)


# 6. Matrix Operations


# 21. Perform element-wise addition and multiplication
first = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
second = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

print("Addition:\n", first + second)
print("Element-wise multiplication:\n", first * second)


# 22. Calculate the matrix product using np.dot()
first = np.array([[1, 2, 3],
                  [4, 5, 6]])
second = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])

product = np.dot(first, second)
print(product)


# 23. Transpose a matrix and find its dot product with the original
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
transposed = matrix.T
result = np.dot(transposed, matrix)

print("Transpose:\n", transposed)
print("Dot product:\n", result)


# 7. Universal Functions


# 24. Calculate the square root of every element
numbers = np.array([1, 4, 9, 16, 25])
print(np.sqrt(numbers))


# 25. Calculate e raised to each element
numbers = np.array([0, 1, 2, 3])
print(np.exp(numbers))


# 26. Apply square root, exponential, and absolute value to random data
rng = np.random.default_rng(26)
random_values = rng.uniform(0, 10, size=5)

print("Random values:", random_values)
print("Square roots:", np.sqrt(random_values))
print("Exponential:", np.exp(random_values))
print("Absolute values:", np.abs(random_values))


# 27. Find the element-wise maximum of two random arrays
rng = np.random.default_rng(27)
first = rng.integers(1, 50, size=6)
second = rng.integers(1, 50, size=6)

print("First array:", first)
print("Second array:", second)
print("Element-wise maximum:", np.maximum(first, second))


# 8. np.where()


# 28. Replace marks below 40 with zero
marks = np.array([35, 72, 48, 90, 55, 28])
updated_marks = np.where(marks < 40, 0, marks)
print(updated_marks)


# 29. Classify income as High or Low
income = np.array([32000, 50000, 75000, 48000, 92000])
category = np.where(income >= 50000, "High", "Low")

print(category)


# 30. Replace values greater than 30 with 100
numbers = np.array([12, 35, 27, 48, 30, 65])
updated = np.where(numbers > 30, 100, numbers)
print(updated)


# 9. Statistical Operations


# 31. Find sum, mean, variance, and standard deviation
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Sum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Variance:", np.var(matrix))
print("Standard deviation:", np.std(matrix))


# 32. Calculate row-wise and column-wise sums
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Row-wise sums:", np.sum(matrix, axis=1))
print("Column-wise sums:", np.sum(matrix, axis=0))


# 33. Find statistics for marks of 10 students
marks = np.array([78, 65, 89, 92, 55, 74, 81, 68, 95, 70])

print("Mean:", np.mean(marks))
print("Standard deviation:", np.std(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))


# 34. Demonstrate any() and all()
values = np.array([True, True, False, True])

print("any():", np.any(values))
print("all():", np.all(values))


# 10. Sorting & Unique Values


# 35. Generate and sort 10 random numbers
rng = np.random.default_rng(35)
random_numbers = rng.integers(1, 101, size=10)

print("Before sorting:", random_numbers)
print("After sorting:", np.sort(random_numbers))


# 36. Find unique values in an array with repeated elements
numbers = np.array([4, 2, 4, 7, 2, 9, 7, 7, 1])
print(np.unique(numbers))


# 37. Find the unique student marks
marks = np.array([65, 70, 65, 88, 92, 70, 75, 88, 92, 65])
print(np.unique(marks))


# 38. Check selected values using np.in1d()
values = np.array([10, 20, 30, 40, 50])
selected = np.array([20, 35, 50])

# np.in1d() is used here because it is named in the lab question.
# np.isin() is the preferred replacement in newer NumPy versions.
result = np.in1d(selected, values)
print(result)


# 11. Integrated Lab Questions


# 39. Student marks analysis
marks = np.array([
    [78, 85, 90],
    [45, 52, 48],
    [67, 71, 69],
    [32, 40, 38],
    [88, 92, 95],
    [56, 61, 59],
    [73, 75, 70],
    [41, 44, 46],
    [95, 89, 93],
    [60, 65, 63]
])

student_totals = np.sum(marks, axis=1)
student_averages = np.mean(marks, axis=1)
qualified_indices = np.where(student_averages >= 50)[0]

print("Total marks:", student_totals)
print("Average marks:", student_averages)
print("Students with average >= 50:", qualified_indices + 1)


# 40. Matrix analysis
matrix = np.arange(1, 17).reshape(4, 4)

print("Matrix:\n", matrix)
print("Transpose:\n", matrix.T)
print("Row-wise sums:", np.sum(matrix, axis=1))
print("Column-wise sums:", np.sum(matrix, axis=0))
print("Mean:", np.mean(matrix))
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))
print("Central 2 × 2 matrix:\n", matrix[1:3, 1:3])


# 41. Random data analysis
np.random.seed(41)
observations = np.random.randn(20)

print("Observations:", observations)
print("Mean:", np.mean(observations))
print("Standard deviation:", np.std(observations))
print("Minimum:", np.min(observations))
print("Maximum:", np.max(observations))
print("Sorted values:", np.sort(observations))

non_negative = np.where(observations < 0, 0, observations)
print("After replacing negatives with zero:", non_negative)


# 42. Matrix operations challenge
first = np.array([[2, 4, 6],
                  [1, 3, 5],
                  [7, 8, 9]])
second = np.array([[9, 7, 5],
                   [6, 4, 2],
                   [3, 1, 8]])

added = first + second
element_product = first * second
matrix_product = np.dot(first, second)

print("Element-wise addition:\n", added)
print("Element-wise multiplication:\n", element_product)
print("Matrix multiplication:\n", matrix_product)
print("Transpose of first matrix:\n", first.T)
print("Maximum in matrix product:", np.max(matrix_product))
print("Minimum in matrix product:", np.min(matrix_product))


# 43. Array manipulation challenge
numbers = np.arange(1, 25)
matrix = numbers.reshape(4, 6)

print("4 × 6 matrix:\n", matrix)
print("Selected rows (1st and 3rd):\n", matrix[[0, 2], :])
print("Selected columns (2nd, 4th and 6th):\n", matrix[:, [1, 3, 5]])
print("Transpose:\n", matrix.T)
print("Row sums:", np.sum(matrix, axis=1))
print("Row means:", np.mean(matrix, axis=1))
print("Column sums:", np.sum(matrix, axis=0))
print("Column means:", np.mean(matrix, axis=0))
print("Unique values:", np.unique(matrix))
