import sys
import Lista_Serial
from PyQt5 import QtWidgets
from heat_flow_gui import Ui_MainWindow
from serial_reader import SerialReader

if __name__ == "__main__":
    serialReader = SerialReader
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.preencher_portas_combobox(Lista_Serial.serial_ports())
    ui.attachInitializeEvent(serialReader.serial_read)
    ui.attachConnectEvent(serialReader.connect)
    ui.attachDisconnectEvent(serialReader.disconnect)
    MainWindow.show()
    sys.exit(app.exec_())
