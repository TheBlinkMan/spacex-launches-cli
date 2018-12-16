from abc import ABCMeta, abstractmethod
import requests
from util import launch_to_string, launches_to_string

API_URL = "https://api.spacexdata.com/v3/launches/{}"

PARAMS = {
    "filter": "flight_number,mission_name,launch_date_utc,rocket/rocket_name,launch_site/site_name_long"
}


class IOption:
    __metaclass__ = ABCMeta

    def __init__(self, description, output_interface):
        self._description = description
        self._output_interface = output_interface

    @abstractmethod
    def execute(self):
        pass

    def description(self):
        return self._description


class NextLaunchOption(IOption):
    def get_next_launch(self):
        return requests.get(API_URL.format("next"), PARAMS).json()

    def execute(self):
        launch = self.get_next_launch()
        launch_str = launch_to_string(launch)
        self._output_interface.print("\n\tINFORMAÇÕES DO PRÓXIMO LANÇAMENTO")
        self._output_interface.print(launch_str)
