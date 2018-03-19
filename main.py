from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from functools import partial
from datetime import date
from core import LessonQueue
from core.data import school_lessons, work_types
from ui import MainWindow, TableWidget
from config import STATUS_BAR_TIMEOUT

lessons = LessonQueue()
_lessons_widgets = []


def task_checked(index, state):
    lessons[index][-2] = state
    lessons.save_data()
    status_bar.showMessage('Состояние урока изменено успешно', msecs=STATUS_BAR_TIMEOUT)


def load_lessons():
    global _lessons_widgets
    _lessons_widgets = []
    for index, lesson in enumerate(lessons.data):
        t = TableWidget(contents.table_contents)
        t.lesson.setText(f'{school_lessons[lesson[0]]}: {work_types[lesson[1]]}')
        t.deadline.setDate(lesson[3])
        t.result.setValue(lesson[-1])
        t.done.setChecked(lesson[-2])

        t.done.clicked.connect(partial(task_checked, index))
        t.delete_button.clicked.connect(partial(remove_lesson, t, index))
        t.save_button.clicked.connect(partial(save_train, index))

        contents.table_layout.addWidget(t)
        _lessons_widgets.append(t)
    status_bar.showMessage('Готово', msecs=STATUS_BAR_TIMEOUT)


def reload_lessons():
    status_bar.showMessage('Обновление...', msecs=STATUS_BAR_TIMEOUT)
    for widget in _lessons_widgets:
        widget.deleteLater()
    load_lessons()


def remove_lesson(widget, index):
    widget.deleteLater()
    del lessons[index]
    status_bar.showMessage('Урок удалён', msecs=STATUS_BAR_TIMEOUT)
    reload_lessons()


def remove_lessons():
    lessons.clear()
    reload_lessons()
    status_bar.showMessage('Очередь очищена', msecs=STATUS_BAR_TIMEOUT)


def save_train(index):
    lessons.neural.add(lessons[index])


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
    lessons.add(*args)
    reload_lessons()


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    contents = window.centralWidget()
    status_bar = window.statusBar()
    data = contents.head_widget

    window.menuBar().action_queue_clear.triggered.connect(remove_lessons)
    window.menuBar().action_clear.triggered.connect(lessons.neural.clear)
    window.menuBar().action_teach.triggered.connect(lessons.neural.train)
    data.add_button.clicked.connect(add_button_click)

    status_bar.showMessage('Загрузка...', msecs=STATUS_BAR_TIMEOUT)
    load_lessons()
    window.show()
    status_bar.showMessage('Готово', msecs=STATUS_BAR_TIMEOUT)

    exit_code = app.exec()
    exit(exit_code)
