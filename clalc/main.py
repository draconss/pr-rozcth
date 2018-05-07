from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QLineEdit,QPushButton
from PyQt5 import uic
import logic_vive

import sys

class nastr_windows(QWidget):
# settings window
    def __init__(self,a):
        super().__init__()
        self.cli = a
        self.ui = uic.loadUi('nst_UK.ui')
        self.UIinit()

    def UIinit(self):
        self.ui.setWindowTitle('настроювання')
        self.ui.pushButton.clicked.connect(self.ok)
        self.ui.pushButton_2.clicked.connect(self.ot)
        self.ui.show()


    def ok(self):
        self.cli.num_skr = self.ui.spinBox.value()
        self.ui.close()
        self.close()
    def ot(self):
        self.ui.close()
        self.close()

class main(QMainWindow,logic_vive.logick):
    def __init__(self):
        super().__init__()
        super(logic_vive.logick).__init__()
        self.ui = uic.loadUi('interface_Uk.ui')
        self.ui.setWindowTitle('Radio tech')
        self.contr = 1
        self.num_skr = 3
        self.but_cli()
        self.ui.show()
    # connect button
    def but_cli(self):
        self.ui.bfind.clicked.connect(self.om_sh)
        self.ui.bfind_resps.clicked.connect(self.res_ps)
        self.ui.bfind_respr.clicked.connect(self.res_pr)
        self.ui.bfind_cpps.clicked.connect(self.cp_ps)
        self.ui.bfind_cppr.clicked.connect(self.cp_pr)
        self.ui.calc.triggered.connect(self.clas)
        self.ui.bfind_XL.clicked.connect(self.reac_L)
        self.ui.bfind_XC.clicked.connect(self.reac_Cp)
        self.ui.bfind_Z.clicked.connect(self.impned)
        self.ui.bfind_c.clicked.connect(self.convert)
        self.ui.bfind_Z_2.clicked.connect(self.P_ze)
        self.ui.bfind_el.clicked.connect(self.R_lem)
        self.ui.NST.triggered.connect(self.nstr)
    #call the settings window
    def nstr(self):
        self.menu = nastr_windows(self)




app = QApplication(sys.argv)
v = main()
sys.exit(app.exec_())
