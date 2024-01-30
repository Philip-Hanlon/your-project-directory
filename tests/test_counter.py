from lib.counter import *

def test_counter_initial_count():
    counter = Counter()
    assert counter.count == 0

"""test to add number """    

def test_counter_add():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5    

def test_counter_report():
    counter = Counter()
    counter.add(10)
    counter.add(7)
    report = counter.report()
    assert report == "Counted to 17 so far."    