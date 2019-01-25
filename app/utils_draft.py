from pprint import pprint
import json
import requests

def get_date(date_from, date_to)
    structure = {
        'slice[]': 'offer', 
        #'filter[advertiser]': '5b2a22d373bdda49008b4604', 
        'filter[date_to]': date_to, 
        'filter[date_from]': date_from, 
        'API-key': '37796ce6525a581c56a493ccd39402eadca187de'
        }

r = requests.get('https://api.dzdata.affise.com/3.0/stats/custom', verify=False, params=structure)

data = json.loads(r.content)

pprint(data)

elems = data['stats']

offers = [
    {
        'id': elem['slice']['offer']['id'],
        'title': elem['slice']['offer']['title'],
        'charge': elem['actions']['total']['charge'],
        'revenue': elem['actions']['total']['revenue'],
        'earning': elem['actions']['total']['earning']
    } for elem in elems
]

report = Report()
for elem in elems:
    Offer.create(
        report = report,
        'id': elem['slice']['offer']['id'],
        'title': elem['slice']['offer']['title'],
        'charge': elem['actions']['total']['charge'],
        'revenue': elem['actions']['total']['revenue'],
        'earning': elem['actions']['total']['earning']
    )