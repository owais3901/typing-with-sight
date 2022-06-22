
import subprocess
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
class MyGUI(QDialog):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("gui.ui",self)
        self.pushButton.clicked.connect(self.click)
        self.show()
    def click(self):
        subprocess.call("main.py",shell=True)
def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
if __name__ == '__main__':
    main()
