#!/usr/bin/python3
import sys
# Класс QUrl предоставляет удобный интерфейс для работы с Urls
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
# Класс QQuickView предоставляет возможность отображать QML файлы.
from PyQt5.QtQuick import QQuickView

import MainWindow as MW
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

#    view = QQuickView()
#    view.setSource(QUrl('main.qml'))
#    view.show()
    window = MW.MainWindow()
    window.show()

    sys.exit(app.exec_())
