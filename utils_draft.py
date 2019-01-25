from pprint import pprint
import json
import requests

structure = {'slice[]': 'offer', 'filter[advertiser]': '5b2a22d373bdda49008b4604', 'filter[date_to]': '2018-10-02', 'filter[date_from]': '2018-10-01', 'API-key': '37796ce6525a581c56a493ccd39402eadca187de'}

r = requests.get('https://api.dzdata.affise.com/3.0/stats/custom', verify=False, params=structure)

#pprint(r.url)

data = json.loads(r.content)

pprint(data)

#print(type(data['stats']))

elems = data['stats']

#levels = len(elems)

#total_charge = [elems['actions']['total']['charge'] for elems in elems]

#pprint(total_charge)

total_charge = [elems['actions']['total']['charge'] for elems in elems]

sorted_total = total_charge.sort(reverse=True)

pprint(total_charge)

offer_ids = [elems['slice']['offer']['title'] for elems in elems]

pprint(offer_ids)