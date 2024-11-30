array = [1, 2, 3, 88, 90, 7, 5, 4, 0]
array.sort()
print(array)

# Bubble sort

def bubble_sort(array):
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
  return array

# Selection sort
# Merge sort
# Quick sort
