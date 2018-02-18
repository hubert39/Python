'''
Created on Nov 16, 2017

Write a program that will read the file, 'red-headed-league.txt', 
count the frequency of the words and store it as a csv file.

@author: Kuei-Lin Yang (Hubert)
'''

import re
import csv
import os
#import operator

class WordCounter(object):
    def __init__(self, filename):
        self.filename = filename
        self.content = ''
        self.countdict = {}
        
        with open(self.filename, 'r') as rf:
            for line in rf:
                self.content = self.content + line + ' '  
        #print self.content
        
    def removepunctuation(self):
        self.content = re.sub(r'[,.\-"]', r' ', self.content)
        #print self.content
        return self.content
        
    def findcount(self):
        self.countdict = {}
        for item in self.content.split():
            if item in self.countdict:
                self.countdict[item] = self.countdict.get(item) + 1
            else:
                self.countdict[item] = 1
        #print self.countdict
        return self.countdict
        
    def writecountfile(self, csvfilename):
        dictlist = []
        for key, value in self.countdict.items():
            listitem = [key, value]
            dictlist.append(listitem)
        #print dictlist
        
        with open(csvfilename, 'w') as wf:
            csv.writer(wf).writerows(dictlist)
    
    def listtop(self, number):
        #print sorted(self.countdict.items(), key=operator.itemgetter(1), reverse=True)[:number]
        #print sorted(self.countdict.items(), key=lambda x:x[1])
        return sorted(self.countdict, key=self.countdict.get, reverse=True)[:number]

        
def main():
    wordCounter = WordCounter( 'red-headed-league.txt' )
    print 'The content after removing punctuation is as follows.\n{}'.format(wordCounter.removepunctuation())
    print 'The frequency of each word is as follows.\n{}'.format(wordCounter.findcount())
    print 'Start to save results to {}.'.format(os.getcwd()+'/WordCounter.csv')
    wordCounter.writecountfile( 'WordCounter.csv' )
    print 'The five most popular words as following sequences.\n{}'.format(wordCounter.listtop(5))
    
if __name__ == "__main__":
    main()