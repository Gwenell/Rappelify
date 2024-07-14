# gui/custom_time_picker.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QDial, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator

class CustomTimePicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.time_label = QLabel("12:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 24px;")
        self.time_label.mousePressEvent = self.enable_time_edit

        self.time_edit = QLineEdit()
        self.time_edit.setAlignment(Qt.AlignCenter)
        self.time_edit.setStyleSheet("font-size: 24px;")
        self.time_edit.setVisible(False)
        self.time_edit.setMaxLength(5)
        self.time_edit.setInputMask("99:99")
        self.time_edit.returnPressed.connect(self.update_time_from_edit)

        layout.addWidget(self.time_label)
        layout.addWidget(self.time_edit)

        self.hour_dial = QDial()
        self.hour_dial.setRange(0, 23)
        self.hour_dial.setValue(12)
        self.hour_dial.setNotchesVisible(True)
        self.hour_dial.valueChanged.connect(self.update_time)
        layout.addWidget(self.hour_dial)

        self.minute_dial = QDial()
        self.minute_dial.setRange(0, 59)
        self.minute_dial.setValue(0)
        self.minute_dial.setNotchesVisible(True)
        self.minute_dial.valueChanged.connect(self.update_time)
        layout.addWidget(self.minute_dial)

        self.setLayout(layout)
        self.update_time()

    def update_time(self):
        hour = self.hour_dial.value()
        minute = self.minute_dial.value()
        self.time_label.setText(f"{hour:02}:{minute:02}")

    def update_time_from_edit(self):
        time_text = self.time_edit.text()
        try:
            hour, minute = map(int, time_text.split(":"))
            if 0 <= hour < 24 and 0 <= minute < 60:
                self.hour_dial.setValue(hour)
                self.minute_dial.setValue(minute)
                self.time_label.setText(f"{hour:02}:{minute:02}")
                self.time_edit.setVisible(False)
                self.time_label.setVisible(True)
        except ValueError:
            pass  # Handle invalid time format if necessary

    def enable_time_edit(self, event):
        self.time_edit.setText(self.time_label.text())
        self.time_label.setVisible(False)
        self.time_edit.setVisible(True)
        self.time_edit.setFocus()

    def time(self):
        hour = self.hour_dial.value()
        minute = self.minute_dial.value()
        return f"{hour:02}:{minute:02}"

    def setTime(self, hour, minute):
        self.hour_dial.setValue(hour)
        self.minute_dial.setValue(minute)
        self.update_time()
