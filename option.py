from abc import ABCMeta, abstractmethod
import requests
from util import launch_to_string, launches_to_string
import copy

API_URL = "https://api.spacexdata.com/v3/launches/{}"

PARAMS = {
    "filter": "flight_number,mission_name,launch_date_utc,rocket/rocket_name,launch_site/site_name_long"
}


class IOption:
    """Declare an interface for a IMenu option."""

    __metaclass__ = ABCMeta

    def __init__(self, output_interface):
        self._output_interface = output_interface

    @abstractmethod
    def execute(self):
        pass


class NextLaunchOption(IOption):
    """Próximo Lançamento"""

    def get_next_launch(self):
        """Return the next launch"""
        url = API_URL.format("next")
        return requests.get(url, PARAMS).json()

    def execute(self):
        """Print the next launch's information to the output interface"""
        launch = self.get_next_launch()
        launch_str = launch_to_string(launch)
        self._output_interface.print("\n\tINFORMAÇÕES DO PRÓXIMO LANÇAMENTO")
        self._output_interface.print(launch_str)


class LastLaunchOption(IOption):
    """Último Lançamento"""

    def get_last_launch(self):
        """Return the last launch"""
        url = API_URL.format("latest")
        return requests.get(url, PARAMS).json()

    def execute(self):
        """Print the last launch's information to the output interface"""
        launch = self.get_last_launch()
        launch_str = launch_to_string(launch)
        self._output_interface.print("\n\tINFORMAÇÕES DO ÚLTIMO LANÇAMENTO")
        self._output_interface.print(launch_str)


class UpcomingLaunchesOption(IOption):
    """Próximos Lançamentos"""

    def get_upcoming_launches(self):
        """Return a list of upcoming launches"""
        url = API_URL.format("upcoming")
        query_params = copy.copy(PARAMS)
        query_params["limit"] = 3
        return requests.get(url, query_params).json()

    def execute(self):
        """Print the upcoming launches's information to the output interface"""
        launches = self.get_upcoming_launches()
        launches_str = launches_to_string(launches)
        self._output_interface.print("\n\tINFORMAÇÕES DOS PRÓXIMOS LANÇAMENTOS")
        self._output_interface.print(launches_str)


class PastLaunchesOption(IOption):
    """Lançamentos Passados"""

    def get_past_launches(self):
        """Return a list of past launches"""
        url = API_URL.format("past")
        query_params = copy.copy(PARAMS)
        query_params["limit"] = 3
        query_params["order"] = "desc"
        return requests.get(url, query_params).json()

    def execute(self):
        """Print the past launches's information to the output interface"""
        launches = self.get_past_launches()
        launches_str = launches_to_string(launches)
        self._output_interface.print("\n\tINFORMAÇÕES DOS ÚLTIMOS LANÇAMENTOS")
        self._output_interface.print(launches_str)
