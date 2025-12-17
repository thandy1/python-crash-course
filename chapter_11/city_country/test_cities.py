from chapter_11.city_country.city_functions import city_function 

def test_city_country():
    location = city_function("santiago", "chile")
    assert location == "Santiago, Chile"

