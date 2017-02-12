import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from heat_flow_gui import Ui_MainWindow

def Heat_Flow_Gui(Ui_MainWindow):
    def __init__(self,MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

if __name__== "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    prog =Ui_MainWindow()
    prog.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

