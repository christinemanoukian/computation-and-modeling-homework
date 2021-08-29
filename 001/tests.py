from code import check_for_symmetry
if check_for_symmetry("racecar") != True:
  print("check_for_symmetry failed on input 'racecar'")
if check_for_symmetry("hi") != False:
  print("check_for_symmetry failed on input 'hi'")
if check_for_symmetry("tacocat") != True:
  print("check_for_symmetry failed on input 'tacocat'")

from code import convert_to_numbers
if convert_to_numbers("a cat") != [1, 0, 3, 1, 20]:
  print("convert_to_numbers failed on input 'a cat'")
if convert_to_numbers("hello") != [8, 5, 12, 12, 15]:
  print("convert_to_numbers failed on input 'hello'")
if convert_to_numbers("christine") != [3, 8, 18, 9, 19, 20, 9, 14, 5]:
  print("convert_to_numbers failed on input 'christine'")

from code import convert_to_letters
if convert_to_letters([1, 0, 3, 1, 20]) != "a cat":
  print("convert_to_letters failed on input [1, 0, 3, 1, 20]")
if convert_to_letters([8, 5, 12, 12, 15]) != "hello":
  print("convert_to_letters failed on input [8, 5, 12, 12, 15]")
if convert_to_letters([3, 8, 18, 9, 19, 20, 9, 14, 5]) != "christine":
  print("convert_to_letters failed on input [3, 8, 18, 9, 19, 20, 9, 14, 5]")

from code import is_prime
if is_prime(29) != "Prime":
  print("is_prime failed on input 29")
if is_prime(15) != "Not Prime":
  print("is_prime failed on input 15")
if is_prime(4) != "Not Prime":
  print("is_prime failed on input 4")