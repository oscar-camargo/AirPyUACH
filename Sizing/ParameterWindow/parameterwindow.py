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
        self.setGeometry(QRect(100,100,1280,720))
        mainlayout = QHBoxLayout(self)
        active_condition = {}
        for i in range(groupbox_n):
            mainlayout.addWidget(QGroupBox(conditions[i]))
            if types[i] == 'Ground':
                active_condition = ground._getmethod(stringbinarysearch( ground._conditions(), conditions[i] ))
                active_condition.popitem()
            elif types[i] == 'Climb':
                active_condition = climb._getmethod(stringbinarysearch( climb._conditions(), conditions[i] ))
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
            print(active_condition)
        
        self.show()
        



        #

