import sys
from PyQt6.QtWidgets import QApplication, QWidget

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
        pass


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())