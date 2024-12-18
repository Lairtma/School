import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt

# Импортируем связь учитель-кабинет
from axios_data import TEACHER_ROOMS


class TeacherRoomWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учитель - кабинет")
        self.setFixedSize(700, 500)  # Размер окна

        # Центральный виджет и основной макет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        central_widget.setStyleSheet("background-color: #6BA4A4;")  # Цвет фона

        # Заголовок
        header_label = QLabel("Учитель - кабинет")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("""
            QLabel {
                background-color: #1F6467;
                color: white;
                font-size: 20px;
                font-weight: bold;
                padding: 10px;
            }
        """)
        main_layout.addWidget(header_label)

        # Список учителей и кабинетов
        self.teacher_room_list = QListWidget()
        self.populate_teacher_room_list()
        main_layout.addWidget(self.teacher_room_list)

        # Нижние кнопки
        bottom_layout = QHBoxLayout()
        back_button = QPushButton("Назад")
        add_button = QPushButton("Добавить")

        back_button.setFixedSize(120, 40)
        add_button.setFixedSize(120, 40)

        back_button.setStyleSheet(self.button_style())
        add_button.setStyleSheet(self.button_style())

        back_button.clicked.connect(self.go_back)
        add_button.clicked.connect(self.add_teacher_room)

        bottom_layout.addWidget(back_button)
        bottom_layout.addStretch()
        bottom_layout.addWidget(add_button)
        main_layout.addLayout(bottom_layout)

    def button_style(self):
        """Стиль для кнопок"""
        return """
            QPushButton {
                background-color: #1F6467;
                color: white;
                font-size: 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #154A4D;
            }
        """

    def populate_teacher_room_list(self):
        """Заполняем список учителей и кабинетов"""
        for entry in TEACHER_ROOMS:
            item = QListWidgetItem()
            item_widget = QWidget()
            item_layout = QHBoxLayout()

            # Поля: учитель и кабинет
            teacher_label = QLabel(entry["teacher"])
            teacher_label.setFixedSize(200, 40)
            teacher_label.setStyleSheet(self.label_style())

            room_label = QLabel(entry["room"])
            room_label.setFixedSize(200, 40)
            room_label.setStyleSheet(self.label_style())

            # Кнопка "Удалить"
            delete_button = QPushButton("🗑️")
            delete_button.setFixedSize(40, 40)
            delete_button.setStyleSheet("border: none; font-size: 18px;")
            delete_button.clicked.connect(lambda _, t=entry: self.delete_teacher_room(t))

            # Кнопка "Изменить"
            edit_button = QPushButton("✏️")
            edit_button.setFixedSize(40, 40)
            edit_button.setStyleSheet("border: none; font-size: 18px;")
            edit_button.clicked.connect(lambda _, t=entry: self.edit_teacher_room(t))

            # Добавляем элементы в макет
            item_layout.addWidget(teacher_label)
            item_layout.addWidget(room_label)
            item_layout.addStretch()
            item_layout.addWidget(delete_button)
            item_layout.addWidget(edit_button)
            item_layout.setContentsMargins(0, 5, 0, 5)

            item_widget.setLayout(item_layout)
            item.setSizeHint(item_widget.sizeHint())
            self.teacher_room_list.addItem(item)
            self.teacher_room_list.setItemWidget(item, item_widget)

    def label_style(self):
        """Стиль для текстовых меток"""
        return """
            QLabel {
                font-size: 16px;
                background-color: #EDEDED;
                padding: 5px;
                border-radius: 5px;
            }
        """

    def delete_teacher_room(self, entry):
        print(f"Удалена связь: {entry['teacher']} - {entry['room']}")

    def edit_teacher_room(self, entry):
        print(f"Редактирование связи: {entry['teacher']} - {entry['room']}")

    def go_back(self):
        print("Назад")
        self.close()

    def add_teacher_room(self):
        print("Добавление новой связи Учитель - кабинет")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TeacherRoomWindow()
    window.show()
    sys.exit(app.exec_())
