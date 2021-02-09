from task.utils import *
from task.exceptions import WrongCityNameError
import requests
from textwrap import indent

COUNTRY_CITY_URL = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=worldcitiespop&q={}&facet=country"
COUNTRY_CURRENCY_URL = 'https://restcountries.eu/rest/v2/name/{}?fullText=true'


def pretty_print(data, city):
    """
    Pretty print of formatted data
    :param data: dict of params to print
    :param city: name of printed city
    """
    print(f"=>  {city.capitalize()}")
    print(f"=>{'-' * 10}")
    for key, value in data.items():
        print(indent(f"{key}: {value}", '=>'))
    print(f"=>{'-' * 10}")


def find_country_info(city_name):
    """
    Finds code of country in which searched city is located
    :param city_name: name of the searching city
    :return: dict of insights about city
    :raise WrongCityNameError if city was not found
    """
    response = requests.get(url=COUNTRY_CITY_URL.format(city_name))

    try:
        data = response.json()['records'][0]
        return {
            'CountryCode': data['fields']['country'].upper()
        }
    except Exception:
        raise WrongCityNameError("Invalid City Name")


def find_currency_country(data):
    """
    Finds country name & currency by country code
    :param data: dict of insights about city
    :return: tuple of country name, country currency
    """
    country_code = data['CountryCode']
    response = requests.get(url=COUNTRY_CURRENCY_URL.format(country_code))
    data = response.json()[0]
    return data['name'], data['currencies'][0]['code'], data['population']


def main():
    """
    Gets user's input(city name) and returns list of country insights
    """
    args = parse_arguments()
    if args.file is None:
        cities = " ".join(args.cities).lower().split(", ")
    else:
        cities = read_file(args.file)

    for city in cities:
        try:
            data = find_country_info(city)
            data['Country'], data['Currency'], data['Population'] = find_currency_country(data)
            pretty_print(data, city)
        except Exception as exception:
            print(f"=>{'-' * 10}")
            print(exception)
            print(f"=>{'-' * 10}")


if __name__ == '__main__':
    main()
