import sys
import requests
import pprint
import signal
import datetime


def signal_handler(signal, frame):
    print("Exit Ctrl+C!")
    sys.exit(0)


def usage():
    usage_message = """
    O que você deseja visualizar?

    1 - Próximo Lançamento
    2 - Último Lançamento
    3 - Próximos Lançamentos
    4 - Lançamentos Passados
    """
    print(usage_message)


def get_user_input(message):
    user_input = None
    try:
        user_input = input(message)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

    return user_input


def get_user_input_with_message(message):
    return get_user_input(message)


def is_valid_option(number):
    if number in [1, 2, 3, 4]:
        return True

    return False


def string_to_int(arg):
    value = None
    try:
        value = int(arg)
    except ValueError:
        pass
    return value


def get_user_option_from_input(user_input):
    number = string_to_int(user_input)
    if number is not None:
        if is_valid_option(number):
            return number
        else:
            print(
                "\n\t{invalid_option} não é uma opção válida".format(
                    invalid_option=number
                )
            )
    else:
        print(
            "\n\t'{invalid_number}' não é um número válido".format(
                invalid_number=user_input
            )
        )
    return None


def menu():
    user_option = None

    while not is_valid_option(user_option):
        usage()
        user_input = get_user_input_with_message("Insira uma opção: ")
        user_option = get_user_option_from_input(user_input)

    return user_option


def get_request_url_by_option(option):
    launches_url = ["next", "latest", "upcoming", "past"]
    return "https://api.spacexdata.com/v3/launches/{}".format(launches_url[option - 1])


def get_query_params_by_option(option):
    params = {
        "filter": "flight_number,mission_name,launch_date_utc,rocket/rocket_name,launch_site/site_name_long",
        "limit": 3,
    }
    if option == 4:
        params["order"] = "desc"

    return params


def make_request(option):
    params = get_query_params_by_option(option)
    url = get_request_url_by_option(option)
    response = requests.get(url, params=params)
    return response.json()


def get_header_by_option(option):
    headers = [
        "INFORMAÇÕES DO PRÓXIMO LANÇAMENTO",
        "INFORMAÇÕES DO ÚLTIMO LANÇAMENTO",
        "INFORMAÇÕES DOS PRÓXIMOS LANÇAMENTOS",
        "INFORMAÇÕES DOS ÚLTIMOS LANÇAMENTOS",
    ]
    return headers[option - 1]


def print_launch(launch):
    launch_date = datetime.datetime.strptime(
        launch["launch_date_utc"], "%Y-%m-%dT%H:%M:%S.%fZ"
    )
    print("Número do Voo:", launch["flight_number"])
    print("Missão:", launch["mission_name"])
    print("Ano de Lançamento:", launch_date.year)
    print("Data de Lançamento (UTC):", launch_date.strftime("%d-%m-%Y às %H:%M"))
    print("Local de Lançamento:", launch["launch_site"]["site_name_long"])
    print("Nome do Foguete:", launch["rocket"]["rocket_name"])


def print_launches(launches):
    if isinstance(launches, list):
        for launch in launches:
            print_launch(launch)
            print("\n\n")
    else:
        print_launch(launches)


def main():
    while True:
        user_option = menu()
        response = make_request(user_option)
        print("\n")
        print("\t" + get_header_by_option(user_option))
        print("\n")
        print_launches(response)


def setup():
    signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    setup()
    main()
