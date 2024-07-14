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
        """
        Initialize the UI components for the settings page, including language and theme options,
        custom color pickers, and synchronization code input.
        """
        layout = QVBoxLayout()

        # Language settings
        language_layout = QHBoxLayout()
        self.language_label = QLabel(_("Language"))
        language_layout.addWidget(self.language_label)

        self.language_combo = QComboBox()
        self.language_combo.addItems([_("English"), _("French")])
        language_layout.addWidget(self.language_combo)
        layout.addLayout(language_layout)

        # Theme settings
        theme_layout = QHBoxLayout()
        self.theme_label = QLabel(_("Theme"))
        theme_layout.addWidget(self.theme_label)

        self.theme_combo = QComboBox()
        self.theme_combo.addItems([_("Light"), _("Dark"), _("Custom"), _("OLED")])
        self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
        theme_layout.addWidget(self.theme_combo)
        layout.addLayout(theme_layout)

        # Custom color settings
        self.custom_color_layout = QHBoxLayout()
        self.primary_color_btn = QPushButton(_("Primary Color"))
        self.primary_color_btn.clicked.connect(self.choose_primary_color)
        self.secondary_color_btn = QPushButton(_("Secondary Color"))
        self.secondary_color_btn.clicked.connect(self.choose_secondary_color)
        self.custom_color_layout.addWidget(self.primary_color_btn)
        self.custom_color_layout.addWidget(self.secondary_color_btn)
        layout.addLayout(self.custom_color_layout)

        # Synchronization code settings
        sync_layout = QHBoxLayout()
        self.sync_label = QLabel(_("Sync Code"))
        self.sync_code_edit = QLineEdit()
        self.sync_code_edit.setPlaceholderText(_("Enter sync code"))
        sync_layout.addWidget(self.sync_label)
        sync_layout.addWidget(self.sync_code_edit)
        layout.addLayout(sync_layout)

        # Save and Cancel buttons
        button_layout = QHBoxLayout()
        self.save_button = QPushButton(_("Save"))
        self.save_button.clicked.connect(self.save_settings)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton(_("Cancel"))
        self.cancel_button.clicked.connect(self.main_window.show_home_page)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def showEvent(self, event):
        """
        Update the UI components with current settings when the settings page is shown.
        """
        super().showEvent(event)
        self.update_ui_from_settings()

    def update_ui_from_settings(self):
        """
        Load current settings and update the UI elements accordingly.
        """
        # Update language combo box
        current_lang = settings.get('language', 'en')
        self.language_combo.setCurrentText(_("English") if current_lang == 'en' else _("French"))

        # Update theme combo box
        current_theme = settings.get('theme', 'light')
        self.theme_combo.setCurrentText(_(current_theme))

        # Update custom color buttons
        custom_colors = settings.get('custom_colors', {})
        self.primary_color = QColor(custom_colors.get('primary', '#FFFFFF'))
        self.secondary_color = QColor(custom_colors.get('secondary', '#000000'))
        self.primary_color_btn.setStyleSheet(f"background-color: {self.primary_color.name()}")
        self.secondary_color_btn.setStyleSheet(f"background-color: {self.secondary_color.name()}")

        # Enable or disable custom color options based on the selected theme
        self.custom_color_layout.setEnabled(current_theme == 'custom')

    def on_theme_changed(self, theme):
        """
        Enable or disable custom color settings based on the selected theme.
        """
        self.custom_color_layout.setEnabled(theme == _("Custom"))

    def choose_primary_color(self):
        """
        Open a color dialog to choose the primary color and update the button's background.
        """
        color = QColorDialog.getColor(self.primary_color, self, _("Primary Color"))
        if color.isValid():
            self.primary_color = color
            self.primary_color_btn.setStyleSheet(f"background-color: {color.name()}")

    def choose_secondary_color(self):
        """
        Open a color dialog to choose the secondary color and update the button's background.
        """
        color = QColorDialog.getColor(self.secondary_color, self, _("Secondary Color"))
        if color.isValid():
            self.secondary_color = color
            self.secondary_color_btn.setStyleSheet(f"background-color: {color.name()}")

    def save_settings(self):
        """
        Save the selected settings to the settings file and apply them to the application.
        """
        # Save language setting
        language = 'en' if self.language_combo.currentText() == _("English") else 'fr'
        settings.set('language', language)
        set_language(language)

        # Save theme setting
        theme = self.theme_combo.currentText()
        if theme == _("Light"):
            settings.set('theme', 'light')
        elif theme == _("Dark"):
            settings.set('theme', 'dark')
        elif theme == _("Custom"):
            settings.set('theme', 'custom')
        elif theme == _("OLED"):
            settings.set('theme', 'oled')

        # Save custom color settings if the theme is custom
        if settings.get('theme') == 'custom':
            settings.set('custom_colors', {
                'primary': self.primary_color.name(),
                'secondary': self.secondary_color.name()
            })

        # Save synchronization code
        sync_code = self.sync_code_edit.text()
        if sync_code:
            self.main_window.sync_manager.connect_to_network(sync_code, "127.0.0.1")

        settings.save_settings()

        # Apply the new settings
        self.main_window.apply_settings()
        self.main_window.show_home_page()

    def retranslate_ui(self):
        """
        Update all UI elements with the current language settings.
        """
        self.language_label.setText(_("Language"))
        self.language_combo.clear()
        self.language_combo.addItems([_("English"), _("French")])
        self.theme_label.setText(_("Theme"))
        self.theme_combo.clear()
        self.theme_combo.addItems([_("Light"), _("Dark"), _("Custom"), _("OLED")])
        self.primary_color_btn.setText(_("Primary Color"))
        self.secondary_color_btn.setText(_("Secondary Color"))
        self.sync_label.setText(_("Sync Code"))
        self.sync_code_edit.setPlaceholderText(_("Enter sync code"))
        self.save_button.setText(_("Save"))
        self.cancel_button.setText(_("Cancel"))
        self.update_ui_from_settings()
