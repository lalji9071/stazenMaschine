from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyModbusTCP.client import ModbusClient
import time
import os
import sys

from PyQt5.QtWidgets import *

from stanzenmaschineUI import Ui_StanzenMaschine


class main(QWidget, Ui_StanzenMaschine):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pbConnect.clicked.connect(self.connect_nexus_machine)

    def connect_nexus_machine(self):
        c = ModbusClient()
        c.host("192.168.0.147")
        c.port(502)
        c.open()
        input_register = c.read_coils(0, 16)
        while True:
            if input_register:

                self.lineEditIP.setText(str(input_register))

            else:
                print("read error")
            time.sleep(5)


app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()
