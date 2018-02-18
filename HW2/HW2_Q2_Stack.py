'''
Created on Nov 2, 2017
A stack follows LIFO (last-in, first-out)

@author: Kuei-Lin Yang (Hubert)
'''

class Sclass(object):
    def __init__(self, llist):
        self.list = llist
        
    def sadd(self, element):
        self.list.append(element)
        return self.list
    
    def sretrieve(self):
        self.list.pop(len(self.list)-1)
        return self.list
    
llist = [4, 6, 9]
print 'the original list is {}'.format(llist)
stack = Sclass(llist) 
print 'the list after adding the element {}'.format(stack.sadd(12))

while llist:
    print 'the list after popping the element {}'.format(stack.sretrieve())
