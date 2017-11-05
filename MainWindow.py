from PyQt5.QtWidgets import (QWidget,QLabel, QPushButton, QVBoxLayout)
from PyQt5.QtGui import (QFont, QIcon)

import GenAndSolve
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.label = QLabel(self)
        # Generate task and solve task
        self.genButton = QPushButton('Сгенерировать задания и решить задания', self)
        self.genButton.clicked.connect(self.handleButton1)

        #add layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.genButton)

        #settint size
        self.setGeometry(500, 500, 500, 220)
        self.setWindowTitle('Задача целераспределения')
        self.setWindowIcon(QIcon('icon.jpeg'))

    def handleButton1(self):
        self.label.setText('Задание сгененрировано и решено. Задание сохранено в файл tasks.txt. Решение сохранено в файл result.txt.')
        GenAndSolve.generate_and_solve_Task()
    #def handleButton2(self):
    #    self.label.setText('Задания решены и решения сохранены в файл  ')
    #    solveTask(taskL)
