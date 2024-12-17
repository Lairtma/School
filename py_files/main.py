import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTableWidgetItem, QTableWidget, QLineEdit, QLabel, QDialog, QComboBox, QRadioButton, QLayout
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
        self.table_lessons_time.setGeometry(70, 60, 200, self.height() - 60)  

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

        self.set_lessons_main_table()
        self.table_schedule.cellClicked.connect(self.on_cell_clicked_table_schedule)


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

    # день недели дата.расположние и таблицы номеров уроков

    def resizeEvent(self, event):
        super(MainWindow, self).resizeEvent(event)
        x_position = (self.width() - self.date_label.width()) // 2
        y_position = self.height() - self.date_label.height() - 5
        self.date_label.move(x_position, y_position)

        row_height = self.height() // 10 if self.height() // 10 < 90 else 90
        y_position = int(self.height() * 0.065)
        self.table_lessons_time.setGeometry(70, y_position, 200, self.height() - 60)
        for row in range(9):
            self.table_lessons_time.setRowHeight(row, row_height)

        self.table_schedule.setGeometry(200, y_position - 20, self.width() - 270, self.height() - 20)
        for row in range(9):
            self.table_schedule.setRowHeight(row, row_height)


        # print(self.width(), self.height())
        

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
        if hasattr(self, 'table_schedule'):
            self.set_lessons_main_table()


    def next_day_button_clicked (self):
        self.current_date_raw += timedelta(days=1)  
        self.update_date_text()

    def previous_day_button_clicked (self):
        self.current_date_raw -= timedelta(days=1) 
        self.update_date_text()

    # заполнение главное таблицы
    # id любого предмета в таблице в БД должно быть col+row 
    def set_lessons_main_table(self):
        data = LESSONS_TITLE_PLACE_TEACHER_CLASS[WEEK_DAYS[1]] #self.current_day_of_week
        for col in range(len(CLASSES_LIST)):
            class_lessons = CLASSES_LIST[0] # должен быть col а не 0
            for row in range(9):
                is_group_lesson = data[class_lessons][1]["group_lesson"] # должен быть row а не 1
                if is_group_lesson:
                    item = QTableWidgetItem(f"Групповое")
                else:
                    subject = data[class_lessons][1]["title_lesson"] if data[class_lessons][1]["title_lesson"] is not None else ""
                    teacher = data[class_lessons][1]["teacher"] if data[class_lessons][1]["teacher"] is not None else ""
                    place = data[class_lessons][1]["places"] if data[class_lessons][1]["places"] is not None else ""
                    item = QTableWidgetItem(f"{subject}\n{teacher}\n{place}")
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setTextAlignment(Qt.AlignCenter)
                self.table_schedule.setItem(row, col, item)

                
    def on_cell_clicked_table_schedule(self, row, column):
        self.table_schedule.setCurrentCell(row, column)
        self.table_schedule.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: #1F6467; 
                color: #FFFFFF;            
            }
            QTableWidget::item {
                border: 1px solid black; 
            }
        """)

        self.settings_of_lesson(row, column)

    # настройка урока диалоговое окно
    def settings_of_lesson(self, row, column):

        # наши первоначальные данные 
        self.existing_data_about_lesson = LESSONS_TITLE_PLACE_TEACHER_CLASS[WEEK_DAYS[1]][CLASSES_LIST[0]][1]
        #existing_data_about_lesson = LESSONS_TITLE_PLACE_TEACHER_CLASS[WEEK_DAYS[self.current_day_of_week]][CLASSES_LIST[column]][row]

        # наши новые данные 
        self.new_updating_data = LESSONS_TITLE_PLACE_TEACHER_CLASS[WEEK_DAYS[1]][CLASSES_LIST[0]][1]


        self.setting_of_lesson_dialog = QDialog(self)
        self.setting_of_lesson_dialog.setWindowTitle("Действия")
        self.setting_of_lesson_dialog.resize(400, 600)
        self.setting_of_lesson_dialog.setStyleSheet("background-color: #1F6467; border-radius: 10px;")


        label_class_name = QLabel(self.setting_of_lesson_dialog)
        label_class_name.setStyleSheet("color: #FFFFFF;")
        label_class_name.setText(f"{CLASSES_LIST[column]}")
        label_class_name.setFont(QFont("Times New Roman", 18))

        label_class_date = QLabel(self.setting_of_lesson_dialog)
        label_class_date.setStyleSheet("color: #FFFFFF;")
        label_class_date.setText(f"{WEEK_DAYS[self.current_day_of_week]} {self.current_date}")
        label_class_date.setFont(QFont("Times New Roman", 18))

        label_class_num = QLabel(self.setting_of_lesson_dialog)
        label_class_num.setStyleSheet("color: #FFFFFF;")
        label_class_num.setText(f"Урок {row + 1}")
        label_class_num.setFont(QFont("Times New Roman", 18))
    

        # создание радио бокса по группам
        label_is_group = QLabel("По группам")
        label_is_group.setStyleSheet("font-size: 18px; color: #FFFFFF;")
        label_is_group.setAlignment(Qt.AlignCenter)

        self.radio_yes =  QRadioButton("Да")
        self.radio_no =  QRadioButton("Нет")

        self.radio_style_checked = ("""
            QRadioButton {
                font-size: 18px;
                color: #FFFFFF;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background: lightgray;
            }
            QRadioButton::indicator:checked {
                background: #5E9EA0;  
            }
            QRadioButton:focus {
                outline: none;
                border: none;
            }
        """)

        self.radio_style_not_checked = ("""
            QRadioButton {
                font-size: 18px;
                color: #FFFFFF;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background: lightgray;
            }
            QRadioButton::indicator:checked {
                background: #D9D9D9;  
            }
                                        
            QRadioButton:focus {
                outline: none;
                border: none;
            }
        """)

        if self.existing_data_about_lesson["group_lesson"]:
            self.radio_yes.setChecked(True)
        else:
            self.radio_no.setChecked(True)
        self.update_button_color()


        self.radio_yes.toggled.connect(self.update_button_color)
        self.radio_no.toggled.connect(self.update_button_color)

        layout_h = QHBoxLayout()
        layout_h.addWidget(label_is_group)
        layout_h.addWidget(self.radio_yes)
        layout_h.addWidget(self.radio_no)
        
        # выпадающие списки. Для не групповых занятий

        layout_v_for_lists = QVBoxLayout()

        # список предметов

        layout_for_lists_subj = QHBoxLayout()
        label_for_lesson = QLabel("Урок: ")
        label_for_lesson.setStyleSheet("font-size: 18px; color: #FFFFFF;")
        list_for_lesson = QComboBox()
        list_for_lesson.addItems(SUBJECTS_LIST)
        list_for_lesson.setStyleSheet("""
            QComboBox {
                background-color: #DCDCDC;
                font-size: 16px;
                border-radius: 5px;
            }
        """)

        layout_for_lists_subj.addWidget(label_for_lesson)
        layout_for_lists_subj.addWidget(list_for_lesson)

        # список учителей

        layout_for_lists_teachers = QHBoxLayout()
        label_for_teacher = QLabel("Учитель: ")
        label_for_teacher.setStyleSheet("font-size: 18px; color: #FFFFFF;")
        list_for_teacher = QComboBox()
        list_for_teacher.addItems(TEACHERS)
        list_for_teacher.setStyleSheet("""
            QComboBox {
                background-color: #DCDCDC;
                font-size: 16px;
                border-radius: 5px;
            }
        """)

        layout_for_lists_teachers.addWidget(label_for_teacher)
        layout_for_lists_teachers.addWidget(list_for_teacher)


        # список кабинетов 

        layout_for_lists_rooms = QHBoxLayout()
        label_for_rooms = QLabel("Кабинет: ")
        label_for_rooms.setStyleSheet("font-size: 18px; color: #FFFFFF;")
        list_for_rooms = QComboBox()
        list_for_rooms.addItems(map(str, PLACES))
        list_for_rooms.setStyleSheet("""
            QComboBox {
                background-color: #DCDCDC;
                font-size: 16px;
                border-radius: 5px;
            }
        """)

        layout_for_lists_rooms.addWidget(label_for_rooms)
        layout_for_lists_rooms.addWidget(list_for_rooms)

        # обьеденяем все лэйауты списков

        layout_v_for_lists.addLayout(layout_for_lists_subj)
        layout_v_for_lists.addLayout(layout_for_lists_teachers)
        layout_v_for_lists.addLayout(layout_for_lists_rooms)


        layout = QVBoxLayout()
        layout.addWidget(label_class_name, alignment=Qt.AlignCenter)
        layout.addWidget(label_class_date, alignment=Qt.AlignCenter)
        layout.addWidget(label_class_num, alignment=Qt.AlignCenter)
        layout.addLayout(layout_h) # радиобоксы 
        layout.addLayout(layout_v_for_lists) # списки
        # layout.setSizeConstraint(QLayout.SetFixedSize)  
        self.setting_of_lesson_dialog.setLayout(layout)


        self.setting_of_lesson_dialog.exec_()

    def update_button_color(self):
        self.radio_yes.setStyleSheet(self.radio_style_not_checked)
        self.radio_no.setStyleSheet(self.radio_style_not_checked)

        if self.radio_yes.isChecked(): 
            self.radio_yes.setStyleSheet(self.radio_style_checked)
            self.new_updating_data["group_lesson"] = True
        if self.radio_no.isChecked(): 
            self.radio_no.setStyleSheet(self.radio_style_checked)
            self.new_updating_data["group_lesson"] = False


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

        label_date_of_free_places = QLabel(self.free_places_dialog)
        label_date_of_free_places.setAlignment(Qt.AlignCenter)
        label_date_of_free_places.setStyleSheet("color: #FFFFFF;")
        label_date_of_free_places.setText(f"Дата: {WEEK_DAYS[self.current_day_of_week]} {self.current_date}\n Урок: {num_lesson}")
        label_date_of_free_places.setFont(QFont("Times New Roman", 18))

        free_rooms_label = QLabel(self.free_places_dialog)
        free_rooms_label.setAlignment(Qt.AlignCenter)
        free_rooms_label.setStyleSheet("color: #FFFFFF;")

        free_rooms_list = [x for x in range(100, 110)] # как то надо заполнить 
        grouped_rooms = [
            ", ".join(map(str, free_rooms_list[i:i + 5]))
            for i in range(0, len(free_rooms_list), 5)
        ]
        formatted_rooms = "\n".join(grouped_rooms)
        free_rooms_label.setText(formatted_rooms)
        free_rooms_label.setFont(QFont("Times New Roman", 16))

        layout = QVBoxLayout()
        layout.addWidget(label_date_of_free_places)
        layout.addWidget(free_rooms_label)
        self.free_places_dialog.setLayout(layout)

        self.free_places_dialog.exec_()

        
#Главня задача - заняться масштабированием на любом дисплее 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())