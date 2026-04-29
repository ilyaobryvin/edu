import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self) -> None:
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle('Application title')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.counter = 0

        label = QLabel('Counter: ', self)
        label.move(100, 100)

        self.label_counter = QLabel(str(self.counter), self)
        self.label_counter.move(160, 100)
        self.label_counter.setFixedWidth(30)

        button = QPushButton('Push it!', self)
        button.move(100, 140)
        button.clicked.connect(self.incCounter)

        self.counter_input = QLineEdit(self)
        self.counter_input.move(100, 180)

        save_button = QPushButton('Save it!', self)
        save_button.move(100, 220)
        save_button.clicked.connect(self.saveCounter)

    def saveCounter(self):
        new_value = self.counter_input.text()
        self.label_counter.setText(new_value)
        self.counter = int(new_value)


    def incCounter(self):
        self.counter += 1
        self.label_counter.setText(str(self.counter))


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())