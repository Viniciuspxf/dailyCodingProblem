# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def decode(encoded_string):
  decoded_string = ""

  for index in range(0, len(encoded_string), 2):
    decoded_string += int(encoded_string[index])*encoded_string[index + 1]
    index += 2

  return decoded_string


def encode(decoded_string):
  previous_character = decoded_string[0]
  counter = 1
  encoded_string = ""

  for character in decoded_string[1:]:
    if previous_character == character:
      counter += 1
    else:
      encoded_string += str(counter) + previous_character
      counter = 1
    previous_character = character

  return encoded_string + str(counter) + previous_character


assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"