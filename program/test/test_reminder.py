from lib.reminder import *
import pytest # pyright: ignore[reportMissingImports]

def test_create_reminder_without_due_date():
    reminder = Reminder()
    reminder.create_reminder("Alice", "Buy groceries")
    result = reminder.reminder()
    assert result == "Buy groceries. Author: Alice - No due date set."

def test_create_reminder_with_due_date():
    reminder = Reminder()
    reminder.create_reminder("Bob", "Submit report", "2023-10-01")
    result = reminder.reminder()
    assert result == "Submit report. Author: Bob - Due by 2023-10-01."

def test_create_reminder_without_task():
    reminder = Reminder()
    reminder.create_reminder("Charlie", None)
    with pytest.raises(Exception) as e:
        reminder.reminder()
    error_message = str(e.value)
    assert error_message == "No reminder set!"