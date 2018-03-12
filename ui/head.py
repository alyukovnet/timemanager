from PyQt5.QtWidgets import (QWidget, QGridLayout, QComboBox, QHBoxLayout, QLabel, QDateEdit,
                             QDoubleSpinBox, QTimeEdit, QPushButton)
from datetime import date, timedelta


class HeadWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(700, 105)
        self.setMinimumWidth(700)

        # Widgets
        self.work_type = QComboBox(self)
        self.work_type.setToolTip('Тип работы')
        # self.work_type.addItems()
        self.lesson = QComboBox(self)
        self.lesson.setToolTip('Урок')
        # self.lesson.addItems()
        actuality_label = QLabel('Дата начала', self)
        self.actuality = QDateEdit(self)
        self.actuality.setDate(date.today())
        self.actuality.setMinimumDate(date(2017, 9, 1))
        self.actuality.setToolTip('Дата начала')
        deadline_label = QLabel('Дата окончания', self)
        self.deadline = QDateEdit(self)
        self.deadline.setDate(date.today() + timedelta(1))
        self.deadline.setMinimumDate(date.today())
        self.deadline.setToolTip('Дата окончания')
        priority_label = QLabel('Приоритет', self)
        self.priority = QDoubleSpinBox(self)
        self.priority.setMaximumWidth(80)
        self.priority.setToolTip('Приоритет')
        time_label = QLabel('Время выполнения', self)
        self.time = QTimeEdit(self)
        self.time.setMaximumWidth(80)
        self.time.setDisplayFormat('HH:mm')
        self.time.setToolTip('Время выполнения')
        self.add_button = QPushButton('Добавить', self)
        self.add_button.setToolTip('Добавить в список')

        # Layouts
        actuality_layout = QHBoxLayout()
        actuality_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)
        actuality_layout.addWidget(actuality_label)
        actuality_layout.addWidget(self.actuality)
        deadline_layout = QHBoxLayout()
        deadline_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)
        deadline_layout.addWidget(deadline_label)
        deadline_layout.addWidget(self.deadline)
        priority_layout = QHBoxLayout()
        priority_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)
        priority_layout.addWidget(priority_label)
        priority_layout.addWidget(self.priority)
        time_layout = QHBoxLayout()
        time_layout.setSizeConstraint(QHBoxLayout.SetFixedSize)
        time_layout.addWidget(time_label)
        time_layout.addWidget(self.time)
        layout = QGridLayout(self)
        layout.addWidget(self.lesson, 0, 0)
        layout.addWidget(self.work_type, 1, 0)
        layout.addLayout(actuality_layout, 0, 2)
        layout.addLayout(deadline_layout, 1, 2)
        layout.addLayout(time_layout, 0, 3)
        layout.addLayout(priority_layout, 1, 3)
        layout.addWidget(self.add_button, 2, 3)

        # Tab order
        self.setTabOrder(self.lesson, self.work_type)
        self.setTabOrder(self.work_type, self.actuality)
        self.setTabOrder(self.actuality, self.deadline)
        self.setTabOrder(self.deadline, self.time)
        self.setTabOrder(self.time, self.priority)
        self.setTabOrder(self.priority, self.add_button)