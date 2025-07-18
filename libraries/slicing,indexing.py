# -*- coding: utf-8 -*-
"""slicing,indexing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hWq1i-m9JOtiyqOPKaD_qI6i6gsz_BLb
"""

# 1D Array Indexing & Slicing
import numpy as np
a = np.array([10,20,30,40,50])
print(a[0])     #10
print(a[3])     #40
print(a[-1])    #50
print(a[1:3])   #[20 30]

#  2D Array Indexing
import numpy as np
b= np.array([[10,20,30],
            [40,50,60]])
print(b[0])    #[10 20 30]
print(b[0,[-1]]) #[30]
print(b)     #[[10 20 30]
#              [40 50 60]

b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(b[0, 0])  # 1 (row 0, column 0)
print(b[1, 2])  # 6 (row 1, column 2)

print(b[0, :])   # First row → [1 2 3]
print(b[:, 1])   # Second column → [2 5]
print(b[:, 2])    #third row [3 6]
print(b[1,0:])    #[4 5 6]

# Reshaping Arrays
import numpy as np
c = np.array([1,2,3,4,5,6])
reshaped = c.reshape([2,3])   # 2 row 3 columns
print(reshaped)
# [[1 2 3]
 #[4 5 6]]
# note : reshape will work when total element will match (eg. 2x3 - 6)

#Flatten (2D → 1D)

flat = reshaped.flatten()
print(flat)   #[1 2 3 4 5 6]

import numpy as np
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr[0])                            # [10 20 30]
print(arr[1])                            #[40 50 60]
print(arr[2])                             #[70 80 90]
print(arr[0,1])                           #[]
print(arr[1,2])
print(arr[0,:])

arr = np.array([[10, 20], [30, 40], [50, 60]])

print(arr[1, 0])   # 30
print(arr[:, 1])   # [20 40 60]
print(arr[0:2, 0]) # [10 30]

# 2d array slicing
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
Row 0 → [1 2 3]
Row 1 → [4 5 6]
         ↑ ↑ ↑
       Col0 Col1 Col2

arr[row_slice, column_slice]
Example: arr[0, :]

print(arr[0, :])   # Output: [1 2 3]
# 0 → row index 0

# : → all columns of that row

#  Example 2: arr[:, 1]
# 👉 All rows, column 1
print(arr[:, 1])   # Output: [2 5]
# : → all rows

# 1 → column index 1

# Example 3: arr[0:2, 1:]
# 👉 Rows 0 to 1, columns 1 to end
print(arr[0:2,1:])

import numpy as np

arr = np.array([[11, 12, 13],
                [21, 22, 23],
                [31, 32, 33]])
# [
#  [11 12 13]  ← row 0
#  [21 22 23]  ← row 1
#  [31 32 33]  ← row 2
# ]
#    ↑  ↑  ↑
#   c0 c1 c2

print(arr[0:2, 0:2])
# [[11 12]
#  [21 22]]
print(arr[0:2, 0:2])
# [[11 12]
#  [21 22]]
print(arr[1:3, 1:3])
# [[22 23]
#  [32 33]]
print(arr[:, 0:2])
# [[11 12]
#  [21 22]
#  [31 32]]
print(arr[0:3, 2:])
# [[13]
#  [23]
#  [33]]
print(arr[:, :])
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

print(arr[1:, 0:2])