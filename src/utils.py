import os
import glob

from PySide6.QtGui import QFontDatabase

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.join(ROOT_PATH, "app")


def load_fonts():
    font_path = os.path.join(APP_PATH, "fonts")

    for font in glob.glob(os.path.join(font_path, "**/*.ttf")):
        QFontDatabase.addApplicationFont(font)
