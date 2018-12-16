import sys
import requests
import pprint
import signal
import datetime
from output_interface import PythonSimpleIO
from option import (
    NextLaunchOption,
    LastLaunchOption,
    UpcomingLaunchesOption,
    PastLaunchesOption,
)
from menu import Menu


class App:
    def __init__(self, menu):
        self.menu = menu

    def run(self):
        self.menu.show()


def create_app():
    io_interface = PythonSimpleIO()

    menu = Menu(io_interface)
    menu.add_option("1", NextLaunchOption("Próximo Lançamento", io_interface))
    menu.add_option("2", LastLaunchOption("Último Lançamento", io_interface))
    menu.add_option("3", UpcomingLaunchesOption("Próximos Lançamentos", io_interface))
    menu.add_option("4", PastLaunchesOption("Lançamentos Passados", io_interface))

    app = App(menu)
    return app


def signal_handler(signal, frame):
    print("Exit Ctrl+C!")
    sys.exit(0)


def setup():
    signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    setup()
    app = create_app()
    app.run()
