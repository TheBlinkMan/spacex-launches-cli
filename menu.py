from abc import ABCMeta, abstractmethod


class IMenu:
    """Declare the menu interface"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def add_option(self, identifier, option):
        """Add an IOption to the menu."""
        pass

    @abstractmethod
    def execute_option(self, identifier):
        """Execute the IOptions's execute method that matches the identifier."""
        pass

    @abstractmethod
    def show(self):
        """Show the menu to the user."""
        pass


class Menu(IMenu):
    def __init__(self, io_interface):
        """
        Initializes the data structure that holds the options.

        Arguments:
        io_interface -- An object that implements IOuputInterface and IInputInterface
        """
        self._options = {}
        self._io_interface = io_interface

    def add_option(self, identifier, option):
        """
        Add an IOption to the _options's dictionary

        Arguments:
        identifier -- string
        option -- IOption
        """
        self._options[identifier] = option

    def execute_option(self, identifier):
        """
        Execute the option that matches the identifier

        Arguments:
        identifier -- string
        """

        self._options[identifier].execute()

    def _usage(self):
        help_message = ["\nO que você deseja visualizar?\n"]

        for key, value in self._options.items():
            assert isinstance(value.__doc__, str), "Define a docstring for option with identifier {}".format(key)
            help_message.append(key + " - " + value.__doc__)

        self._io_interface.print("\n".join(help_message))

    def _is_valid_option(self, identifier):
        """
        Return True if the option is valid, False otherwise.

        Arguments:
        identifier -- string that identifies an option
        """
        valid_options = self._options.keys()
        if identifier in valid_options:
            return True
        return False

    def show(self):
        """
        Print the options to the output interface and
        interactively executes the options based on the user input.
        """
        while True:
            self._usage()
            option = self._io_interface.input("\nInsira uma opção: ")
            if not self._is_valid_option(option):
                self._io_interface.print("\t\tNão é uma opção válida")
                continue

            self._options[option].execute()
