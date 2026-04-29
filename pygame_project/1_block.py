import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt6.QtGui import QFont

# Create app
app = QApplication(sys.argv)

# create main window
# window = QMainWindow()
# window.setWindowTitle('My first main window')
# window.setGeometry(100, 100, 600, 400)

# Создание окна
window = QWidget()
window.setWindowTitle("Пример QLabel")
window.setGeometry(100, 100, 400, 200)  # Установка размеров окна

# Создание метки и установка ее как дочерний элемент для окна
label = QLabel(text="Привет, мир!", parent=window)
label.move(150, 80)  # Позиционирование метки вручную

# Изменение шрифта, размера и толщины текста с помощью setFont
font = QFont("Arial", 24)  # Шрифт Arial, размер 24
font.setBold(True)  # Сделать текст жирным
label.setFont(font)
# show our window
window.show()

# start main cycle
sys.exit(app.exec())