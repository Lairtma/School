import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt

# Импортируем список учителей
from axios_data import TEACHERS


class TeacherListWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список учителей")
        self.setFixedSize(600, 500)  # Фиксированный размер окна

        # Центральный виджет и основной макет
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        central_widget.setStyleSheet("background-color: #6BA4A4;")  # Цвет фона

        # Заголовок
        header_label = QLabel("Список учителей")
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

        # Список учителей
        self.teacher_list_widget = QListWidget()
        self.populate_teacher_list()
        main_layout.addWidget(self.teacher_list_widget)

        # Нижние кнопки
        bottom_layout = QHBoxLayout()
        back_button = QPushButton("Назад")
        add_button = QPushButton("Добавить")

        back_button.setFixedSize(120, 40)
        add_button.setFixedSize(120, 40)

        back_button.setStyleSheet(self.button_style())
        add_button.setStyleSheet(self.button_style())

        back_button.clicked.connect(self.go_back)
        add_button.clicked.connect(self.add_teacher)

        bottom_layout.addWidget(back_button)
        bottom_layout.addStretch()
        bottom_layout.addWidget(add_button)
        main_layout.addLayout(bottom_layout)

    def button_style(self):
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

    def populate_teacher_list(self):
        # Создание элементов списка учителей
        for teacher in TEACHERS:
            item = QListWidgetItem()
            item_widget = QWidget()
            item_layout = QHBoxLayout()

            # Название учителя
            teacher_label = QLabel(teacher)
            teacher_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    background-color: #EDEDED;
                    padding: 10px;
                    border-radius: 10px;
                }
            """)
            teacher_label.setAlignment(Qt.AlignCenter)
            teacher_label.setFixedSize(250, 40)

            # Кнопка "Удалить"
            delete_button = QPushButton("🗑️")  # Иконка-корзина
            delete_button.setFixedSize(40, 40)
            delete_button.setStyleSheet("border: none; font-size: 18px;")
            delete_button.clicked.connect(lambda _, t=teacher: self.delete_teacher(t))

            # Кнопка "Изменить"
            edit_button = QPushButton("✏️")  # Иконка-карандаш
            edit_button.setFixedSize(40, 40)
            edit_button.setStyleSheet("border: none; font-size: 18px;")
            edit_button.clicked.connect(lambda _, t=teacher: self.edit_teacher(t))

            # Добавляем элементы в макет
            item_layout.addWidget(teacher_label)
            item_layout.addStretch()
            item_layout.addWidget(delete_button)
            item_layout.addWidget(edit_button)
            item_layout.setContentsMargins(0, 5, 0, 5)
            item_widget.setLayout(item_layout)

            item.setSizeHint(item_widget.sizeHint())
            self.teacher_list_widget.addItem(item)
            self.teacher_list_widget.setItemWidget(item, item_widget)

    def delete_teacher(self, teacher_name):
        print(f"Удалён учитель: {teacher_name}")

    def edit_teacher(self, teacher_name):
        print(f"Редактирование учителя: {teacher_name}")

    def go_back(self):
        print("Назад")
        self.close()

    def add_teacher(self):
        print("Добавление нового учителя")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TeacherListWindow()
    window.show()
    sys.exit(app.exec_())
