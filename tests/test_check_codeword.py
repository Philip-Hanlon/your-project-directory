from lib.check_codeword import check_codeword

"""if codeword is correct
   returns "correct! Come in," 
"""

def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

    """if the codeword is wrong
       returns "WRONG!"
    """
def test_with_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"


    """If the codeword has the right first and  last letter
       returns "Close, but nope."
    """

def test_with_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

"""If the codeword has the right first letter and the wrong last one 
   returns "WRONG!"
"""    
def test_with_wrong_firstletter_codeword():
    result = check_codeword("hat")
    assert result == "WRONG!"