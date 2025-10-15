# import datetime

class Reminder:
    def __init__(self):
        self.author = ""
        self.task = ""
        self.due_date = None

    def create_reminder(self, author, task, due_date = None):
        self.author = author
        self.task = task
        self.due_date = due_date

    # Commenting out date formatting methods for simplicity -> may implement later
    # def set_date_format(self, fmt):
    #     """Set strftime-style format used when due_date is a date/datetime."""
    #     self.date_format = fmt

    # def _format_date(self, d):
    #     if d is None:
    #         return None
    #     if isinstance(d, (datetime.date, datetime.datetime)):
    #         return d.strftime(self.date_format)
    #     return d  # assume already a string

    def reminder(self):
        if self.task is None:
            raise Exception("No reminder set!")
        if self.due_date is None:
            return f"{self.task}. Author: {self.author} - No due date set."
        else:
            return f"{self.task}. Author: {self.author} - Due by {self.due_date}."