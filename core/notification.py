from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from utils.translations import _

class NotificationManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.active_notifications = {}

    def show_notification(self, reminder):
        if reminder.description in self.active_notifications:
            return

        msg = QMessageBox(self.main_window)
        msg.setWindowTitle(_("reminder"))
        msg.setText(reminder.description)
        msg.setIcon(QMessageBox.Information)
        acknowledge_button = msg.addButton(_("acknowledge"), QMessageBox.AcceptRole)
        msg.addButton(_("later"), QMessageBox.RejectRole)

        msg.finished.connect(lambda result: self.handle_notification_result(result, reminder, msg))

        self.active_notifications[reminder.description] = msg
        msg.show()
        self.main_window.activateWindow()

    def handle_notification_result(self, result, reminder, msg):
        if msg.clickedButton() == msg.button(QMessageBox.AcceptRole):
            confirm_msg = QMessageBox.question(self.main_window, _("confirmation"),
                                               _("confirm_acknowledge"))
            if confirm_msg == QMessageBox.Yes:
                reminder.acknowledge()
            else:
                self.show_notification(reminder)
        else:
            QTimer.singleShot(3600000, lambda: self.show_notification(reminder))  # Repeat after 1 hour

        del self.active_notifications[reminder.description]