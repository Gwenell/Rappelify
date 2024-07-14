from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from utils.translations import _

class NotificationManager:
    def __init__(self, main_window):
        """
        Initialize the NotificationManager with a reference to the main window.
        Parameters:
            main_window (MainWindow): The main window instance.
        """
        self.main_window = main_window
        self.active_notifications = {}

    def show_notification(self, reminder):
        """
        Display a notification for the given reminder.
        Parameters:
            reminder (Reminder): The reminder object for which to show the notification.
        """
        if reminder.description in self.active_notifications:
            return

        msg = QMessageBox(self.main_window)
        msg.setWindowTitle(_("Reminder"))
        msg.setText(reminder.description)
        msg.setIcon(QMessageBox.Information)
        acknowledge_button = msg.addButton(_("Acknowledge"), QMessageBox.AcceptRole)
        msg.addButton(_("Later"), QMessageBox.RejectRole)

        msg.finished.connect(lambda result: self.handle_notification_result(result, reminder, msg))

        self.active_notifications[reminder.description] = msg
        msg.show()
        self.main_window.activateWindow()

    def handle_notification_result(self, result, reminder, msg):
        """
        Handle the result of the notification dialog.
        Parameters:
            result (int): The result code of the dialog.
            reminder (Reminder): The reminder object related to the notification.
            msg (QMessageBox): The message box instance of the notification.
        """
        if msg.clickedButton() == msg.button(QMessageBox.AcceptRole):
            confirm_msg = QMessageBox.question(self.main_window, _("Confirmation"), _("Confirm Acknowledge"))
            if confirm_msg == QMessageBox.Yes:
                reminder.acknowledge()
            else:
                self.show_notification(reminder)
        else:
            QTimer.singleShot(3600000, lambda: self.show_notification(reminder))  # Repeat after 1 hour

        del self.active_notifications[reminder.description]
