import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 7.0212030982546e-05, 'date': 'Tue, 2 Mar 2021 00:00:01 GMT', 'inverseRate': 14242.57333118},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.8249537859952e-05, 'date': 'Tue, 2 Mar 2021 00:00:01 GMT', 'inverseRate': 17167.518176784}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

