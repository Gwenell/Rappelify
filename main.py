import sys
import os

# Add the project directory to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor
from gui.main_window import MainWindow
from core.sync import SyncManager
from utils.settings import settings
from themes.theme_manager import ThemeManager

def main():
    app = QApplication(sys.argv)

    # Initialize settings
    settings.load_settings()

    # Initialize the synchronization manager
    sync_manager = SyncManager()

    # Create and display the main window
    window = MainWindow(app, sync_manager)
    window.apply_settings()  # Apply initial settings, including the theme
    window.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
