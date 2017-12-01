from PyQt5.QtWidgets import (QWidget,QLabel, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtWidgets import  (QStackedWidget, QFormLayout)
from PyQt5.QtCore import  pyqtSignal, QSize

import TaskGenerator as TG

import generate_tasks
import solve_tasks
class MainWindow(QWidget):
    tasks_name = 'tasks.txt'
    results_name = 'result.txt'
    TaskG = TG.TaskGenerator()
    def __init__(self):
        super(MainWindow, self).__init__()
        # add layout
        self.workWidget =  WorkWidget()
        self.confWidget = ConfigWidget()
        self.botWidget = QStackedWidget()
        self.botWidget.addWidget(self.confWidget)
        self.botWidget.addWidget(self.workWidget)

        layout = QVBoxLayout(self)

        #change to config layout  button
        self.confButton = QPushButton('Настройки')
        self.confButton.clicked.connect(self.handleButton3)
        # change to config work  button(
        self.workButton = QPushButton('Решать')
        self.workButton.clicked.connect(self.handleButton4)

        #buttons layout
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.confButton)
        buttonLayout.addWidget(self.workButton)
        #add layout
        layout.addLayout(buttonLayout)
        layout.addWidget(self.botWidget)

        #settint size
        self.setMaximumSize(QSize(900,500))
        self.setMinimumSize(QSize(500,500))
        self.setWindowTitle('Задача целераспределения')
        self.setWindowIcon(QIcon('icon.jpeg'))

    def handleButton3(self):
        self.botWidget.setCurrentIndex(0)
    def handleButton4(self):
        self.botWidget.setCurrentIndex(1)

class ConfigWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        # myQLineEdit.textChanged.connect(self.setName)
        # config layout
        self.configLayout = QVBoxLayout(self)
        self.configLabel = QLabel("Настройки:")
        self.configLayout.addWidget(self.configLabel)

class WorkWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        # Generate tasks button
        self.genButton = QPushButton('Сгенерировать задания', self)
        self.genButton.clicked.connect(self.handleButton1)
        # Solve tasks button
        self.solButton = QPushButton('Решить задания', self)
        self.solButton.clicked.connect(self.handleButton2)
        #set label
        self.label = QLabel(self)

        text = str("Компьютерная программа генерации заданий на решение задачи целераспределения методом динамического программирования. \n"  +
                            "Пусть для поражения каждой из n целей,имеющих боевые потенциалы c_i, необходимо соответственно a_j средств поражения. \n" +
                            "Требуется произвести целераспределение таким образом, чтобы нанести противнику максимально возможный ущерб m отпущенными \n"
                            "средствами поражения.")
        font = QFont()
        font.setPointSize(14)
        self.label.setText(text)
        self.label.setFont(font)


        #work layout
        self.workLayout = QVBoxLayout(self)
        self.workLayout.addWidget(self.label)
        self.workLayout.addWidget(self.genButton)
        self.workLayout.addWidget(self.solButton)

    def handleButton1(self):
            self.label.setText('Задание сгенерировано и сохранено в файл tasks.txt.')
            generate_tasks.generate_tasks(self.tasks_name, self.TaskG)

    def handleButton2(self):
            self.label.setText('Задание решено и решение сохранено в файл result.txt.')
            solve_tasks.solve_task(self.results_name, self.tasks_name)
