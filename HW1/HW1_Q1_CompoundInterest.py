'''
Created on Oct 19, 2017

Pn = P0 * (1+r)^n
Pn is the compound principal
P0 is the principal amount
r is the rate of interest
n is the number of year from 1 to 20

@author: KueiLin (Hubert)
'''
import math

r = 0.1
while(True):
    #listOfPn = []
    P0 = raw_input('Please input your principal amount (P0) or a quit character (Q/q):')
    sP0 = P0.strip()
    
    if( sP0 == 'q' or sP0 == 'Q'):
        print 'Quit the program!'
        break
    elif sP0.replace('.', '', 1).isdigit():
        listOfPn = [ float(sP0) * math.pow(1+r, n) for n in range(1,21) ]
        #for n in range(1,21):
        #    listOfPn.append( float(sP0) * math.pow(1+r, n) )
        print listOfPn
    else:
        print '{} is not numeric or a quit character (Q/q)'.format(sP0)
        continue