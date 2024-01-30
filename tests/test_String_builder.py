from lib.String_builder import *

def test_string_builder_initialization():
    string = StringBuilder()
    assert string.size() == 0
    assert string.output() == ""

def test_string_builder_add():
    string = StringBuilder()
    string.add("Hello")
    assert string.size() == 5  
    assert string.output() == "Hello"    