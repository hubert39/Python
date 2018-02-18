'''
Created on Oct 19, 2017

A queue follows FIFO: 
function queueadd is to add the element
function queueretrieve is to pop the element
Consider a list with values [1,2,3]
Add 7 to the queue and then follow the FIFO rules to pop elements until the list is empty.

@author: KueiLin (Hubert)
'''

def queueadd(queue, element):
    print 'add the element {}'.format(element)
    queue.append(element)
    return queue
    
def queueretrieve(queue):
    print 'pop the element {}'.format(queue[0])
    queue.pop(0)
    return queue

listOfQueue = [1, 2, 3]
print 'the original list is {}'.format(listOfQueue)
print 'the list after adding the element {}'.format(queueadd(listOfQueue, 7))

while listOfQueue:
    print 'the list after popping the element {}'.format(queueretrieve(listOfQueue))