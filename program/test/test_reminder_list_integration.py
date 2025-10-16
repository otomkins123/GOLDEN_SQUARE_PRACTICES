from lib.reminder import *
from lib.reminder_list import *
import pytest # type: ignore

@pytest.fixture
def init_setup():
    # Initialize ReminderList and some Reminder objects
    reminder_list = ReminderList()
    reminder1 = Reminder(); reminder1.create_reminder("Alice", "Buy groceries", "2023-10-05")
    reminder2 = Reminder(); reminder2.create_reminder("Bob", "Submit report", "2023-10-01")
    reminder3 = Reminder(); reminder3.create_reminder("Charlie", "Call mom")
    # Add reminders to the list
    for reminder in [reminder1, reminder2, reminder3]:
        reminder_list.add(reminder)
    # Return all objects needed for tests
    return reminder_list, reminder1, reminder2, reminder3

def test_reminder_list_returns_all_reminders(init_setup):
    # Check all reminders are added correctly
    assert init_setup[0].count() == 3
    assert init_setup[0].all() == [
        "Buy groceries. Author: Alice - Due by 2023-10-05.",
        "Submit report. Author: Bob - Due by 2023-10-01.",
        "Call mom. Author: Charlie - No due date set."
    ]

@pytest.mark.parametrize("method, arg, expected", [
    ("due_today", "2023-10-01", ["Submit report. Author: Bob - Due by 2023-10-01."]),
    ("overdue", "2023-10-03", ["Submit report. Author: Bob - Due by 2023-10-01."]),
    ("upcoming", "2023-10-03", ["Buy groceries. Author: Alice - Due by 2023-10-05."])
])
def test_reminder_list_filters(init_setup, method, arg, expected):
    # Check due_today, overdue, and upcoming methods to return correct reminders
    assert getattr(init_setup[0], method)(arg) == expected

def test_reminder_list_remove_reminder(init_setup):
    # Remove a reminder and check the list updates correctly
    init_setup[0].remove(init_setup[2])
    assert init_setup[0].count() == 2
    assert init_setup[0].all() == [
        "Buy groceries. Author: Alice - Due by 2023-10-05.",
        "Call mom. Author: Charlie - No due date set."
    ]

def test_reminder_list_reset(init_setup):
    # Reset the list and check it's empty
    init_setup[0].reset()
    assert init_setup[0].count() == 0
    assert init_setup[0].all() == []