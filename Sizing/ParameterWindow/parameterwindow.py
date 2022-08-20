import sys
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH\\Sizing')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Parameters.mission_parameters import *

class ParametersWindow(QWidget):
    def __init__(self,groupbox_n=1,conditions=['']):
        super().__init__()
        self.setGeometry(QRect(100,100,1280,720))
        mainlayout = QHBoxLayout(self)
        for i in range(groupbox_n):
            mainlayout.addWidget(QGroupBox(conditions[i]))




        self.show()

