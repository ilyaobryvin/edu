import sys
import os
import random
import pandas as pd
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.data = None

    def initializeUI(self) -> None:
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle('Конвертер файлов')
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        csv_exists = os.path.exists("demo_data.csv")
        json_exists = os.path.exists("demo_data.json")

        if not (csv_exists and json_exists):
            self.generateDemoFiles()

        main_v_box = QVBoxLayout()

        button_load_file = QPushButton('Загрузить файл', self)
        self.button_list = QComboBox(self)
        self.button_list.addItems(['CSV > JSON', 'JSON > CSV'])
        button_save_file = QPushButton('Сохранить как...', self)
        self.empty_file_label = QLabel('', self)

        main_v_box.addWidget(button_load_file)
        main_v_box.addWidget(self.button_list)
        main_v_box.addWidget(button_save_file)
        main_v_box.addWidget(self.empty_file_label)

        button_load_file.clicked.connect(self.loadFile)
        button_save_file.clicked.connect(self.saveFile)

        main_v_box.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_v_box.setSpacing(8)

        self.setLayout(main_v_box)

    def loadFile(self):
        mode = self.button_list.currentText()
        self.empty_file_label.setText('')

        if mode == 'CSV > JSON':
            file_type = "CSV Files (*.csv)"
        else:
            file_type = "JSON Files (*.json)"
        
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', file_type)

        if not file_path:
            return
        
        df = pd.DataFrame()
        try:
            if mode == 'CSV > JSON':
                df = self.convertFromCSVToJSON(file_path)
            else:
                df = self.convertFromJSONToCSV(file_path)
        except Exception as e:
            print("Error reading file:", e)
            self.data = None

        if df.empty:
            print("File is empty")
            self.data = None
            self.empty_file_label.setText('Загруженный файл пустой! Выберите другой файл!')
            return

        self.empty_file_label.setText('Файл сконвертирован! Можно сохранять!')
        self.data = df
        

    def saveFile(self):
        mode = self.button_list.currentText()

        save_filter = "JSON Files (*.json)" if mode == 'CSV > JSON' else "CSV Files (*.csv)"

        to_file_path, _ = QFileDialog.getSaveFileName(self, '', '', save_filter)

        if not to_file_path:
            return
        
        if self.data is None:
            return
        
        if mode == 'CSV > JSON':
            self.data.to_json(to_file_path, orient="records", force_ascii=False, indent=2)
        else:
            self.data.to_csv(to_file_path, index=False)            
    
    def convertFromCSVToJSON(self, filepath):
        return pd.read_csv(filepath)
    
    def convertFromJSONToCSV(self, filepath):
        return pd.read_json(filepath)
    
    def generateDemoFiles(self):
        data = []
        for i in range(1, 6):
            data.append({
                "id": i,
                "product": f"item_{random.randint(1, 3)}",
                "qty": random.randint(1, 5),
                "price": random.randint(100, 500),
            })

        df = pd.DataFrame(data)

        with open('demo_data_empty.csv', 'w') as f:
            f.write('')
        df.to_csv('demo_data.csv', index=False)
        df.to_json('demo_data.json', orient="records", force_ascii=False, indent=2)

        print("Demo files created!")


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())