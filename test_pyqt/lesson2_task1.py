import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSpinBox, QRadioButton, QButtonGroup, QPushButton
from PyQt6.QtCore import Qt

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
        label = QLabel('Калькулятор скидок', self)
        label.setStyleSheet('font-size: 24px; font-family: Arial;')

        self.price_input = QSpinBox(self)
        self.price_input.setRange(0, int(1e6))
        self.price_input.setValue(0)
        self.price_input.setFixedWidth(200)

        # radio buttons
        self.radio_group = QButtonGroup(self)
        radio_values = ['10% (Чёрная пятница)', '20% (Распродажа)', '30% (Промокод)']
        radio_buttons = []
        for value in radio_values:
            rb = QRadioButton(value, self)
            rb.setStyleSheet('font-size: 12px; font-family: Arial;')
            self.radio_group.addButton(rb)
            radio_buttons.append(rb)
        
        submit_button = QPushButton('Calculate', self)
        self.result_label = QLabel('', self)
        
        main_v_box = QVBoxLayout()
        main_v_box.setContentsMargins(16, 16, 16, 16)
        main_v_box.setSpacing(10)

        main_v_box.addWidget(label, alignment=Qt.AlignmentFlag.AlignTop)
        main_v_box.addWidget(self.price_input)

        for rb in radio_buttons:
            main_v_box.addWidget(rb)

        main_v_box.addWidget(submit_button, alignment=Qt.AlignmentFlag.AlignLeft)
        main_v_box.addWidget(self.result_label)

        submit_button.clicked.connect(self.pushSubmit)

        main_v_box.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_v_box.setSpacing(8)
        self.setLayout(main_v_box)

    def pushSubmit(self):
        price = self.price_input.value()
        checked = self.radio_group.checkedButton()
        if checked is None:
            disc_perc = 0
        else:
            disc_perc = int(checked.text().split('%')[0]) / 100
        
        disc_abc = round(price * disc_perc, 2)
        price_with_disc = price - disc_abc

        self.result_label.setText(f"Current price: {price_with_disc:.0f} rub., price with discount: {disc_abc:.0f} rub.")

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())