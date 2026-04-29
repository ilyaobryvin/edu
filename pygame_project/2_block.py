import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QGridLayout with QLabel Example")

layout = QGridLayout()

label1 = QLabel("Label 1")
label2 = QLabel("Label 2")
label3 = QLabel("Label 3")
label4 = QLabel("Label 4")

layout.addWidget(label1, 0, 0)  # (row, column)
layout.addWidget(label2, 0, 1)
layout.addWidget(label3, 1, 0)
layout.addWidget(label4, 1, 1)

window.setLayout(layout)
window.show()

sys.exit(app.exec())