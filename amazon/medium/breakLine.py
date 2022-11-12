# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10. assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

def break_line(string:str, k:int):
  splitted_string = string.split()
  lines = []
  current_length = 0
  begin_index = 0

  for end_index in range(len(splitted_string)):
    if current_length == 0 and len(splitted_string[end_index]) <= k:
      current_length += len(splitted_string[end_index])
    elif len(splitted_string[end_index]) + current_length + 1 <= k:
      current_length += len(splitted_string[end_index]) + current_length + 1
    elif len(splitted_string[end_index]) <= k and begin_index != end_index:
      lines.append(" ".join(splitted_string[begin_index:end_index]))
      begin_index = end_index
      current_length = len(splitted_string[end_index])
    else:
      return

  if splitted_string[begin_index:end_index + 1]:
    lines.append(" ".join(splitted_string[begin_index:end_index + 1]))

  return lines if len(lines[-1]) <= k else None

print(break_line("the quick brown fox jumps 1111111111 the lazy 1111111111", 10))
