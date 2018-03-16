from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from functools import partial
from datetime import date
from threading import Thread
from core import LessonQueue
from core.data import school_lessons, work_types
from ui import MainWindow, TableWidget
from config import STATUS_BAR_TIMEOUT

lessons = LessonQueue()


def delete_button_click(self, index):
    contents.table_layout.removeWidget(self)
    self.deleteLater()
    del lessons[index]
    status_bar.showMessage('Урок удалён', msecs=STATUS_BAR_TIMEOUT)


def task_checked(index, state):
    lessons[index][-2] = state
    lessons.save_data()
    status_bar.showMessage('Состояние урока изменено успешно', msecs=STATUS_BAR_TIMEOUT)


def add_lesson(lesson_dict):
    index, lesson = list(lesson_dict.keys())[0], list(lesson_dict.values())[0]
    t = TableWidget(contents.table_contents)
    t.lesson.setText(f'{school_lessons[lesson[0]]}: {work_types[lesson[1]]}')
    t.deadline.setDate(lesson[3])
    t.result.setValue(lesson[-1])  # TODO: check this
    t.done.setChecked(lesson[-2])

    t.done.clicked.connect(partial(task_checked, index))
    t.delete_button.clicked.connect(partial(delete_button_click, t, index))

    contents.table_layout.addWidget(t)
    status_bar.showMessage('Новый урок добавлен', msecs=STATUS_BAR_TIMEOUT)


def reload_lessons():
    for k, v in lessons.data.items():
        status_bar.showMessage('Загрузка данных...')
        add_lesson({k: v})


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

    exit_code = app.exec()
    lessons.save_data()
    exit(exit_code)
