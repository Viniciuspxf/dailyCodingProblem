# This problem was asked by Amazon.

# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

# Do this in O(N) time.


def maximum_sum(array):
  current_sum = 0
  maximum_sum = 0
  for integer in array:
    current_sum = max(integer, integer + current_sum)
    maximum_sum = max(maximum_sum, current_sum)

  return maximum_sum

print(maximum_sum([34, -50, 42, 14, -5, 86]))
print(maximum_sum([-5, -1, -8, -9]))