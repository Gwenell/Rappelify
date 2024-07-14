from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication

class ThemeManager:
    @staticmethod
    def apply_theme(app, theme, primary_color=None, secondary_color=None):
        """
        Apply the selected theme to the application.
        Parameters:
            app (QApplication): The application instance to apply the theme to.
            theme (str): The name of the theme to apply.
            primary_color (QColor, optional): The primary color for custom themes.
            secondary_color (QColor, optional): The secondary color for custom themes.
        """
        if theme == "dark":
            ThemeManager.set_dark_theme(app)
        elif theme == "light":
            ThemeManager.set_light_theme(app)
        elif theme == "custom":
            ThemeManager.set_custom_theme(app, primary_color, secondary_color)
        elif theme == "oled":
            ThemeManager.set_oled_dark_theme(app)

    @staticmethod
    def set_dark_theme(app):
        """
        Apply a dark theme to the application.
        Parameters:
            app (QApplication): The application instance to apply the theme to.
        """
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        app.setPalette(dark_palette)
        app.setStyle("Fusion")  # This can help with consistent styling

    @staticmethod
    def set_light_theme(app):
        """
        Apply a light theme to the application.
        Parameters:
            app (QApplication): The application instance to apply the theme to.
        """
        app.setPalette(app.style().standardPalette())
        app.setStyle("Fusion")

    @staticmethod
    def set_custom_theme(app, primary_color, secondary_color):
        """
        Apply a custom theme to the application with specified primary and secondary colors.
        Parameters:
            app (QApplication): The application instance to apply the theme to.
            primary_color (QColor): The primary color for the custom theme.
            secondary_color (QColor): The secondary color for the custom theme.
        """
        custom_palette = QPalette()
        custom_palette.setColor(QPalette.Window, primary_color)
        custom_palette.setColor(QPalette.WindowText, secondary_color)
        custom_palette.setColor(QPalette.Base, primary_color)
        custom_palette.setColor(QPalette.AlternateBase, primary_color)
        custom_palette.setColor(QPalette.ToolTipBase, secondary_color)
        custom_palette.setColor(QPalette.ToolTipText, secondary_color)
        custom_palette.setColor(QPalette.Text, secondary_color)
        custom_palette.setColor(QPalette.Button, primary_color)
        custom_palette.setColor(QPalette.ButtonText, secondary_color)
        custom_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        custom_palette.setColor(QPalette.Link, secondary_color)
        custom_palette.setColor(QPalette.Highlight, secondary_color)
        custom_palette.setColor(QPalette.HighlightedText, primary_color)
        app.setPalette(custom_palette)
        app.setStyle("Fusion")

    @staticmethod
    def set_oled_dark_theme(app):
        """
        Apply an OLED dark theme to the application.
        Parameters:
            app (QApplication): The application instance to apply the theme to.
        """
        oled_palette = QPalette()
        oled_palette.setColor(QPalette.Window, QColor(0, 0, 0))
        oled_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        oled_palette.setColor(QPalette.Base, QColor(0, 0, 0))
        oled_palette.setColor(QPalette.AlternateBase, QColor(0, 0, 0))
        oled_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        oled_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        oled_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        oled_palette.setColor(QPalette.Button, QColor(0, 0, 0))
        oled_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        oled_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        oled_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        oled_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        oled_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        app.setPalette(oled_palette)
        app.setStyle("Fusion")
