from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout
from utils.translations import _

class HomePage(QWidget):
    def __init__(self, main_window):
        """
        Initialize the HomePage with a reference to the main window.
        Parameters:
            main_window (MainWindow): The main window instance.
        """
        super().__init__()
        self.main_window = main_window
        self.reminders = []
        self.init_ui()

    def init_ui(self):
        """
        Set up the user interface for the HomePage, including layout and widgets.
        """
        layout = QVBoxLayout()

        # Button layout for Add Reminder and Settings
        button_layout = QHBoxLayout()
        self.add_reminder_btn = QPushButton(_("Add Reminder"))
        self.add_reminder_btn.clicked.connect(self.main_window.show_add_reminder_page)
        button_layout.addWidget(self.add_reminder_btn)

        self.settings_btn = QPushButton(_("Settings"))
        self.settings_btn.clicked.connect(self.main_window.show_settings_page)
        button_layout.addWidget(self.settings_btn)

        layout.addLayout(button_layout)

        # List widget to display reminders
        self.reminders_list = QListWidget()
        layout.addWidget(self.reminders_list)

        self.setLayout(layout)

    def update_reminders_list(self):
        """
        Update the list widget with current reminders.
        """
        self.reminders_list.clear()
        for reminder in self.reminders:
            item_text = f"{reminder.description} - {reminder.time}"
            if reminder.recurrent:
                item_text += f" ({_('Recurring')}: {_('Every')} {reminder.recurrence_number} {_(reminder.recurrence_unit)})"
            self.reminders_list.addItem(item_text)

    def retranslate_ui(self):
        """
        Update the text of UI elements to match the current language settings.
        """
        self.add_reminder_btn.setText(_("Add Reminder"))
        self.settings_btn.setText(_("Settings"))
        self.update_reminders_list()
