from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from core import LessonQueue
from core.data import school_lessons, work_types
from datetime import date
from ui import MainWindow, TableWidget
from threading import Thread

lessons = LessonQueue()


def reload_lessons():
    for lesson in lessons.data:
        t = TableWidget(window.centralWidget().table_contents)
        t.lesson.setText(f'{school_lessons[lesson[0]]}: {work_types[lesson[1]]}')
        t.deadline.setDate(lesson[3])
        t.result.setValue(lesson[-1])   # TODO: check this
        t.done.setChecked(lesson[-2])
        window.centralWidget().table_layout.addWidget(t)


def add():
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
    data = window.centralWidget().head_widget
    data.add_button.clicked.connect(add)
    reload_lessons()
    window.show()
    window.statusBar().showMessage('Готов')
    status = app.exec()
    exit(status)
