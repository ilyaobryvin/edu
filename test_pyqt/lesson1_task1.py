import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

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

        self.label = QLabel('Counter: ', self)
        self.label.move(10, 10)

        self.label_counter = QLabel(str(self.counter), self)
        self.label_counter.move(100, 10)
        self.label_counter.setFixedWidth(30)

        self.label_attempt = QLabel('Attempts left: ', self)
        self.label_attempt.move(10, 30)

        self.label_attempt_counter = QLabel(str(10-self.counter), self)
        self.label_attempt_counter.move(100, 30)
        self.label_attempt_counter.setFixedWidth(30)

        self.button = QPushButton('Push it!', self)
        self.button.move(10, 50)
        self.button.clicked.connect(self.incCounter)

        self.label_attempt_over = QLabel('Atempts are over!', self)
        self.label_attempt_over.move(10, 80)
        self.label_attempt_over.setVisible(False)

    def incCounter(self):
        self.counter += 1
        self.label_counter.setText(str(self.counter))
        self.label_attempt_counter.setText(str(10-self.counter))
    
        if self.counter >= 10:
            self.button.setEnabled(False)
            self.label_attempt_over.setVisible(False)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())