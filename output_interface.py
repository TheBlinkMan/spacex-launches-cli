from abc import ABCMeta, abstractmethod
from sys import exit


class IInputInterface:
    """Declare the InputInterface Interface"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def input(self, arg):
        pass


class IOutputInterface:
    """Declare the OutputInterface Interface"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def print(self, arg):
        pass


class PythonSimpleIO(IOutputInterface, IInputInterface):
    """Concrete IO that uses the standard python IO functions"""

    def print(self, arg):
        print(arg)

    def input(self, arg):
        user_input = None
        try:
            user_input = input(arg)
        except (EOFError, KeyboardInterrupt):
            exit(0)
        return user_input
