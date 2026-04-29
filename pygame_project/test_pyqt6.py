import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Простое приложение")

layout = QVBoxLayout()

label = QLabel("Привет, мир!")
button = QPushButton("Нажми меня")
button.clicked.connect(lambda: label.setText("Кнопка нажата!"))

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())