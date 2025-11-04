from name_function import get_formatted_name

def test_get_formatted_name():
    formatted = get_formatted_name('samir','sapkota')
    assert formatted == "Samir Sapkota"
