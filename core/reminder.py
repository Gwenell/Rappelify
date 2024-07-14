from datetime import datetime, timedelta

class Reminder:
    def __init__(self, description, time, days, recurrent=False, recurrence_number=None, recurrence_unit=None):
        self.description = description
        self.time = time
        self.days = days
        self.recurrent = recurrent
        self.recurrence_number = recurrence_number
        self.recurrence_unit = recurrence_unit
        self.last_triggered = None

    def is_due(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.strftime("%a")[:3]

        if self.time <= current_time and current_day in self.days:
            if not self.recurrent:
                return self.last_triggered is None or (now - self.last_triggered).days >= 1
            else:
                if self.last_triggered is None:
                    return True
                else:
                    if self.recurrence_unit == "days":
                        next_due = self.last_triggered + timedelta(days=self.recurrence_number)
                    elif self.recurrence_unit == "weeks":
                        next_due = self.last_triggered + timedelta(weeks=self.recurrence_number)
                    elif self.recurrence_unit == "months":
                        next_due = self.last_triggered + timedelta(days=30*self.recurrence_number)
                    return now >= next_due
        return False

    def acknowledge(self):
        self.last_triggered = datetime.now()