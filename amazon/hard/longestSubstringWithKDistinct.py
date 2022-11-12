# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longestSubstring(string, k): #linear solution
  characters = set()
  begin_index = 0
  max_length = 1

  max_begin_index = 0
  max_end_index = 0

  for current_index in range(len(string)):
    characters.add(string[current_index])

    while len(characters) > k and begin_index < current_index:
      characters.remove(string[begin_index])
      begin_index += 1

    if max_length < current_index - begin_index + 1:
        max_begin_index = begin_index
        max_end_index = current_index
        max_length = current_index - begin_index + 1

  return string[max_begin_index:max_end_index+1]


print(longestSubstring("abcba", 2))



