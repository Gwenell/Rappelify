# gui/main_window.py

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from gui.home_page import HomePage
from gui.add_reminder_page import AddReminderPage
from gui.settings_page import SettingsPage
from core.notification import NotificationManager
from themes.theme_manager import ThemeManager
from utils.settings import settings
from utils.translations import _

class MainWindow(QMainWindow):
    def __init__(self, app, sync_manager):
        super().__init__()
        self.app = app
        self.sync_manager = sync_manager
        self.notification_manager = NotificationManager(self)
        self.init_ui()

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_reminders)
        self.update_timer.start(60000)  # Check every minute

    def init_ui(self):
        self.setWindowTitle("Rappelify")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)

        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.home_page = HomePage(self)
        self.add_reminder_page = AddReminderPage(self)
        self.settings_page = SettingsPage(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.add_reminder_page)
        self.stacked_widget.addWidget(self.settings_page)

        self.setCentralWidget(central_widget)

        self.show_home_page()

    def show_home_page(self):
        self.stacked_widget.setCurrentWidget(self.home_page)

    def show_add_reminder_page(self):
        self.stacked_widget.setCurrentWidget(self.add_reminder_page)

    def show_settings_page(self):
        self.stacked_widget.setCurrentWidget(self.settings_page)

    def update_reminders(self):
        for reminder in self.home_page.reminders:
            if reminder.is_due():
                self.notification_manager.show_notification(reminder)
        self.home_page.update_reminders_list()

    def apply_settings(self):
        theme = settings.get('theme', 'light')
        custom_colors = settings.get('custom_colors', {})
        primary_color = QColor(custom_colors.get('primary', '#FFFFFF'))
        secondary_color = QColor(custom_colors.get('secondary', '#000000'))
        ThemeManager.apply_theme(self.app, theme, primary_color, secondary_color)
        self.retranslate_ui()

    def retranslate_ui(self):
        self.setWindowTitle(_("Rappelify"))
        self.home_page.retranslate_ui()
        self.add_reminder_page.retranslate_ui()
        self.settings_page.retranslate_ui()
