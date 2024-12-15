import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QTableWidget, QScrollArea
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QFont
from PyQt5.QtCore import Qt
from axios_data import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("../mainWindow.ui", self)

        self.setWindowTitle("School Schedule for Konstantin")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        #настройка меню бара
        self.menu_bar_export_to_excel_for_this_day.triggered.connect(self.export_to_excel_for_this_day)
        self.menu_bar_export_to_excel_for_week.triggered.connect(self.export_to_excel_for_week)
        self.menu_bar_import_from_excel.triggered.connect(self.import_from_excel)

        #настройка кнопок "следующий день" и "предыдущий день" 
        pixmap = QPixmap("../assets/arrow.png")
        mirrored_pixmap = pixmap.transformed(QTransform().scale(-1, 1))

        self.previous_day_button.setIcon(QIcon(mirrored_pixmap)) 
        self.previous_day_button.setIconSize(QtCore.QSize(32, 32)) 
        self.previous_day_button.setFixedSize(50, 50)  

        self.next_day_button.setIcon(QIcon(pixmap)) 
        self.next_day_button.setIconSize(QtCore.QSize(32, 32)) 
        self.next_day_button.setFixedSize(50, 50)

        #настройка расположения кнопок
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.previous_day_button, alignment=Qt.AlignLeft)
        h_layout.addStretch() 
        h_layout.addWidget(self.next_day_button, alignment=Qt.AlignRight)

        v_layout = QVBoxLayout()
        v_layout.addStretch()  
        v_layout.addLayout(h_layout)  
        v_layout.addStretch()

        central_widget.setLayout(v_layout)

        #настройка таблицы номера урока и времени его проведения

        self.table_lessons_time = QTableWidget(self)
        self.table_lessons_time.setRowCount(9)  
        self.table_lessons_time.setColumnCount(1) 
        self.table_lessons_time.setGeometry(70, 60, 200, 1000)  

        self.table_lessons_time.verticalHeader().setVisible(False)
        self.table_lessons_time.horizontalHeader().setVisible(False)
        self.table_lessons_time.setFrameStyle(QTableWidget.NoFrame)
        self.table_lessons_time.setStyleSheet("""
            QTableWidget::item {
                border: 1px solid black;  /* Чёрная обводка вокруг ячеек */
            }
        """)
        font = QFont("Times New Roman ", 16)

        for row in range(9):
            self.table_lessons_time.setRowHeight(row, 90)

        for row, text in enumerate(LESSONS_NUM_TIME):
            item = QTableWidgetItem(text)
            item.setFont(font)  # Применяем шрифт
            item.setTextAlignment(Qt.AlignCenter)  # Центрирование текста
            self.table_lessons_time.setItem(row, 0, item)

        #настройка таблицы уроков, кабинетов и учителей
        # self.table_schedule = QTableWidget(self)
        # self.table_schedule.setRowCount(9)  
        # self.table_schedule.setColumnCount(len(CLASSES_LIST)) 
        # self.table_schedule.setGeometry(200, 40, len(CLASSES_LIST)*200, 1000) 
        # self.table_schedule.setFrameStyle(QTableWidget.NoFrame)
        # self.table_schedule.verticalHeader().setVisible(False)
        # self.table_schedule.setHorizontalHeaderLabels(CLASSES_LIST)

        # for row in range(9):
        #     self.table_schedule.setRowHeight(row, 90)

        # for column in range(len(CLASSES_LIST)):
        #     self.table_schedule.setColumnWidth(column, 100)

        # self.table_schedule.setStyleSheet("""
        #     QTableWidget::item {
        #         border: 1px solid black;  /* Чёрная обводка вокруг ячеек */
        #     }
        # """)



    def import_from_excel(self):
        print("import_from_excel")

    def export_to_excel_for_week(self):
        print("export_to_excel_for_week")

    def export_to_excel_for_this_day(self):
        print("export_to_excel_for_this_day")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())