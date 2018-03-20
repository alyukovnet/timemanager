from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from functools import partial
from datetime import date
from core import TasksQueue
from core.data import school_lessons, work_types
from ui import MainWindow, TableWidget
from config import STATUS_BAR_TIMEOUT

tasks = TasksQueue()
_tasks_widget = []


def task_checked(index, state):
    tasks[index][-2] = state
    tasks.dump()
    status_bar.showMessage('Состояние урока изменено успешно', msecs=STATUS_BAR_TIMEOUT)


def load_tasks():
    global _tasks_widget
    _tasks_widget = []
    for index, task in enumerate(tasks.data):
        t = TableWidget(contents.table_contents)
        t.lesson.setText(f'{school_lessons[task[0]]}: {work_types[task[1]]}')
        t.deadline.setDate(task[3])
        t.result.setValue(task[-1])
        t.done.setChecked(task[-2])

        t.done.clicked.connect(partial(task_checked, index))
        t.delete_button.clicked.connect(partial(remove_lesson, t, index))
        t.save_button.clicked.connect(partial(save_train, index, t))

        contents.table_layout.addWidget(t)
        _tasks_widget.append(t)
    status_bar.showMessage('Готово', msecs=STATUS_BAR_TIMEOUT)


def reload_lessons():
    status_bar.showMessage('Обновление...', msecs=STATUS_BAR_TIMEOUT)
    for widget in _tasks_widget:
        widget.deleteLater()
    load_tasks()


def remove_lesson(widget, index):
    widget.deleteLater()
    del tasks[index]
    status_bar.showMessage('Урок удалён', msecs=STATUS_BAR_TIMEOUT)
    reload_lessons()


def remove_lessons():
    tasks.clear()
    reload_lessons()
    status_bar.showMessage('Очередь очищена', msecs=STATUS_BAR_TIMEOUT)


def save_train(index, t):
    new_predict = round(t.result.value(), 2)
    tasks.neural.add(tasks[index], new_predict)


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
    tasks.add(*args)
    reload_lessons()


def action_clear_button():
    tasks.neural.clear()
    reload_lessons()


def action_teach_button():
    tasks.refresh()
    reload_lessons()


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    contents = window.centralWidget()
    status_bar = window.statusBar()
    data = contents.head_widget

    window.menuBar().action_queue_clear.triggered.connect(remove_lessons)
    window.menuBar().action_clear.triggered.connect(action_clear_button)
    window.menuBar().action_teach.triggered.connect(action_teach_button)
    data.add_button.clicked.connect(add_button_click)

    status_bar.showMessage('Загрузка...', msecs=STATUS_BAR_TIMEOUT)
    load_tasks()
    window.show()
    status_bar.showMessage('Готово', msecs=STATUS_BAR_TIMEOUT)

    exit_code = app.exec()
    exit(exit_code)
