import sys
import os

# Ajouter le répertoire du projet au sys.path
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

    # Initialiser les paramètres
    settings.load_settings()

    # Initialiser le gestionnaire de synchronisation
    sync_manager = SyncManager()

    # Créer et afficher la fenêtre principale
    window = MainWindow(app, sync_manager)
    window.apply_settings()  # Appliquer les paramètres initiaux, y compris le thème
    window.show()

    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())