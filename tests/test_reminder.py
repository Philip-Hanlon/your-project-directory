from lib.reminder import Reminder

def test_reminds_user_of_task():
    reminder = Reminder("Phil")
    reminder.remind_me_to("Walk the dog,")
    result = reminder.remind()
    assert result == "Walk the dog,, Phil!"