from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from core import LessonQueue
from core.data import school_lessons, work_types
from datetime import date
from ui import MainWindow, TableWidget
from threading import Thread
from functools import partial

lessons = LessonQueue()


def task_checked(lesson, state):
    lesson[-2] = state
    lessons.save_data()
    status_bar.showMessage('Состояние урока изменено успешно', msecs=2000)


def add_lesson(lesson):
    t = TableWidget(contents.table_contents)
    t.lesson.setText(f'{school_lessons[lesson[0]]}: {work_types[lesson[1]]}')
    t.deadline.setDate(lesson[3])
    t.result.setValue(lesson[-1])  # TODO: check this
    t.done.setChecked(lesson[-2])

    t.done.clicked.connect(partial(task_checked, lesson))

    contents.table_layout.addWidget(t)
    status_bar.showMessage('Новый урок добавлен', msecs=2000)


def reload_lessons():
    for lesson in lessons.data:
        status_bar.showMessage('Загрузка данных...')
        add_lesson(lesson)


def add_button_click():
    time = data.time.time()
    actuality = data.actuality.date()
    deadline = data.deadline.date()
    args = (
        data.lesson.currentIndex(),
        data.work_type.currentIndex(),
        date(actuality.year(), actuality.month(), actuality.day()),
        date(deadline.year(), deadline.month(), deadline.day()),
        time.hour() * 60 + time.minute(),
        round(data.priority.value(), 2)
    )
    p = lessons.add(*args)
    add_lesson(p)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    contents = window.centralWidget()
    status_bar = window.statusBar()
    data = contents.head_widget

    data.add_button.clicked.connect(add_button_click)
    reload_lessons()
    window.show()
    status_bar.showMessage('Готов')

    exit(app.exec())
