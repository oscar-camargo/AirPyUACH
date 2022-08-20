from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class ParametersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QRect(100,100,500,300))
        self.setWindowTitle('This is a second window')
        self.label = QLabel('Second Screen Working',self)
        self.show()

        