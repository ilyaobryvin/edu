import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

def on_button_clicked():
    button.click_count += 1
    label.setText(f"Счетчик: {button.click_count}")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Счетчик кликов")

layout = QVBoxLayout()

button = QPushButton("Кликни меня")
button.click_count = 0

label = QLabel("Счетчик: 0")

button.clicked.connect(on_button_clicked)

layout.addWidget(button)
layout.addWidget(label)

window.setLayout(layout)
window.show()

sys.exit(app.exec())