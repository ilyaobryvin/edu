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
        self.change_bg_label = QLabel('Background colors: ', self)
        self.change_bg_label.move(10, 10)

        self.button_red = QPushButton('Red color', self)
        self.button_red.move(10, 30)
        self.button_red.clicked.connect(self.changeBGColor_r)

        self.button_green = QPushButton('Green color', self)
        self.button_green.move(10, 50)
        self.button_green.clicked.connect(self.changeBGColor_g)

        self.button_blue = QPushButton('Blue color', self)
        self.button_blue.move(10, 70)
        self.button_blue.clicked.connect(self.changeBGColor_b)

        self.current_bg_label = QLabel('Current background color is: ', self)
        self.current_bg_label.move(10, 100)

        self.background_color = QLabel('None', self)
        self.background_color.move(180, 100)


    def changeBGColor_r(self):
        self.setStyleSheet("background-color: darkred")
        self.background_color.setText('Red')
        self.background_color.setFixedWidth(30)

    def changeBGColor_g(self):
        self.setStyleSheet("background-color: green")
        self.background_color.setText('Green')
        self.background_color.setFixedWidth(30)

    def changeBGColor_b(self):
        self.setStyleSheet("background-color: blue")
        self.background_color.setText('Blue')
        self.background_color.setFixedWidth(30)

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())