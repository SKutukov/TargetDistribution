#!/usr/bin/python3
from PyQt5.QtWidgets  import QApplication
import MainWindow as MW
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MW.MainWindow()
    window.show()
    sys.exit(app.exec_())
