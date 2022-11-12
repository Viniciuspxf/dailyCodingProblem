# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.


def rotatedBinarySearch(array, k):
  begin = 0
  end = len(array) - 1
  
  while begin + 1 != end:
    medium = (begin + end) // 2
  
    if array[medium] > array[begin]:
      begin = medium
    elif array[medium] < array[end]:
      end = medium

  shift = end

  begin = 0
  end = len(array) - 1

  while begin <= end:
    medium = (begin + end) // 2
    if array[(medium - shift) % len(array)] < k:
      begin = medium + 1
    elif array[(medium - shift) % len(array)] > k:
      end = medium - 1
    else:
      return (medium - shift) % len(array)

print(rotatedBinarySearch([13, 18, 25, 2, 8, 10], 8))
print(rotatedBinarySearch([2, 8, 10, 13, 18, 25], 8))
print(rotatedBinarySearch([25, 2, 8, 10, 13, 18], 8))