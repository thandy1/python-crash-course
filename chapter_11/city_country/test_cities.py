from city_functions import city_functions 

def test_city_country():
    location = city_functions("santiago", "chile")
    assert location == "Santiago, Chile"

def test_city_country_population():
    location = city_functions("santiago", "chile", 5000000)
    assert location == "Santiago, Chile - Population 5000000"