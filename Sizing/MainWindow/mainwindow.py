import sys 
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(1920,1080)
        #self.parameters_window = ParametersWindow()


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
        self.add_before_analyses = QPushButton('Add Before',self.analyses_layout_widget)
        self.add_after_analyses = QPushButton('Add After',self.analyses_layout_widget)
        self.remove_analyses = QPushButton('Remove',self.analyses_layout_widget)
        self.tree = QTreeWidget(self.analyses_layout_widget)
        self.export_plots = QPushButton('Export Plots as Images',self.analyses_layout_widget)
        self.export_data_csv = QPushButton('Export Data as CSV',self.analyses_layout_widget)
        self.analyseslayout.addWidget(self.add_before_analyses,0,0,1,1)
        self.analyseslayout.addWidget(self.add_after_analyses,0,1,1,1)
        self.analyseslayout.addWidget(self.remove_analyses,0,2,1,1)
        self.analyseslayout.addWidget(self.tree,1,0,1,3)
        self.analyseslayout.addWidget(self.export_plots,2,0,1,3)
        self.analyseslayout.addWidget(self.export_data_csv,3,0,1,3)
        
        #------------------------------#


        #---------Tab Widget-----------#

        self.tabwidget = QTabWidget(self.mainlayout_widget)
        tabPolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        tabPolicy.setHorizontalStretch(10)
        tabPolicy.setVerticalStretch(0)
        tabPolicy.setHeightForWidth(self.tabwidget.sizePolicy().hasHeightForWidth())
        self.tabwidget.setSizePolicy(tabPolicy)
        self.tab = QWidget()
        self.tabwidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tabwidget.addTab(self.tab_2, "")

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

        #Mission grid layout
        self.constraint_layout_widget = QWidget(self.constraint_groupbox)
        self.constraint_layout_widget.setGeometry(QRect(10,30,420,420))
        self.constraint_layout = QGridLayout(self.constraint_layout_widget)
        
        #Buttons and table
        self.constraint_table = QTableWidget(1,3,self.constraint_layout_widget)
        self.clear_constraint = QPushButton('Clear All',self.constraint_layout_widget)
        self.plot_diagram = QPushButton('Plot Diagram',self.constraint_layout_widget)
        self.constraint_layout.addWidget(self.constraint_table,0,0,1,2)
        self.constraint_layout.addWidget(self.clear_constraint,1,0,1,1)
        self.constraint_layout.addWidget(self.plot_diagram,1,1,1,1)
        #------------------------------#


        #--------Main Grid Layout Definition---------#
        
        mainlayout.addWidget(self.tree_groupbox,0,0,2,1)
        mainlayout.addWidget(self.tabwidget,0,1,2,1)
        mainlayout.addWidget(self.mission_groupbox,0,2,1,1)
        mainlayout.addWidget(self.constraint_groupbox,1,2,1,1)
        
        #--------------------------------------------#
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()