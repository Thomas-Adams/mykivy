import yaml
import json
from models import Country, start_db, stop_db


def load_countries():
    property_list = (
        'name',
        'tld',
        'abbr'
        'phone',
        'curr_code',
        'curr_name'
    )
    countries = dict()
    with open('./data/countries/country-by-abbreviation.json') as json_file:
        for line in yaml.safe_load(json_file):
            country = dict([('name', line['country']), ('abbr', line['abbreviation'])])
            countries[line['country']] = country

    with open('./data/countries/country-by-domain-tld.json') as json_file:
        for line in yaml.safe_load(json_file):
            if line['country'] in countries:
                country = countries[line['country']]
                if not line['tld'] is None:
                    country['tld'] = line['tld'][1:]

    with open('./data/countries/country-by-currency-code.json') as json_file:
        for line in yaml.safe_load(json_file):
            if line['country'] in countries:
                country = countries[line['country']]
                if not line['currency_code'] is None:
                    country['curr_code'] = line['currency_code']

    with open('./data/countries/country-by-currency-name.json') as json_file:
        for line in yaml.safe_load(json_file):
            if line['country'] in countries:
                country = countries[line['country']]
                if not line['currency_name'] is None:
                    country['curr_name'] = line['currency_name']

    with open('./data/countries/country-by-calling-code.json') as json_file:
        for line in yaml.safe_load(json_file):
            if line['country'] in countries:
                country = countries[line['country']]
                if not line['calling_code'] is None:
                    country['phone'] = line['calling_code']

    start_db()

    for k, v in countries.items():
        country = Country(name=v['name'])
        if 'tld' in v:
            country.tld=v['tld']
        if 'abbr' in v:
            country.abbr=v['abbr']
        if 'phone' in v:
            country.phone = v['phone']
        country.save()

    stop_db()

    print(json.dumps(countries, indent=4, sort_keys=True))


if __name__ == '__main__':
    load_countries()
