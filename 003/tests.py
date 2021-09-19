from code import *

if tally_sort([3,3,1,0,3,1,-2]) != [-2,0,1,1,3,3,3]:
    print('tally_sort failed on input [3,3,1,0,3,1,-2]')

if card_sort([3,3,1,0,3,1,-2]) != [-2,0,1,1,3,3,3]:
    print('card_sort failed on input [3,3,1,0,3,1,-2]')

if swap_sort([3,3,1,0,3,1,-2]) != [-2,0,1,1,3,3,3]:
    print('swap_sort failed on input [3,3,1,0,3,1,-2]')