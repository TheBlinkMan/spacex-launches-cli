import datetime


def launch_to_string(launch):
    launch_date = datetime.datetime.strptime(
        launch["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    flight_number = launch["flight_number"]
    mission_name = launch["mission_name"]
    launch_year = launch_date.year
    formatted_launch_date = launch_date.strftime("%d-%m-%Y às %H:%M")
    launch_site_name_long = launch["launch_site"]["site_name_long"]
    rocket_name = launch["rocket"]["rocket_name"]

    launch_str = """
    Número do Voo: {}
    Missão: {}
    Ano de Lançamento: {}
    Data de Lançamento (UTC): {}
    Local de Lançamento: {}
    Nome do Foguete: {}
    """.format(
        flight_number,
        mission_name,
        launch_year,
        formatted_launch_date,
        launch_site_name_long,
        rocket_name,
    )

    return launch_str


def launches_to_string(launches):
    launches_str = []
    for launch in launches:
        launches_str.append(launch_to_string(launch))

    return "\n\n".join(launches_str)
