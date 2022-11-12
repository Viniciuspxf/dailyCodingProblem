
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

def longestPalindromicContigous(string): #quadratic solution
  max_length = 1

  max_begin_index = 0
  max_end_index = 0
  for index in range(len(string)):
    begin_index = index
    end_index = index

    while begin_index - 1 >= 0 and end_index + 1 < len(string) and string[begin_index - 1] == string[end_index + 1]:
      begin_index -= 1
      end_index += 1

    if max_length < end_index - begin_index + 1:
        max_begin_index = begin_index
        max_end_index = end_index
        max_length = end_index - begin_index + 1

    begin_index = index
    end_index = index + 1

    if (index + 1 < len(string) and string[index] == string[end_index]):
      while begin_index - 1 >= 0 and end_index + 1 < len(string) and string[begin_index - 1] == string[end_index + 1]:
        begin_index -= 1
        end_index += 1

    if max_length < end_index - begin_index + 1:
        max_begin_index = begin_index
        max_end_index = end_index
        max_length = end_index - begin_index + 1
  
  return string[max_begin_index:max_end_index+1]

print(longestPalindromicContigous("aabcdcb"))
print(longestPalindromicContigous("bananas"))