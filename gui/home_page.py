from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QHBoxLayout
from utils.translations import _

class HomePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.reminders = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        self.add_reminder_btn = QPushButton(_("add_reminder"))
        self.add_reminder_btn.clicked.connect(self.main_window.show_add_reminder_page)
        button_layout.addWidget(self.add_reminder_btn)

        self.settings_btn = QPushButton(_("settings"))
        self.settings_btn.clicked.connect(self.main_window.show_settings_page)
        button_layout.addWidget(self.settings_btn)

        layout.addLayout(button_layout)

        self.reminders_list = QListWidget()
        layout.addWidget(self.reminders_list)

        self.setLayout(layout)

    def update_reminders_list(self):
        self.reminders_list.clear()
        for reminder in self.reminders:
            item_text = f"{reminder.description} - {reminder.time}"
            if reminder.recurrent:
                item_text += f" ({_('recurring')}: {_('every')} {reminder.recurrence_number} {_(reminder.recurrence_unit)})"
            self.reminders_list.addItem(item_text)

    def retranslate_ui(self):
        self.add_reminder_btn.setText(_("add_reminder"))
        self.settings_btn.setText(_("settings"))
        self.update_reminders_list()