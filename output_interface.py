from abc import ABCMeta, abstractmethod
from sys import exit

class IInputInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def input(self, arg):
        pass

class IOutputInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def print(self, arg):
        pass

class PythonSimpleIO(IOutputInterface, IInputInterface):

    def print(self, arg):
        print(arg)

    def input(self, arg):
        user_input = None
        try:
            user_input = input(arg)
        except (EOFError, KeyboardInterrupt):
            exit(0)
        return user_input