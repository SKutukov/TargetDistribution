from PyQt5.QtWidgets import (QWidget,QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtGui import (QFont, QIcon)

import GenAndSolve
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.label = QLabel(self)
        # Generate tasks button
        self.genButton = QPushButton('Сгенерировать задания', self)
        self.genButton.clicked.connect(self.handleButton1)
        # Solve tasks button
        self.solButton = QPushButton('Решить задания', self)
        self.solButton.clicked.connect(self.handleButton2)

        #add layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.genButton)
        layout.addWidget(self.solButton)

        #settint size
        self.setGeometry(500, 500, 500, 220)
        self.setWindowTitle('Задача целераспределения')
        self.setWindowIcon(QIcon('icon.jpeg'))

    def handleButton1(self):
        self.label.setText('Задание сгенерировано и сохранено в файл tasks.txt.')
        GenAndSolve.generate_tasks()

    def handleButton2(self):
        self.label.setText('Задание решено и решение сохранено в файл result.txt.')
        GenAndSolve.solve_task()