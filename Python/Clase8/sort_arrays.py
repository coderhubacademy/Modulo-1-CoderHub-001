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

def quick_sort(array):
  print("array", array)
  if len(array) <= 1:
    return array
  else:
    pivot = array.pop()
    print("pivot", pivot)
    items_greater = []
    items_lower = []
    for item in array:
      if item > pivot:
        items_greater.append(item)
      else:
        items_lower.append(item)
    print("ordenado", items_lower, [pivot], items_greater)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
  
array = [30, 40, 11, 22, 3, 1, 7, 21, 9, 17, 8]
print("quick_sort", quick_sort(array))

# Selection sort
# Merge sort
# Quick sort
