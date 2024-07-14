from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QTimeEdit, QPushButton, QCheckBox,
                             QGroupBox, QRadioButton, QSpinBox, QComboBox)
from utils.translations import _
from core.reminder import Reminder


class AddReminderPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.description_edit = None
        self.time_edit = None
        self.days_group = None
        self.day_checkboxes = []
        self.recurrence_group = None
        self.recurrence_radio = None
        self.recurrence_number = None
        self.recurrence_unit = None
        self.save_button = None
        self.cancel_button = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText(_("reminder_description"))
        layout.addWidget(self.description_edit)

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        layout.addWidget(self.time_edit)

        self.days_group = QGroupBox(_("days_of_week"))
        days_layout = QHBoxLayout()
        for day in _("days_of_week_list"):
            checkbox = QCheckBox(day)
            self.day_checkboxes.append(checkbox)
            days_layout.addWidget(checkbox)
        self.days_group.setLayout(days_layout)
        layout.addWidget(self.days_group)

        self.recurrence_group = QGroupBox(_("recurrence"))
        recurrence_layout = QVBoxLayout()
        self.recurrence_radio = QRadioButton(_("recurring"))
        self.recurrence_radio.toggled.connect(self.toggle_recurrence)
        recurrence_layout.addWidget(self.recurrence_radio)

        recurrence_options = QHBoxLayout()
        self.recurrence_number = QSpinBox()
        self.recurrence_number.setEnabled(False)
        recurrence_options.addWidget(self.recurrence_number)

        self.recurrence_unit = QComboBox()
        self.recurrence_unit.addItems([_("days"), _("weeks"), _("months")])
        self.recurrence_unit.setEnabled(False)
        recurrence_options.addWidget(self.recurrence_unit)

        recurrence_layout.addLayout(recurrence_options)
        self.recurrence_group.setLayout(recurrence_layout)
        layout.addWidget(self.recurrence_group)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton(_("save"))
        self.save_button.clicked.connect(self.save_reminder)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(_("cancel"))
        self.cancel_button.clicked.connect(self.main_window.show_home_page)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def toggle_recurrence(self, checked):
        self.recurrence_number.setEnabled(checked)
        self.recurrence_unit.setEnabled(checked)

    def save_reminder(self):
        reminder_data = self.get_reminder_data()
        reminder = Reminder(**reminder_data)
        self.main_window.home_page.reminders.append(reminder)
        self.main_window.home_page.update_reminders_list()
        self.main_window.show_home_page()

    def get_reminder_data(self):
        return {
            "description": self.description_edit.text(),
            "time": self.time_edit.time().toString("HH:mm"),
            "days": [cb.text() for cb in self.day_checkboxes if cb.isChecked()],
            "recurrent": self.recurrence_radio.isChecked(),
            "recurrence_number": self.recurrence_number.value() if self.recurrence_radio.isChecked() else None,
            "recurrence_unit": self.recurrence_unit.currentText() if self.recurrence_radio.isChecked() else None
        }

    def retranslate_ui(self):
        self.description_edit.setPlaceholderText(_("reminder_description"))
        self.days_group.setTitle(_("days_of_week"))
        for i, day in enumerate(_("days_of_week_list")):
            self.day_checkboxes[i].setText(day)
        self.recurrence_group.setTitle(_("recurrence"))
        self.recurrence_radio.setText(_("recurring"))
        self.recurrence_unit.clear()
        self.recurrence_unit.addItems([_("days"), _("weeks"), _("months")])
        self.save_button.setText(_("save"))
        self.cancel_button.setText(_("cancel"))