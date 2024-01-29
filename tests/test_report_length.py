from lib.report_length import report_length

def test_first_test_report_length():
    result = report_length("Hello")
    assert result == "This string was 5 characters long."

def test_second_test_report_length():
    result = report_length(" ") 
    assert result == "This string was 1 characters long."  
