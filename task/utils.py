from os import path
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='GeoInsightFetcher')
    parser.add_argument(help='Cities names', nargs="+", dest="cities")
    parser.add_argument('-f', "--file", help='file with cities names', dest="file")
    return parser.parse_args()


def file_check(file_name):
    if path.isfile(file_name) and file_name.lower().endswith((".txt",)):
        return True
    return False


def read_file(file_name):
    if file_check(file_name):
        with open(file_name, "r+") as file:
            result = file.read().split('\n')
        return result
    return [None]
