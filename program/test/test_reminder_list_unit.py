from lib.reminder_list import *

def return_all_reminders():
    reminder_list = ReminderList()
    assert reminder_list.all() == []

def test_count_initially_zero():
    reminder_list = ReminderList()
    assert reminder_list.count() == 0