from lib.reminder import *
from lib.reminder_list import *

def test_reminder_list_integration():
    reminder_list = ReminderList()
    reminder1 = Reminder()
    reminder1.create_reminder("Alice", "Buy groceries", "2023-10-05")
    reminder2 = Reminder()
    reminder2.create_reminder("Bob", "Submit report", "2023-10-01")
    reminder3 = Reminder()
    reminder3.create_reminder("Charlie", "Call mom")
    reminder_list.add(reminder1)
    reminder_list.add(reminder2)
    reminder_list.add(reminder3)