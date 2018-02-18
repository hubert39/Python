'''
Created on Nov 2, 2017

@author: Kuei-Lin Yang (Hubert)
'''

import math

class InterestCalculator(object):
    finalval = 0
    def __init__(self, nyears, interest_rate, initial_principal):
        #finalval = 0
        self.nyears = nyears;
        self.interest_rate = interest_rate;
        self.initial_principal = initial_principal;

# P * ( (1+i)^n - 1)
class CICalculator(InterestCalculator):
    ''' CI stands for compound interest '''
    def calcfinalval(self):
        self.finalval = self.initial_principal * ( math.pow(1+self.interest_rate, self.nyears) - 1 )
        
        
class SICalculator(InterestCalculator):
    '''SI stands for simple interest '''
    def calcfinalval(self):
        self.finalval = self.initial_principal * self.interest_rate * self.nyears
        

c = CICalculator(2, 0.1, 1000)
c.calcfinalval()
print c.finalval

s = SICalculator(2, 0.1, 1000)
s.calcfinalval()
print s.finalval
