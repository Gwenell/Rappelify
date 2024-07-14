from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
                             QColorDialog, QPushButton, QLineEdit)
from PyQt5.QtGui import QColor
from themes.theme_manager import ThemeManager
from utils.settings import settings
from utils.translations import _, set_language


class SettingsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.language_label = None
        self.language_combo = None
        self.theme_label = None
        self.theme_combo = None
        self.custom_color_layout = None
        self.primary_color_btn = None
        self.secondary_color_btn = None
        self.sync_label = None
        self.sync_code_edit = None
        self.save_button = None
        self.cancel_button = None
        self.primary_color = QColor(settings.get('custom_colors', {}).get('primary', '#FFFFFF'))
        self.secondary_color = QColor(settings.get('custom_colors', {}).get('secondary', '#000000'))
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Language
        language_layout = QHBoxLayout()
        self.language_label = QLabel(_("language"))
        language_layout.addWidget(self.language_label)

        self.language_combo = QComboBox()
        self.language_combo.addItems([_("english"), _("french")])
        language_layout.addWidget(self.language_combo)
        layout.addLayout(language_layout)

        # Theme
        theme_layout = QHBoxLayout()
        self.theme_label = QLabel(_("theme"))
        theme_layout.addWidget(self.theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems([_("light"), _("dark"), _("custom"), _("oled")])
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        theme_layout.addWidget(self.theme_combo)

        layout.addLayout(theme_layout)

        # Custom colors
        self.custom_color_layout = QHBoxLayout()
        self.primary_color_btn = QPushButton(_("primary_color"))
        self.primary_color_btn.clicked.connect(self.choose_primary_color)
        self.secondary_color_btn = QPushButton(_("secondary_color"))
        self.secondary_color_btn.clicked.connect(self.choose_secondary_color)
        self.custom_color_layout.addWidget(self.primary_color_btn)
        self.custom_color_layout.addWidget(self.secondary_color_btn)
        layout.addLayout(self.custom_color_layout)

        # Sync
        sync_layout = QHBoxLayout()
        self.sync_label = QLabel(_("sync_code"))
        self.sync_code_edit = QLineEdit()
        self.sync_code_edit.setPlaceholderText(_("enter_sync_code"))
        sync_layout.addWidget(self.sync_label)
        sync_layout.addWidget(self.sync_code_edit)
        layout.addLayout(sync_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton(_("save"))
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(_("cancel"))
        self.cancel_button.clicked.connect(self.main_window.show_home_page)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def showEvent(self, event):
        super().showEvent(event)
        self.update_ui_from_settings()

    def update_ui_from_settings(self):
        # Update language combo
        current_lang = settings.get('language', 'en')
        self.language_combo.setCurrentText(_("english") if current_lang == 'en' else _("french"))

        # Update theme combo
        current_theme = settings.get('theme', 'light')
        self.theme_combo.setCurrentText(_(current_theme))

        # Update custom color buttons
        custom_colors = settings.get('custom_colors', {})
        self.primary_color = QColor(custom_colors.get('primary', '#FFFFFF'))
        self.secondary_color = QColor(custom_colors.get('secondary', '#000000'))
        self.primary_color_btn.setStyleSheet(f"background-color: {self.primary_color.name()}")
        self.secondary_color_btn.setStyleSheet(f"background-color: {self.secondary_color.name()}")

        # Enable/disable custom color options
        self.custom_color_layout.setEnabled(current_theme == 'custom')

    def on_theme_changed(self, theme):
        self.custom_color_layout.setEnabled(theme == _("custom"))

    def choose_primary_color(self):
        color = QColorDialog.getColor(self.primary_color, self, _("primary_color"))
        if color.isValid():
            self.primary_color = color
            self.primary_color_btn.setStyleSheet(f"background-color: {color.name()}")

    def choose_secondary_color(self):
        color = QColorDialog.getColor(self.secondary_color, self, _("secondary_color"))
        if color.isValid():
            self.secondary_color = color
            self.secondary_color_btn.setStyleSheet(f"background-color: {color.name()}")

    def save_settings(self):
        language = 'en' if self.language_combo.currentText() == _("english") else 'fr'
        settings.set('language', language)
        set_language(language)

        theme = self.theme_combo.currentText()
        if theme == _("light"):
            settings.set('theme', 'light')
        elif theme == _("dark"):
            settings.set('theme', 'dark')
        elif theme == _("custom"):
            settings.set('theme', 'custom')
        elif theme == _("oled"):
            settings.set('theme', 'oled')

        if settings.get('theme') == 'custom':
            settings.set('custom_colors', {
                'primary': self.primary_color.name(),
                'secondary': self.secondary_color.name()
            })

        sync_code = self.sync_code_edit.text()
        if sync_code:
            self.main_window.sync_manager.connect_to_network(sync_code, "127.0.0.1")

        settings.save_settings()

        # Apply the new settings
        self.main_window.apply_settings()
        self.main_window.show_home_page()

    def retranslate_ui(self):
        self.language_label.setText(_("language"))
        self.language_combo.clear()
        self.language_combo.addItems([_("english"), _("french")])
        self.theme_label.setText(_("theme"))
        self.theme_combo.clear()
        self.theme_combo.addItems([_("light"), _("dark"), _("custom"), _("oled")])
        self.primary_color_btn.setText(_("primary_color"))
        self.secondary_color_btn.setText(_("secondary_color"))
        self.sync_label.setText(_("sync_code"))
        self.sync_code_edit.setPlaceholderText(_("enter_sync_code"))
        self.save_button.setText(_("save"))
        self.cancel_button.setText(_("cancel"))
        self.update_ui_from_settings()