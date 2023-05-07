#1 Implement Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            # the target value has been found
            return mid
        elif arr[mid] < target:
            # the target value is in the right half of the list
            low = mid + 1
        else:
            # the target value is in the left half of the list
            high = mid - 1

    # the target value was not found
    return -1
arr = [1, 3, 5, 7, 9]
target = 5
print(binary_search(arr, target))  # output: 2

#2 Implement Merge Sort
def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
if __name__ == '__main__':
    array = [66, 54, 37, 100, 48, 11]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)

#3 Implement Quick Sort
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)


data = [21, 32, 13, 45, 26, 19, 74]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
#4 Implement Insertion Sort
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [2, 14, 41, 55, 71]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

#5 Write a program to sort list of strings (similar to that of dictionary)
def sort_list_of_strings(lst):
    return sorted(lst, key=lambda s: s.lower())
lst = ['cat', 'apple', 'Dog', 'banana', 'Zebra']
print(sort_list_of_strings(lst))  # output: ['apple', 'banana', 'cat', 'Dog', 'Zebra']