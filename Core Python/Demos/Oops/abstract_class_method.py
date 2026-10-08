#abstract method
#1.Need to implement compulsory in subclasses
#2.No body only definition

from abc import ABC, abstractmethod
#abstract class should be inherited from ABC class
class Vehicle(ABC):
    @abstractmethod
    def stop():
        pass
#v1 = Vehicle() #Can't Inatantiate
class Bike(Vehicle):
    def start(self):
        print('Start method...')
    def stop(self):
        print('Stop method...')
b1 = Bike()
b1.start()
b1.stop()