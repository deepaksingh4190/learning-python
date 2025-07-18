# -*- coding: utf-8 -*-
"""linear_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TNwDM1QP_riKodfNedjeZDUiIzAt6QH8
"""

# Linear search, also known as sequential search, is a simple algorithm for finding a target element within a list or array. It works by checking each element in the sequence one by one, starting from the beginning, until the target is found or the end of the sequence is reached.
#Algorithm:
# Start from the first element of the list.
# Compare the current element with the target element.
# If they match, the element is found, and its index is returned.
# If they do not match, move to the next element in the list.
# Repeat steps 2-4 until the element is found or the end of the list is reached.
# If the end of the list is reached without finding the target, indicate that the element is not present (e.g., by returning -1 or None).

def linear_search(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return f"found at index {i}"
  return f"not found"
linear_search([10, 25, 30, 45, 50],30)