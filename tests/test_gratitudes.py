from lib.gratitudes import *

def test_gratitudes_one():
    gratitude_list = Gratitudes()
    assert gratitude_list.gratitudes == []

def test_gratitudes_add():
    gratitude_list = Gratitudes()
    gratitude_list.add("Football")
    assert gratitude_list.gratitudes == ["Football"]    

def test_gratitudes_add():
    gratitude_list = Gratitudes()
    gratitude_list.add("Football")
    gratitude_list.add("Golf")
    assert gratitude_list.gratitudes == ["Football", "Golf"] 

def test_gratitudes_format():
    gratitude_list = Gratitudes()
    gratitude_list.add("Football")
    gratitude_list.add("Golf")
    formatted_gratitudes = gratitude_list.format()
    assert formatted_gratitudes == "Be grateful for: Football, Golf"        

