from code import *

if newton_rhapson(2,2,.0001) != 1.4142156862745099:
    print('newton_rhapson(2,2,.0001) failed on input 2,2,.0001')
if newton_rhapson(3,2,.0001) != 1.7320508100147276:
    print('newton_rhapson(3,2,.0001) failed on input 3,2,.0001')
if newton_rhapson(2,3,.0001) != 1.259933493449977:
    print('newton_rhapson(2,3,.0001 failed on input 2,3,.0001')