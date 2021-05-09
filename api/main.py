from bs4 import BeautifulSoup
import requests
import json
import os


def get_data_from_web(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find('div', class_='row no-margin')

    return data


def parse_data(data):
    titles = data.find_all('b', class_='title')
    titles = [title.text.strip() for title in titles]

    numbers = data.find_all('font', class_='Numbers')
    numbers = [int(number.text) for number in numbers]

    last_updated_date = data.find('font', class_='dataAtt').text.strip()

    return (titles, numbers, last_updated_date)


def file_exists(filepath):
    return os.path.isfile(filepath)


def read_json_file(filepath):
    with open(filepath, 'r', encoding='utf8') as openfile:
        data_json = json.load(openfile)

    return data_json


def get_keys_from_json(key, json_data):
    keys = []

    for entry in json_data:
        if (key in entry):
            keys.append(entry[key])

    return keys


def get_numbers_diff(old_numbers, new_numbers):
    diff = []
    numbers_length = len(new_numbers)

    for i in range(numbers_length):
        diff.append(new_numbers[i] - old_numbers[i])

    return diff


def get_updates(filepath, new_numbers):
    if (file_exists(filepath)):
        old_json_data = read_json_file(filepath)
        old_numbers = get_keys_from_json('number', old_json_data)
        diff = get_numbers_diff(old_numbers, new_numbers)
    else:
        diff = [0] * len(new_numbers)

    return diff


def create_dict(titles, numbers, updates, last_update_date):
    entries_length = len(titles)
    result = [{'lastUpdatedDate': last_update_date}]

    for entry in range(entries_length):
        value = {'title': titles[entry],
                 'number': numbers[entry], 'update': updates[entry]}
        result.append(value)

    return result


def write_json_file(filepath, result):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=2)


def web_scraper():
    url = 'https://silveiramartins.rs.gov.br/coronavirus/boletim-epidemiologico'
    filepath = 'data.json'

    data = get_data_from_web(url)
    (titles, new_numbers, last_updated_date) = parse_data(data)

    updates = get_updates(filepath, new_numbers)
    result = create_dict(titles, new_numbers, updates, last_updated_date)

    write_json_file(filepath, result)

    return result
