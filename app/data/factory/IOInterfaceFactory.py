'''
Created on Apr 25, 2016

@author: Kyle
'''
from app.data.Enum import IO
from app.data.io.Pin import Pin
from app.data.io.TCP import TCP

class IOInterfaceFactory(object):
    '''
    classdocs
    '''
    factories = {}
    def addFactory(type, shapeFactory):
        shapeFactory.factories.put[type] = shapeFactory
    addFactory = staticmethod(addFactory)
        
    def getInterface(type):
        if not id in IOInterfaceFactory.factories:
            IOInterfaceFactory.factories[type] = eval(type + '.Factory()')
        return IOInterfaceFactory.factories[type].create()
    getInterface = staticmethod(getInterface)