import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QButtonGroup, QRadioButton, QPushButton
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
        header = QLabel('Опрос удовлетворенности', self)
        header.setStyleSheet('font-size: 24px; font-family: Arial;')
        header.setFixedHeight(30)
        header.setAlignment(Qt.AlignmentFlag.AlignTop)

        sub_header = QLabel('Выберите вариант:', self)
        sub_header.setStyleSheet('font-size: 20px; font-family: Arial;')
        sub_header.setFixedHeight(24)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(header)
        main_v_box.addWidget(sub_header)
        # radio buttons
        radio_group = QButtonGroup(self)
        radio_values = ['Good', 'Normal', 'Bad']
        for value in radio_values:
            radio_button = QRadioButton(value, self)
            radio_button.setStyleSheet('font-size: 12px; font-family: Arial;')
            radio_group.addButton(radio_button)
            main_v_box.addWidget(radio_button)
        
        radio_group.buttonClicked.connect(self.getValue)
        # sumit button
        self.submit_button = QPushButton('Send', self)
        self.submit_button.setFixedWidth(130)
        self.submit_button.setEnabled(False)
        self.submit_button.setStyleSheet('font-size: 14px; font-family: Arial;')
        self.submit_button.clicked.connect(self.submit)
        main_v_box.addWidget(self.submit_button)
        main_v_box.setAlignment(self.submit_button, Qt.AlignmentFlag.AlignCenter)

        self.selected_value = None

        self.setLayout(main_v_box)

    def getValue(self, button):
        # print(button.text())
        self.selected_value = button.text()
        self.submit_button.setEnabled(True)

    def submit(self):
        print(f"User selected: {self.selected_value}")


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())