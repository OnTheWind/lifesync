'''
Created on Apr 25, 2016

@author: Kyle
'''
from app.data.io.IOInterface import IOInterface
from app.data.Enum import IO
import socket

class TCP(IOInterface):
    '''
    classdocs
    '''

    def __init__(self, socket, appId):
        self.type = IO.TCP
        self.socket = socket
        
    def getInputPointer(self):
        return self.pin
    
    def getInputType(self):
        return self.type
    
    def getCurrentVal(self):
        'TODO socket connection'
        raise NotImplementedError()
    
    class Factory:
        def create(self): return TCP()