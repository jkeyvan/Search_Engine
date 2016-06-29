import sys,os,shutil,threading,time
from PyQt4 import QtGui,QtCore
from setting import *

##Front page


class main_window(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setGeometry(position[0],position[1],size[0],size[1])

        self.frame=QtGui.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(180, 200, 441, 104))
        self.frame.setStyleSheet("background-image: url(E:/final project/pictures/logo.gif);")

        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(105, 330, 599, 31))
        self.font = QtGui.QFont()
        self.font.setFamily("Constantia")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.lineEdit.setFont(self.font)
        self.lineEdit.setStyleSheet(("background:white;"
                                              "padding: 3px;"
                                              "border-style: solid;"
                                              "border: 2px solid gray;"
                                              "border-radius: 8px;"))

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(355, 380, 61, 23))
        self.pushButton.setStyleSheet(("border: 2px solid gray;"
                                                "border-radius: 6px;"))
        self.pushButton.setText("Search")



def main():
    app=QtGui.QApplication(sys.argv)
    main=main_window()
    main.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()