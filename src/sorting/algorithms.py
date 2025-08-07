import helpers

array = [5, 8, 1, 2, 9]
big_array = [5, 8, 1, 2, 9, 3] * 1000

def swap(arr, index1, index2):
  arr[index1], arr[index2] = (arr[index2], arr[index1])

def bubble_sort(arr: list):
  array = arr.copy()
  for i in range(0, len(array) -1):
    swap_made = False
    for j in range(0, (len(array) - (i+1))):
      if(array[j] > array[j+1]):
        swap(array, j, j+1)
        swap_made = True

    if(not swap_made):
      break
  return array
    

def merge_sort(arr):

  if(len(arr) == 1):
    print(arr)
    return arr
  
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  merge = []
  
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if(left[i] <= right[j]):
      merge.append(left[i])
      i += 1
    else:
      merge.append(right[j])
      j += 1

  merge.extend(left[i:])
  merge.extend(right[j:])

  return merge

# print(bubble_sort(array))
print(merge_sort(array))


# print('Bubble Sort execution time:')
# helpers.calculate_execution_time(bubble_sort, big_array)

# print('MergeSort execution time')
# helpers.calculate_execution_time(merge_sort, big_array)

