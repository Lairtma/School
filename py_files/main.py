import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QTableWidget, QLineEdit, QLabel, QDialog, QPushButton
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QFont
from PyQt5.QtCore import Qt
from axios_data import *
from datetime import datetime, timedelta

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("../mainWindow.ui", self)

        self.setWindowTitle("School Schedule for Konstantin")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.current_date_raw = datetime.now()
        self.update_date_text()

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

        self.next_day_button.clicked.connect(self.next_day_button_clicked)
        self.previous_day_button.clicked.connect(self.previous_day_button_clicked)

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
                border: 1px solid black; 
            }
        """)
        self.font = QFont("Times New Roman ", 16)

        for row in range(9):
            self.table_lessons_time.setRowHeight(row, 90)

        for row, text in enumerate(LESSONS_NUM_TIME):
            item = QTableWidgetItem(text)
            item.setFont(self.font) 
            item.setTextAlignment(Qt.AlignCenter)  
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table_lessons_time.setItem(row, 0, item)

        self.table_lessons_time.cellClicked.connect(self.on_cell_clicked)

        #настройка таблицы уроков, кабинетов и учителей
        self.table_schedule = QTableWidget(self)
        self.table_schedule.setRowCount(9)  
        self.table_schedule.setColumnCount(len(CLASSES_LIST)) 
        self.table_schedule.setGeometry(200, 40, 1200, 1000) 
        self.table_schedule.setFrameStyle(QTableWidget.NoFrame)
        self.table_schedule.verticalHeader().setVisible(False)
        self.table_schedule.setHorizontalHeaderLabels(CLASSES_LIST)

        for row in range(9):
            self.table_schedule.setRowHeight(row, 90)
            

        self.table_schedule.setStyleSheet("""
            QTableWidget::item {
                border: 1px solid black;  
            }
        """)


        # день недели дата

        self.date_label = QLineEdit(self)
        self.date_label.setText(self.date_text)
        self.date_label.setReadOnly(True)
        self.date_label.setFixedWidth(250)
        self.date_label.setAlignment(Qt.AlignCenter)

        self.date_label.setStyleSheet("""
            QLineEdit {
                background-color: #1F6467; 
                color: #FFFFFF;           
                font-size: 16px;          
                border-radius: 10px;  
                font-weight: bold;      
            }
        """)

    # день недели дата.расположние

    def resizeEvent(self, event):
        super(MainWindow, self).resizeEvent(event)
        x_position = (self.width() - self.date_label.width()) // 2
        y_position = self.height() - self.date_label.height() - 20
        self.date_label.move(x_position, y_position)
        

    #функкции для меню бара

    def import_from_excel(self):
        print("import_from_excel")

    def export_to_excel_for_week(self):
        print("export_to_excel_for_week")

    def export_to_excel_for_this_day(self):
        print("export_to_excel_for_this_day")

    #функции для кнопок следующий - предыдущий 
    def update_date_text(self):
        self.current_date = self.current_date_raw.strftime("%d.%m.%Y")
        self.current_day_of_week = self.current_date_raw.weekday()
        self.date_text = f"{WEEK_DAYS[self.current_day_of_week]} {self.current_date}"
        if hasattr(self, 'date_label'):
            self.date_label.setText(self.date_text)

    def next_day_button_clicked (self):
        self.current_date_raw += timedelta(days=1)  
        self.update_date_text()

    def previous_day_button_clicked (self):
        self.current_date_raw -= timedelta(days=1) 
        self.update_date_text()

    # функция для нажатия на кнопку номера урока 
    def on_cell_clicked(self, row, column):
        self.table_lessons_time.setCurrentCell(row, column)
        self.table_lessons_time.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #1F6467; 
                color: #FFFFFF;            
            }
            QTableWidget::item {
                border: 1px solid black; 
            }
        """)

        self.free_places_for_the_lessons_widget(LESSONS_NUM_TIME[row].split("\n")[0], row, column)

    #вывод свободных кабинетов 
    def free_places_for_the_lessons_widget(self, num_lesson, row, column):

        self.free_places_dialog = QDialog(self)
        self.free_places_dialog.setWindowTitle("Свободные кабинеты")  
        self.free_places_dialog.resize(300, 200)  
        self.free_places_dialog.setStyleSheet("background-color: #1F6467; border-radius: 10px;")

        free_rooms_label = QLabel(self.free_places_dialog)
        free_rooms_label.setAlignment(Qt.AlignCenter)
        free_rooms_label.setStyleSheet("color: #FFFFFF;")

        free_rooms_list = [x for x in range(100, 110)]
        grouped_rooms = [
            ", ".join(map(str, free_rooms_list[i:i + 5]))
            for i in range(0, len(free_rooms_list), 5)
        ]
        formatted_rooms = "\n".join(grouped_rooms)
        free_rooms_label.setText(formatted_rooms)
        free_rooms_label.setFont(QFont("Times New Roman", 16))

        layout = QVBoxLayout()
        layout.addWidget(free_rooms_label)
        self.free_places_dialog.setLayout(layout)

        self.free_places_dialog.exec_()

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())