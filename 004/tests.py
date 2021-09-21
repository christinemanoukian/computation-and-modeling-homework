from code import *

if newton_rhapson(2,2,.0001) != 1.4142156862745099:
    print('newton_rhapson failed on input 2,2,.0001')
if newton_rhapson(3,2,.0001) != 1.7320508100147276:
    print('newton_rhapson failed on input 3,2,.0001')
if newton_rhapson(2,3,.0001) != 1.259933493449977:
    print('newton_rhapson failed on input 2,3,.0001')

if merge([2,2,3,5,8], [1,4,9]) != [1,2,2,3,4,5,8,9]:
    print('merge failed on input [2,2,3,5,8], [1,4,9]')
if merge([1,1,6], [1,1,3]) != [1,1,1,1,3,6]:
    print('merge failed on input [1,1,6], [1,1,3]')
if merge([1,6], [-5,-4,-3,7]) != [-5,-4,-3,1,6,7]:
    print('merge failed on input [1,6], [-5,-4,-3,7]')
