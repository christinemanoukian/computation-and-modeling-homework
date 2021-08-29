def check_for_symmetry(input_string):
  if input_string == "":
    return True
  else:
    reverse = ""
    length = len(input_string) - 1
    while length >= 0:
      reverse += input_string[length]
      length -= 1
      new = reverse
    if input_string == new:
      return True
    else:
      return False


def convert_to_numbers(input_string):
  result = []
  alphabet = " abcdefghijklmnopqrstuvwxyz"
  for char in input_string:
    result.append(alphabet.index(char))
  return result


def convert_to_letters(input_array):
  result = ""
  alphabet = " abcdefghijklmnopqrstuvwxyz"
  for num in input_array:
    result += alphabet[num]
  return result


def is_prime(n):
  if n == 4:
    return "Not Prime"
  else:
    for num in range(2, n//2):
      if n % num == 0:
        return "Not Prime"
    return "Prime"
