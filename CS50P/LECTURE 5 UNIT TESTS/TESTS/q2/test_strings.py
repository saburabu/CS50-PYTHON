from strings import clean_name as cn

def test_clean_name():
    assert cn(" sabur ") == "Sabur"
    assert cn("JOHN") == "John"
    assert cn(" mary jane ") == "Mary Jane"