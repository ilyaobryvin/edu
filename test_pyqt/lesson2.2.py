import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QButtonGroup, QRadioButton, QPushButton, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self) -> None:
        # self.setGeometry(600, 200, 800, 600)
        self.setMinimumSize(350, 250)
        self.setWindowTitle('Application title')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        label = QLabel('Confirmation code: ', self)
        self.code_input = QLineEdit(self)
        self.submit_button = QPushButton('Send', self)

        self.submit_button.setEnabled(False)
        self.code_input.textEdited.connect(self.checkCode)
        self.submit_button.clicked.connect(self.submit)

        main_h_box = QHBoxLayout()
        main_h_box.addWidget(label)
        main_h_box.addWidget(self.code_input)
        main_h_box.addWidget(self.submit_button)
        self.value = None

        self.setLayout(main_h_box)

    def checkCode(self):
        if len(self.code_input.text()) > 0:
            self.submit_button.setEnabled(True)
            self.value = self.code_input.text()

    def submit(self):
        if self.value is not None:
            print(self.value)
            self.value = None

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())