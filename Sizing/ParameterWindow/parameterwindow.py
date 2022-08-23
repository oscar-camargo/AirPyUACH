import sys
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Sizing.Parameters.mission_parameters import *
from Core.Tools.StringBinarySearch import stringbinarysearch

class ParametersWindow(QWidget):
    def __init__(self,groupbox_n=1,types = [''],conditions=['']):
        super().__init__()
        self.setGeometry(QRect(100,100,1280,500))
        self.mainlayout = QGridLayout(self)
        active_condition = {}
        self.groupbox_n = groupbox_n
        self.types = types
        self.conditions = conditions
        for i in range(groupbox_n):
            active_groupbox = QGroupBox(conditions[i])
            self.active_groupbox_layout = QGridLayout(active_groupbox)
            self.mainlayout.addWidget(active_groupbox,0,i,1,1)
            if types[i] == 'Ground':
                active_condition = ground._getmethod(stringbinarysearch( ground._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Climb':
                active_condition = climb._getmethod( stringbinarysearch( climb._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Cruise':
                active_condition = cruise._getmethod(stringbinarysearch( cruise._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Descent':
                active_condition = descent._getmethod(stringbinarysearch( descent._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Hover':
                active_condition = hover._getmethod(stringbinarysearch( hover._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Single Point':
                active_condition = single_point._getmethod(stringbinarysearch( single_point._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Transition':
                active_condition = transition._getmethod(stringbinarysearch( transition._conditions(), conditions[i] ))
                active_condition.popitem()
            else:
                pass
            for key,j in zip(active_condition,range(len(active_condition))):
                dummylabel = QLabel('{}'.format(key))
                dummyline = QLineEdit()
                unitscombo = QComboBox()
                unitscombo.addItems(['s','m','km','ft','mi','m/s','km/h','ft/s','mph','m/s^2','ft/s^2','deg','rad','deg/s','rad/s','Pa','psi','Unitless'])
                self.active_groupbox_layout.addWidget(dummylabel,j,0,1,1)
                self.active_groupbox_layout.addWidget(dummyline,j,1,1,1)
                self.active_groupbox_layout.addWidget(unitscombo,j,2,1,1)
            
            self.saveparameters = QPushButton('Save All Parameters')
            self.mainlayout.addWidget(self.saveparameters,1,0,1,groupbox_n)
        self.show()
        self.savedparameters = [[] for i in range(self.groupbox_n)]
        QObject.connect(self.saveparameters,SIGNAL('clicked()'),self.save_parameters)

    def save_parameters(self):
        for i in range(self.groupbox_n):
            active_groupbox_layout = self.mainlayout.itemAtPosition(0,i).widget().findChild(QGridLayout)
            active_groupbox_list = [[active_groupbox_layout.itemAtPosition(j,0).widget().text(),float(active_groupbox_layout.itemAtPosition(j,1).widget().text()),\
            active_groupbox_layout.itemAtPosition(j,2).widget().currentText()] for j in range(active_groupbox_layout.rowCount())]
            self.savedparameters[i] = active_groupbox_list


