from PyQt5.QtWidgets import (QWidget, QLineEdit, QGridLayout, QDateEdit, QVBoxLayout, QPushButton,
                             QDoubleSpinBox, QCheckBox)
from datetime import date


class TableWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(700, 72)
        self.setMinimumWidth(700)

        # Widgets
        self.lesson = QLineEdit(self)
        self.lesson.setReadOnly(True)
        self.lesson.setToolTip('Описание предмета')
        self.deadline = QDateEdit(self)
        self.deadline.setToolTip('Дата окончания')
        self.deadline.setReadOnly(True)
        self.deadline.setDate(date.today())
        self.deadline.setMinimumDate(date(2017, 9, 1))
        self.save_button = QPushButton('Сохранить', self)
        self.delete_button = QPushButton('Удалить', self)
        self.result = QDoubleSpinBox(self)
        self.result.setSingleStep(0.01)
        self.result.setToolTip('Результат')
        self.done = QCheckBox(self)
        self.done.setToolTip('Задача выполнена')

        # Layouts
        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self.lesson, 0, 1)
        grid_layout.addWidget(self.deadline, 0, 3)
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.save_button)
        buttons_layout.addWidget(self.delete_button)
        grid_layout.addLayout(buttons_layout, 0, 5)
        grid_layout.addWidget(self.result, 0, 4)
        grid_layout.addWidget(self.done, 0, 0)

        # Tab order
        self.setTabOrder(self.done, self.lesson)
        self.setTabOrder(self.lesson, self.deadline)
        self.setTabOrder(self.deadline, self.result)
        self.setTabOrder(self.result, self.save_button)
        self.setTabOrder(self.save_button, self.delete_button)
