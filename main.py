import sys
from View.main_window import MainWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
