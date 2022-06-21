import sys
sys.path.append('008')
from merge_sort import merge_sort

if merge_sort([-2,3,5,-2,4,4,-5,-5]) != [-5,-5,-2,-2,3,4,4,5]:
    print('merge_sort failed on input [-2,3,5,-2,4,4,-5,-5]')

if merge_sort([0,7,2,7]) != [0,2,7,7]:
    print('merge_sort failed on input [0,7,2,7]')

if merge_sort([6,9,7,4,2,1,8,5]) != [1,2,4,5,6,7,8,9]:
    print('merge_sort failed on input [6,9,7,4,2,1,8,5]')
