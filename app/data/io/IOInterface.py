'''
Created on Apr 24, 2016

@author: Kyle
'''

class IOInterface(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    
    def getInputPointer(self):
        raise NotImplementedError()
    
    def getInputType(self):
        raise NotImplementedError()
    
    def getCurrentVal(self):
        raise NotImplementedError()