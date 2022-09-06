import sys 
#This block is only necessary for me to develop the repo. Once all code is done, it shall be deleted, since normal usage of these tools will be done as a package
sys.path.append('C:\\Users\\Oscar Camargo\\UACH\\AirPyUACH')
#Not sure if this is the best method. If you want to help developing, modify the imports as you like.
#
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import Sizing.Methods.constraint_analysis as ca
from Sizing.Parameters.mission_parameters import *
from Core.Tools.StringBinarySearch import stringbinarysearch
from pint import UnitRegistry


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1920,1080)


        #----Main Widget and Layout definition----#
        
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.mainlayout_widget = QWidget(self.centralwidget)
        self.mainlayout_widget.setGeometry(10,20,1900,950)
        mainlayout = QGridLayout(self.mainlayout_widget)
        mainlayout.setContentsMargins(0,0,0,0)

        #-----------------------------------------#


        #---Analyses tree definition---#

        #Analyses Groupbox
        self.tree_groupbox = QGroupBox('Analyses',self.mainlayout_widget)
        treePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        treePolicy.setHorizontalStretch(3)
        treePolicy.setVerticalStretch(0)
        treePolicy.setHeightForWidth(self.tree_groupbox.sizePolicy().hasHeightForWidth())
        self.tree_groupbox.setSizePolicy(treePolicy)
    
        #Layouts
        
        self.analyses_layout_widget = QWidget(self.tree_groupbox)
        self.analyses_layout_widget.setGeometry(QRect(10, 20, 315, 870))
        self.analyseslayout = QGridLayout(self.analyses_layout_widget)
        self.analyseslayout.setContentsMargins(0, 0, 0, 0)
        
        #Tree and buttons widgets
        self.add_after_analyses = QPushButton('Add After',self.analyses_layout_widget)
        self.remove_analyses = QPushButton('Remove',self.analyses_layout_widget)
        self.tree = QTreeWidget(self.analyses_layout_widget)
        self.tree.headerItem().setText(0,'Analyses')
        dummy_analysis = QTreeWidgetItem(self.tree)
        dummy_analysis.setText(0,'1')
        dummy_analysis.setSelected(True)
        self.export_plots = QPushButton('Export Plots as Images',self.analyses_layout_widget)
        self.export_data_csv = QPushButton('Export Data as CSV',self.analyses_layout_widget)
        self.analyseslayout.addWidget(self.add_after_analyses,0,0,1,1)
        self.analyseslayout.addWidget(self.remove_analyses,0,1,1,1)
        self.analyseslayout.addWidget(self.tree,1,0,1,2)
        self.analyseslayout.addWidget(self.export_plots,2,0,1,2)
        self.analyseslayout.addWidget(self.export_data_csv,3,0,1,2)
        self.analysis_types = []
        self.analysis_conditions = []
        self.analysis_conditions_parameters = []
        
        #------------------------------#


        #---------Tab Widget-----------#

        self.tabwidget = QTabWidget(self.mainlayout_widget)
        tabPolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tabPolicy.setHorizontalStretch(10)
        tabPolicy.setVerticalStretch(0)
        tabPolicy.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(tabPolicy)
        self.tab = QWidget()
        self.tabwidget.addTab(self.tab, "Weight Estimation")
        self.tab_2 = QWidget()
        self.tabwidget.addTab(self.tab_2, "Constraint Diagram")
        self.tab_3 = QWidget()
        self.tabwidget.addTab(self.tab_3,'Wing Geometry')

        #------------------------------#
        

        #--------Mission Table---------#

        #Table groupbox
        self.mission_groupbox = QGroupBox('Mission Segments',self.mainlayout_widget)
        missionPolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        missionPolicy.setHorizontalStretch(4)
        missionPolicy.setVerticalStretch(0)
        missionPolicy.setHeightForWidth(self.mission_groupbox.sizePolicy().hasHeightForWidth())
        self.mission_groupbox.setSizePolicy(missionPolicy)

        #Mission grid layout
        self.mission_layout_widget = QWidget(self.mission_groupbox)
        self.mission_layout_widget.setGeometry(QRect(10,30,420,420))
        self.mission_layout = QGridLayout(self.mission_layout_widget)
        
        #Buttons and table
        self.add_before_mission = QPushButton('Add Before',self.mission_layout_widget)
        self.add_after_mission = QPushButton('Add After',self.mission_layout_widget)
        self.remove_mission = QPushButton('Remove',self.mission_layout_widget)
        
        self.table_mission = QTableWidget(1,2,self.mission_layout_widget)
        self.table_mission.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)   
        self.table_mission.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.missiontypeitem = QTableWidgetItem()
        self.missionconditionitem = QTableWidgetItem()
        self.missiontypeitem.setText('Type')
        self.missionconditionitem.setText('Condition')
        self.table_mission.setHorizontalHeaderItem(0,self.missiontypeitem)
        self.table_mission.setHorizontalHeaderItem(1,self.missionconditionitem)
        self.missiontypecombo = QComboBox()
        self.missionconditioncombo = QComboBox()
        self.table_mission.setCellWidget(0,0,self.missiontypecombo)
        self.table_mission.setCellWidget(0,1,self.missionconditioncombo)
        self.missiontypecombo.addItems(['Ground','Climb','Cruise','Descent','Hover','Single Point','Transition'])
        self.missionconditioncombo.addItems(['Ground','Landing','Takeoff'])

        self.clear_mission = QPushButton('Clear All',self.mission_layout_widget)
        self.configure_mission = QPushButton('Configure',self.mission_layout_widget)
        self.save_mission = QPushButton('Save Mission',self.mission_layout_widget)
        self.mission_layout.addWidget(self.add_before_mission,0,0,1,1)
        self.mission_layout.addWidget(self.add_after_mission,0,1,1,1)
        self.mission_layout.addWidget(self.remove_mission,0,2,1,1)
        self.mission_layout.addWidget(self.table_mission,1,0,1,3)
        self.mission_layout.addWidget(self.clear_mission,2,0,1,1)
        self.mission_layout.addWidget(self.configure_mission,2,1,1,1)
        self.mission_layout.addWidget(self.save_mission,2,2,1,1)

        #------------------------------#


        #--------Constraint Table---------#

        #Table groupbox
        self.constraint_groupbox = QGroupBox('Mission Segments',self.mainlayout_widget)
        constraintPolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        constraintPolicy.setHorizontalStretch(4)
        constraintPolicy.setVerticalStretch(0)
        constraintPolicy.setHeightForWidth(self.constraint_groupbox.sizePolicy().hasHeightForWidth())
        self.constraint_groupbox.setSizePolicy(constraintPolicy)

        #Constraint grid layout and table
        self.constraint_layout_widget = QWidget(self.constraint_groupbox)
        self.constraint_layout_widget.setGeometry(QRect(10,30,420,420))
        self.constraint_layout = QGridLayout(self.constraint_layout_widget)
        self.constraintdescription = QLabel('Select a Mission Condition')
        self.conditionlabel = QLabel('')
        self.segmentcombo = QComboBox()
        self.constraint_table = QTableWidget()
        self.saveconstraint = QPushButton('Save Parameters') 

        self.constraint_layout.addWidget(self.constraintdescription,0,0,1,3)
        self.constraint_layout.addWidget(self.segmentcombo,1,0,1,3)
        self.constraint_layout.addWidget(self.conditionlabel,2,0,1,3)
        self.constraint_layout.addWidget(self.constraint_table,3,0,1,3)
        self.constraint_layout.addWidget(self.saveconstraint,4,0,1,3)
        
        self.selected_type_id = 0

        #------------------------------#


        #--------Main Grid Layout Definition---------#
        
        mainlayout.addWidget(self.tree_groupbox,0,0,2,1)
        mainlayout.addWidget(self.tabwidget,0,1,2,1)
        mainlayout.addWidget(self.mission_groupbox,0,2,1,1)
        mainlayout.addWidget(self.constraint_groupbox,1,2,1,1)
        
        #--------------------------------------------#

        #---------PINT Units Registry Declaration----------#
        #Important for handling different unit systems
        self.ureg = UnitRegistry()


        #--------UI Signals--------#
        
        QObject.connect(self.add_before_mission, SIGNAL('clicked()'),self.add_row_before_mission)
        QObject.connect(self.add_after_mission, SIGNAL('clicked()'),self.add_row_after_mission)
        QObject.connect(self.remove_mission, SIGNAL('clicked()'),self.mission_remove)
        QObject.connect(self.clear_mission, SIGNAL('clicked()'),self.mission_clear)
        QObject.connect(self.configure_mission,SIGNAL('clicked()'),self.configmission)
        
        QObject.connect(self.add_after_analyses, SIGNAL('clicked()'),self.add_row_after_analyses)
        QObject.connect(self.remove_analyses,SIGNAL('clicked()'),self.analyses_remove)
        self.missiontypecombo.currentTextChanged.connect(self.combochange)
        self.segmentcombo.currentTextChanged.connect(self.update_constraint)
        QObject.connect(self.saveconstraint,SIGNAL('clicked()'),self.take_params)
        
        self.missionparameters = 0
        #--------------------------#


        #---------UI Slots---------#

    def add_row_before_mission(self):
        if self.table_mission.currentRow() != 0:
            combotype = QComboBox()
            combotype.addItems(['Ground','Climb','Cruise','Descent','Hover','Single Point','Transition'])
            comboconditions = QComboBox()
            comboconditions.addItems(['Ground','Landing','Takeoff'])
            self.table_mission.insertRow(self.table_mission.currentRow())
            self.table_mission.setCellWidget(self.table_mission.currentRow()-1,0,combotype)
            self.table_mission.setCellWidget(self.table_mission.currentRow()-1,1,comboconditions)
            combotype.currentTextChanged.connect(self.combochange)

    def add_row_after_mission(self):
        combotype = QComboBox()
        combotype.addItems(['Ground','Climb','Cruise','Descent','Hover','Single Point','Transition'])
        comboconditions = QComboBox()
        comboconditions.addItems(['Ground','Landing','Takeoff'])
        self.table_mission.insertRow(self.table_mission.currentRow()+1)
        self.table_mission.setCellWidget(self.table_mission.currentRow()+1,0,combotype)
        self.table_mission.setCellWidget(self.table_mission.currentRow()+1,1,comboconditions)
        combotype.currentTextChanged.connect(self.combochange)

    def mission_remove(self):
        if self.table_mission.currentRow() != 0:
            self.table_mission.removeRow(self.table_mission.currentRow())
        else:
            pass

    def add_row_after_analyses(self):
        new = QTreeWidgetItem(self.tree)
        new.setText(0,'{}'.format(self.tree.topLevelItemCount()))
        

    def analyses_remove(self):
        if self.tree.currentIndex().row() != 0:
            self.tree.takeTopLevelItem(self.tree.currentIndex().row())
        else:
            pass

    def mission_clear(self):
        self.table_mission.setRowCount(1)

    def combochange(self):
        if self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Ground':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Ground','Landing','Takeoff'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Climb':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Constant CAS Constant Rate', 'Constant EAS Constant Rate', 'Constant M Constant Angle', 'Constant M Constant Rate', 'Constant M Linear altitude', 'Constant Speed Constant Angle', 'Constant Speed Constant Rate', 'Constant Speed Linear Altitude', 'Constant Throttle Constant Speed', 'Constant q Constant Angle', 'Constant q Constant Rate', 'Linear M Constant Rate', 'Linear Speed Constant Rate'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Cruise':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Constant Acc. Constant Alt.', 'Constant M Constant Alt.', 'Constant M Constant Alt. Loiter', 'Constant Pitch rate Constant Alt.', 'Constant Speed Constant Alt.', 'Constant Speed Constant Alt. Loiter', 'Constant Throttle Constant Alt.', 'Constant q Constant Alt.', 'Constant q Constant Alt. Loiter'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Descent':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Constant CAS Constant Rate', 'Constant EAS Constant Rate', 'Constant Speed Constant Angle', 'Constant Speed Constant Rate', 'Linear Mach Constant Rate'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Hover':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Climb','Descent','Hover'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Single Point':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['Set Speed Set Alt.', 'Set Speed Set Alt. NoProp', 'Set Speed Set Throttle'])
        elif self.table_mission.cellWidget(self.table_mission.currentRow(),0).currentText() == 'Transition':
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).clear()
            self.table_mission.cellWidget(self.table_mission.currentRow(),1).addItems(['C. Acc. C. Angle Linear Climb', 'C. Acc. C. Pitch Rate C. Alt.'])

    def configmission(self):
        self.row_n = self.table_mission.rowCount()
        self.types = [self.table_mission.cellWidget(i,0).currentText() for i in range(self.row_n)]
        self.segmentcombo.clear()
        self.params =  dict({})
        for element in self.duplicates(self.types):
            self.segmentcombo.addItem(element)
            self.params[element] = [[],[],[]]

        self.currentanalysis = self.tree.selectedItems()[0]
        self.currentanalysis.takeChildren()

    def tree_parameters(self):
        for i in range(self.row_n):
            self.current_segment = self.currentanalysis.child(i)
            self.current_condition = QTreeWidgetItem(self.current_segment)
            self.current_condition.setText(0,'{}'.format(self.conditions[i]))
            for param in self.mission_configuration.savedparameters[i]:
                self.current_parameter = QTreeWidgetItem(self.current_condition)
                self.current_parameter.setText(0,'{}: {} {}'.format(param[0],param[1],param[2]))

    def update_constraint(self):
        self.constraint_table.setRowCount(1)
        for i in range(3):
            self.constraint_table.removeCellWidget(i,0)
        self.selected_type_id = 0
        selected_type = self.segmentcombo.currentText()
        for type in self.types:
            if type in selected_type:
                self.selected_type_id = self.types.index(type)
        self.selected_type_condition = self.table_mission.cellWidget(self.selected_type_id,1).currentText()
        active_condition = {}
    
        if 'Ground' in self.segmentcombo.currentText():
            active_condition = ground._getmethod(stringbinarysearch( ground._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Climb' in self.segmentcombo.currentText():
            active_condition = climb._getmethod( stringbinarysearch( climb._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Cruise' in self.segmentcombo.currentText():
            active_condition = cruise._getmethod(stringbinarysearch( cruise._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Descent' in self.segmentcombo.currentText():
            active_condition = descent._getmethod(stringbinarysearch( descent._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Hover' in self.segmentcombo.currentText():
            active_condition = hover._getmethod(stringbinarysearch( hover._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Single Point' in self.segmentcombo.currentText():
            active_condition = single_point._getmethod(stringbinarysearch( single_point._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        elif 'Transition' in self.segmentcombo.currentText():
            active_condition = transition._getmethod(stringbinarysearch( transition._conditions(), self.selected_type_condition ))
            active_condition.popitem()
        else:
            pass
        self.constraint_table.setRowCount(len(active_condition))
        self.constraint_table.setColumnCount(3)
        for key,j in zip(active_condition,range(len(active_condition))):
                dummylabel = QLabel('{}'.format(key))
                unitscombo = QComboBox()
                unitscombo.addItems(['s','m','km','ft','mi','m/s','km/h','ft/s','mph','m/s^2','ft/s^2','deg','rad','deg/s','rad/s','Pa','psi','Unitless'])
                self.constraint_table.setCellWidget(j,0,dummylabel)
                self.constraint_table.setCellWidget(j,2,unitscombo)
        self.conditionlabel.setText(self.selected_type_condition)
        self.constraint_layout.addWidget(self.saveconstraint,len(active_condition)+3,0,1,3)

    def duplicates(self,arr):
        seen_items = set()
        seen_i = [1] * 7
        updated_arr = []
        for i in range(len(arr)):
            if arr[i] not in seen_items:
                seen_items.add(arr[i])
                updated_arr.append(arr[i])
            else:
                if arr[i] == 'Ground':
                    seen_i[0] += 1
                    updated_arr.append('Ground {}'.format(seen_i[0]))
                elif arr[i] == 'Climb':
                    seen_i[1] += 1
                    updated_arr.append('Climb {}'.format(seen_i[1]))
                elif arr[i] == 'Cruise':
                    seen_i[2] += 1
                    updated_arr.append('Cruise {}'.format(seen_i[2]))
                elif arr[i] == 'Descent':
                    seen_i[3] += 1
                    updated_arr.append('Descent {}'.format(seen_i[3]))
                elif arr[i] == 'Hover':
                    seen_i[4] += 1
                    updated_arr.append('Hover {}'.format(seen_i[4]))
                elif arr[i] == 'Single Point':
                    seen_i[5] += 1
                    updated_arr.append('Single Point {}'.format(seen_i[5]))
                elif arr[i] == 'Transition':
                    seen_i[6] += 1
                    updated_arr.append('Transition {}'.format(seen_i[6]))
                else:
                    pass
        return updated_arr

    def take_params(self):
        for i in range(self.constraint_table.rowCount()):
            self.params[self.segmentcombo.currentText()][0].append(self.constraint_table.cellWidget(i,0).text())
            self.params[self.segmentcombo.currentText()][1].append(self.constraint_table.item(i,1).text())
            self.params[self.segmentcombo.currentText()][2].append(self.constraint_table.cellWidget(i,2).currentText())
        print(self.params)
        #--------------------------#
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()