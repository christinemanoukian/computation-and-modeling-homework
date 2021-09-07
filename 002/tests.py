from code import encode
if encode("a cat", 2, 3) != [5,3,9,5,43]:
    print("encode failed on input 'a cat'")
if encode("a cat", 1, 0) != [1,0,3,1,20]:
    print("encode failed on input 'a cat'")
if encode("christine", 2, 3) != [9,19,39,21,41,43,21,31,13]:
    print("encode failed on input 'christine'")

from code import decode_numbers
if decode_numbers([5,3,9,5,43], 2, 3) != "a cat":
    print("encode failed on input [5,3,9,5,43], 2, 3")
if decode_numbers([-5,3,9,5,43], 2, 3) != False:
    print("encode failed on input [-5,3,9,5,43], 2, 3)")
if decode_numbers([5,3,9,5,43], 1, 0) != False:
    print("encode failed on input [5,3,9,5,43], 1, 0")

from code import Stack
s = Stack()
s.push('a')
s.push('b')
s.print()
s.push('c')
s.push('d')
s.print()
print(s.pop())
s.print()

from code import Queue
q = Queue()
q.enqueue('e')
q.enqueue('f')
q.print()
q.enqueue('g')
q.enqueue('h')
q.print()
q.dequeue()
q.print()

from code import calc_minimum
if calc_minimum([3,5,1,7,2]) != 1:
    print("calc_minimum failed on input [3,5,1,7,2]")
if calc_minimum([10,9,8,7,6,5,-5,4,3,2,1]) != -5:
    print("calc_minimum failed on input [10,9,8,7,6,5,-5,4,3,2,1]")
if calc_minimum([3,1,1,8]) != 1:
    print("calc_minimum failed on input [3,1,1,8]")

from code import simple_sort
if simple_sort([3,5,1,7,2]) != [1,2,3,5,7]:
    print("simple_sort failed on input [3,5,1,7,2]")
if simple_sort([10,9,8,7,6,5,-5,4,3,2,1]) != [-5,1,2,3,4,5,6,7,8,9,10]:
    print("simple_sort failed on input [10,9,8,7,6,5,-5,4,3,2,1]")
if simple_sort([3,1,1,8]) != [1,1,3,8]:
    print("simple_sort failed on input [3,1,1,8]")
