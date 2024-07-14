from datetime import datetime, timedelta

class Reminder:
    def __init__(self, description, time=None, days=None, recurrent=False, recurrence_number=None, recurrence_unit=None, device_type='pc'):
        """
        Initialize a Reminder object.
        Parameters:
            description (str): The description of the reminder.
            time (str, optional): The time of the reminder in HH:MM format. Defaults to "12:00" for phone and current time for PC.
            days (list, optional): A list of days the reminder is active. Defaults to an empty list.
            recurrent (bool, optional): Whether the reminder is recurrent. Defaults to False.
            recurrence_number (int, optional): The recurrence interval number. Defaults to None.
            recurrence_unit (str, optional): The recurrence unit ('days', 'weeks', 'months'). Defaults to None.
            device_type (str, optional): The type of device ('pc' or 'phone'). Defaults to 'pc'.
        """
        self.description = description
        self.time = time if time else ("12:00" if device_type == 'phone' else datetime.now().strftime("%H:%M"))
        self.days = days if days else []
        self.recurrent = recurrent
        self.recurrence_number = recurrence_number
        self.recurrence_unit = recurrence_unit
        self.last_triggered = None

    def is_due(self):
        """
        Check if the reminder is due based on the current time and day.
        Returns:
            bool: True if the reminder is due, False otherwise.
        """
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        current_day = now.strftime("%a")[:3]

        if self.time <= current_time and (not self.days or current_day in self.days):
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
                        next_due = self.last_triggered + timedelta(days=30 * self.recurrence_number)
                    return now >= next_due
        return False

    def acknowledge(self):
        """
        Acknowledge the reminder, setting the last triggered time to now.
        """
        self.last_triggered = datetime.now()
