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
        self.widgets = []

        products = [{"title": "Микрофон", "price": 15000}, {"title": "Монитор", "price": 20000}]

        main_v_box = QVBoxLayout()

        for product in products:
            product_title = QLabel(product['title'], self)
            product_price = QLabel(str(product['price']), self)
            product_quantity = QLineEdit("1", self)
            product_total = QLabel(str(product['price']), self)

            product_quantity.setFixedWidth(50)

            product_h_box = QHBoxLayout()
            product_h_box.addWidget(product_title)
            product_h_box.addWidget(product_price)
            product_h_box.addWidget(product_quantity)
            product_h_box.addWidget(product_total)
            
            main_v_box.addLayout(product_h_box)

            self.widgets.append({'price': product['price'], 'quantity': product_quantity, 'total': product_total})

        calc_button = QPushButton('Calculate', self)
        main_v_box.addWidget(calc_button)
        main_v_box.setAlignment(calc_button, Qt.AlignmentFlag.AlignRight)
        self.total_label = QLabel('Total', self)
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_v_box.addWidget(self.total_label)

        calc_button.clicked.connect(self.calcTotal)

        self.setLayout(main_v_box)

    def calcTotal(self):
        total_sum = 0
        for widget in self.widgets:
            price = widget['price']
            qnt = int(widget['quantity'].text())
            product_sum = price * qnt
            widget['total'].setText(str(product_sum))
            total_sum += product_sum
        self.total_label.setText(f"Total: {total_sum:,} rub")

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())