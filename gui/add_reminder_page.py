# gui/add_reminder_page.py

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QCheckBox, QGroupBox, QRadioButton,
                             QSpinBox, QComboBox)
from PyQt5.QtCore import Qt
from utils.translations import _
from core.reminder import Reminder
from gui.custom_time_picker import CustomTimePicker  # Ensure this import is correct
import platform

class AddReminderPage(QWidget):
    def __init__(self, main_window):
        """
        Initialize the AddReminderPage with a reference to the main window.
        Parameters:
            main_window (MainWindow): The main window instance.
        """
        super().__init__()
        self.main_window = main_window
        self.description_edit = None
        self.time_checkbox = None
        self.time_picker = None
        self.days_group = None
        self.day_checkboxes = []
        self.recurrence_group = None
        self.recurrence_radio = None
        self.recurrence_number = None
        self.recurrence_unit = None
        self.save_button = None
        self.cancel_button = None
        self.device_type = 'phone' if platform.system() in ['Android', 'iOS'] else 'pc'
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)

        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText(_("Reminder description"))
        layout.addWidget(self.description_edit)

        self.time_checkbox = QCheckBox(_("Enable reminder time"))
        self.time_checkbox.setChecked(self.device_type == 'phone')
        self.time_checkbox.stateChanged.connect(self.toggle_time_picker)
        layout.addWidget(self.time_checkbox)

        self.time_picker = CustomTimePicker()
        self.time_picker.setEnabled(self.device_type == 'phone')
        layout.addWidget(self.time_picker)

        self.days_group = QGroupBox(_("Days of the Week"))
        days_layout = QHBoxLayout()
        for day in _("days_of_week_list"):
            checkbox = QCheckBox(day)
            self.day_checkboxes.append(checkbox)
            days_layout.addWidget(checkbox)
        self.days_group.setLayout(days_layout)
        layout.addWidget(self.days_group)

        self.recurrence_group = QGroupBox(_("Recurrence"))
        recurrence_layout = QVBoxLayout()
        self.recurrence_radio = QRadioButton(_("Recurring"))
        self.recurrence_radio.toggled.connect(self.toggle_recurrence)
        recurrence_layout.addWidget(self.recurrence_radio)

        recurrence_options = QHBoxLayout()
        self.recurrence_number = QSpinBox()
        self.recurrence_number.setEnabled(False)
        recurrence_options.addWidget(self.recurrence_number)

        self.recurrence_unit = QComboBox()
        self.recurrence_unit.addItems([_("Days"), _("Weeks"), _("Months")])
        self.recurrence_unit.setEnabled(False)
        recurrence_options.addWidget(self.recurrence_unit)

        recurrence_layout.addLayout(recurrence_options)
        self.recurrence_group.setLayout(recurrence_layout)
        layout.addWidget(self.recurrence_group)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton(_("Save"))
        self.save_button.clicked.connect(self.save_reminder)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(_("Cancel"))
        self.cancel_button.clicked.connect(self.main_window.show_home_page)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def toggle_time_picker(self, state):
        self.time_picker.setEnabled(state == Qt.Checked)

    def toggle_recurrence(self, checked):
        self.recurrence_number.setEnabled(checked)
        self.recurrence_unit.setEnabled(checked)

    def save_reminder(self):
        reminder_data = self.get_reminder_data()
        reminder = Reminder(**reminder_data, device_type=self.device_type)
        self.main_window.home_page.reminders.append(reminder)
        self.main_window.home_page.update_reminders_list()
        self.main_window.show_home_page()

    def get_reminder_data(self):
        time = None
        if self.time_checkbox.isChecked():
            time = self.time_picker.time()
        return {
            "description": self.description_edit.text(),
            "time": time,
            "days": [cb.text() for cb in self.day_checkboxes if cb.isChecked()],
            "recurrent": self.recurrence_radio.isChecked(),
            "recurrence_number": self.recurrence_number.value() if self.recurrence_radio.isChecked() else None,
            "recurrence_unit": self.recurrence_unit.currentText() if self.recurrence_radio.isChecked() else None
        }

    def retranslate_ui(self):
        self.description_edit.setPlaceholderText(_("Reminder description"))
        self.time_checkbox.setText(_("Enable reminder time"))
        self.days_group.setTitle(_("Days of the Week"))
        for i, day in enumerate(_("days_of_week_list")):
            self.day_checkboxes[i].setText(day)
        self.recurrence_group.setTitle(_("Recurrence"))
        self.recurrence_radio.setText(_("Recurring"))
        self.recurrence_unit.clear()
        self.recurrence_unit.addItems([_("Days"), _("Weeks"), _("Months")])
        self.save_button.setText(_("Save"))
        self.cancel_button.setText(_("Cancel"))
