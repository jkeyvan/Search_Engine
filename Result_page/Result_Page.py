import sys,os,shutil,threading,time
from PyQt4 import QtGui,QtCore
from ui_window import *

class result_page(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = result_page()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())