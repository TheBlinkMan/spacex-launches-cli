class Menu:
    def __init__(self, io_interface):
        self._options = {}
        self._io_interface = io_interface

    def add_option(self, identifier, option):
        self._options[identifier] = option

    def execute_option(self, identifier):
        self._options[identifier].execute()

    def usage(self):
        help_message = ["\nO que você deseja visualizar?\n"]

        for key, value in self._options.items():
            help_message.append(key + " - " + value.description())

        self._io_interface.print("\n".join(help_message))

    def is_valid_option(self, option):
        valid_options = self._options.keys()
        if option in valid_options:
            return True
        return False

    def show(self):
        while True:
            self.usage()
            option = self._io_interface.input("\nInsira uma opção: ")
            if not self.is_valid_option(option):
                self._io_interface.print("\t\tNão é uma opção válida")
                continue

            self._options[option].execute()
