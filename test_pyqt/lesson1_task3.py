import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton

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
        self.input_a = QLineEdit(self)
        self.input_a.move(10, 10)
        self.input_a.setFixedWidth(120)

        self.input_b = QLineEdit(self)
        self.input_b.move(10, 40)
        self.input_b.setFixedWidth(120)

        self.result_label = QLabel("Результат: ", self)
        self.result_label.move(10, 100)
        self.result_label.setFixedWidth(300)

        self.result = QLabel("0", self)
        self.result.move(80, 100)
        self.result.setFixedWidth(300)

        self.btn_sum = QPushButton("Сложить", self)
        self.btn_sum.move(10, 70)
        self.btn_sum.clicked.connect(self.on_sum_clicked)

    def on_sum_clicked(self):
        a_text = self.input_a.text().strip() or '0'
        b_text = self.input_b.text().strip() or '0'

        try:
            a = float(a_text.replace(",", "."))
            b = float(b_text.replace(",", "."))
        except ValueError:
            self.result.setText("Введите корректные числа")
            return

        result = a + b
        if result % 1 == 0:
            self.result.setText(str(int(result)))
            return
        self.result.setText(str(result))


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())