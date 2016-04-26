'''
Created on Apr 25, 2016

@author: Kyle
'''
from app.data.io.IOInterface import IOInterface
from app.data.Enum import IO

class Pin(IOInterface):
    '''
    classdocs
    '''

    def __init__(self, pin):
        self.type=IO.PIN
        self.pin=pin
        
    def getInputType(self):
        return self.type
        
    def getInputPointer(self):
        return self.pin
    
    def getCurrentVal(self):
        'TODO GPIO setup'
        raise NotImplementedError()
    
    class Factory:
        def create(self): return Pin()