import sys 
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import math
import numpy as np
import matplotlib.pyplot as plt

class configuration():
    def __init__(self):
        self.values = [['',None] for i in range(11)]

