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


def get_intersection(list1, list2):
  result = []
  for element in list1:
    if element in list2 and element not in result:
      result.append(element)
  return result


def get_union(list1, list2):
  result = []
  for element in list1:
    if element not in result:
      result.append(element)
  for elements in list2:
    if elements not in result:
      result.append(elements)
  return result


def count_characters(input_string):
  new = input_string.lower()
  result = {

  }
  for char in new:
      result[char] = result.get(char, 0) + 1
  return result


def get_first_nth_terms_nonrecursive(n):
  result = []
  for num in range(1, n):
    if num == 1:
      first_term = 5
      result.append(5)
    result.append(3 * first_term - 4)
    first_term = 3 * first_term - 4
  return result


def get_nth_term_recursive(n):
  if n == 1:
    return 5
  answer = 3 * get_nth_term_recursive(n-1) - 4
  return answer


def convert_to_base_10(inputt):
  total = 0
  count = 0
  lst = [int(num) for num in str(inputt)]
  lst = lst[::-1]
  for number in lst:
    if number == 1:
      total += 2 ** count
    count += 1
  return total


import math
def convert_to_base_2(inputt):
  var = math.floor(math.log(inputt, 2)) + 1
  result = ""
  for char in range(var, 0, -1):
    if inputt - 2 ** (char - 1) >= 0:
      result += "1"
      inputt -= 2 ** (char - 1)
    else:
      result += "0"
  return int(result)
