# from reminder import Reminder
        # Commented out due to inheritance issue in tests

class ReminderList:
    def __init__(self):
        self.reminders = []

    def add(self, reminder):
        self.reminders.append(reminder)

    def all(self):
        return [reminder.reminder() for reminder in self.reminders]
    
    def reset(self):
        self.reminders = []

    def count(self):
        return len(self.reminders)
    
    def remove(self, reminder):
        self.reminders.remove(reminder)

    def due_today(self, today_date):
        return [reminder.reminder() for reminder in self.reminders if reminder.due_date == today_date]
    
    def overdue(self, today_date):
        return [reminder.reminder() for reminder in self.reminders if reminder.due_date is not None and reminder.due_date < today_date]
    
    def upcoming(self, today_date):
        return [reminder.reminder() for reminder in self.reminders if reminder.due_date is not None and reminder.due_date > today_date]