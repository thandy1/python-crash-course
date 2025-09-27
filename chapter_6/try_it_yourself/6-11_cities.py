"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

cities = {
    'new york': {
        'country': 'united states',
        'population': 19870000,
        'fact': 'most ethnically diverse city',
    },
    'dallas': {
        'country': 'united states',
        'population': 1326087,
        'fact': 'largest urban arts district',
    },
    'austin': {
        'country': 'united states',
        'population': 993588,
        'fact': 'renowned for its vibrant food scene',
    },
}

for city, information in cities.items():
    print(f"{city.title()} is located in the {information['country']}"
          f" and has a population of {information['population']:,} people."
          f" One interesting fact: {information['fact']}.\n")