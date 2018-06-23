import pprint

_dict = {}

for i in range(41):
    _dict[i] = {
        'informations': 'Sem informações ainda',
        'rent': {
            'price': float(12.00 * (i % 5)),
            'ownerId': 'Bank'
        }
    }

# print(_dict)
pprint.pprint(_dict, indent=4)

