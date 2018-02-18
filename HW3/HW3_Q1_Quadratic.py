'''
Created on Nov 16, 2017

The standard form of a quadratic expression is ax^2 + bx + c where a, b and c are real numbers and a is not equal to zero.
The degree of a quadratic expression is 2 and a, b and c are called the coefficients.
Part I - Addition and subtraction of quadratic expressions
Part II - Equality operator for quadratic expressions

@author: Kuei-Lin Yang (Hubert)
'''
'''
def monome(factor, degree, highdegree):
    if degree == highdegree and factor > 0:
        sign = ''
    elif factor > 0:
        sign = '+'
    else:
        sign = '-'
        factor = -factor
        
    if degree == 0:
        x = ''
    elif degree == 1:
        x = 'x'
    elif degree == 2:
        x = 'x^2'
  
    if factor == 0:
        return ''
    elif degree != 0 and (factor == 1 or factor == -1):
        return sign + '%s' % (x)
    elif degree == 0 and (factor == 1 or factor == -1):
        return sign + '%s' % (factor)
    else:
        return sign + '%s%s' % (factor, x)
'''
 
class Quadratic(object):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.highdegree = 2
        
        if self.__a == 0:
            raise ValueError("Coefficient 'a' of x^2 cannot be 0 in a quadratic equation.")    
        
        if (self.__a is None) and (self.__b != 0):
            self.highdegree = 1
        elif (self.__a is None) and (self.__b == 0):
            self.highdegree = 0

    def monome(self, factor, degree, highdegree):
        if degree == highdegree and factor > 0:
            sign = ''
        elif factor > 0:
            sign = '+'
        else:
            sign = '-'
            factor = -factor
        
        if degree == 0:
            x = ''
        elif degree == 1:
            x = 'x'
        elif degree == 2:
            x = 'x^2'
  
        if factor == 0:
            return ''
        elif degree != 0 and (factor == 1 or factor == -1):
            return sign + '%s' % (x)
        elif degree == 0 and (factor == 1 or factor == -1):
            return sign + '%s' % (factor)
        else:
            return sign + '%s%s' % (factor, x)
        
    def __str__(self):
        if self.highdegree == 2:
            return self.monome(self.__a, 2, self.highdegree) + self.monome(self.__b, 1, self.highdegree) + self.monome(self.__c, 0, self.highdegree)
        elif self.highdegree == 1:
            return self.monome(self.__b, 1, self.highdegree) + self.monome(self.__c, 0, self.highdegree)
        elif self.highdegree == 0:
            return self.monome(self.__c, 0, self.highdegree)

    def __add__(self, addend):
        if self.__a + addend.__a != 0:
            return Quadratic(self.__a+addend.__a, self.__b+addend.__b, self.__c+addend.__c)
        else:
            return Quadratic(None, self.__b+addend.__b, self.__c+addend.__c)
            
    def __sub__(self, subtrahend):
        if self.__a - subtrahend.__a != 0:
            return Quadratic(self.__a-subtrahend.__a, self.__b-subtrahend.__b, self.__c-subtrahend.__c)
        else:
            return Quadratic(None, self.__b-subtrahend.__b, self.__c-subtrahend.__c)
        
    def __eq__(self, rvalue):
        if (self.__a == rvalue.__a) and (self.__b == rvalue.__b) and (self.__c == rvalue.__c):
            return True
        else:
            return False

def main():
    Q1 = Quadratic(3, 8 , -5)
    print 'Q1=', Q1
    Q2 = Quadratic(2, 3, 7)
    print 'Q2=', Q2
    quadsum = Q1 + Q2
    print 'Q1+Q2=', quadsum
    quaddiff = Q1 - Q2
    print 'Q1-Q2=', quaddiff
        
    if Q1 == Q1:
        print '{} and {} are the same.'.format(Q1, Q1)
    else:
        print '{} and {} are different.'.format(Q1, Q1)

    if Q1 == Q2:
        print '{} and {} are the same.'.format(Q1, Q2)
    else:
        print '{} and {} are different.'.format(Q1, Q2)
      
if __name__ == "__main__":
    main()