from lib.greet import greet

def test_greets_person_given_name():
    result = greet("Phil")
    assert result == "Hello, Phil!"