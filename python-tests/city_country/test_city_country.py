from city_country import get_citycountry

def test_get_citycountry():
    assert get_citycountry('kathmandu','nepal')=='kathmandu,nepal'