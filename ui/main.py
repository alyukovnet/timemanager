from PyQt5.QtWidgets import (QMainWindow, QWidget, QScrollArea, QFrame, QStatusBar, QMenuBar, QMenu,
                             QAction, QGridLayout, QVBoxLayout, qApp)
from .head import HeadWidget
# from table import TableWidget


class _MainWindowContents(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table_area = QScrollArea(self)
        self.table_area.setWidgetResizable(True)
        self.table_contents = QWidget()
        self.table_area.setWidget(self.table_contents)
        self.table_layout = QVBoxLayout(self.table_contents)
        # widget = TableWidget(self.table_contents)
        # self.verticalLayout.addWidget(widget)
        hr = QFrame(self)
        hr.setFrameShape(QFrame.HLine)
        hr.setFrameShadow(QFrame.Sunken)
        self.head_widget = HeadWidget(self)

        # Layout
        layout = QGridLayout(self)
        layout.addWidget(self.head_widget, 0, 0)
        layout.addWidget(hr, 1, 0)
        layout.addWidget(self.table_area, 2, 0)


class _MenuBar(QMenuBar):
    def __init__(self, main_window):
        super().__init__(main_window)
        # self.setGeometry(0, 0, 700, 20)

        # Menus
        menu_file = QMenu('Файл', self)
        menu_file.menuAction().setStatusTip('Тут можно выйти ;)')
        menu_neural = QMenu('Нейронная сеть', self)
        menu_neural.menuAction().setStatusTip('Настройка работы нейронной сети')
        menu_queue = QMenu('Очередь', self)
        menu_queue.menuAction().setStatusTip('Управление очередью')
        menu_help = QMenu('Справка', self)
        menu_help.menuAction().setStatusTip('Ничего полезного ¯\_(ツ)_/¯')

        # Actions
        action_exit = QAction('&Выход', main_window)
        action_exit.triggered.connect(qApp.quit)
        action_exit.setStatusTip('Выйти отсюда')
        action_teach = QAction('&Обучить', main_window)
        # action_teach.triggered.connect()
        action_teach.setStatusTip('Запустить настройку коэффициентов')
        action_clear = QAction('О&чистить', main_window)
        # action_clear.triggered.connect()
        action_clear.setStatusTip('Очистить коэффициенты')
        action_queue_clear = QAction('&Очистить', main_window)
        # action_queue_clear.triggered.connect()
        action_queue_clear.setStatusTip('Очистить очередь')
        action_about_qt = QAction('&О Qt', main_window)
        action_about_qt.triggered.connect(qApp.aboutQt)
        action_about_qt.setStatusTip('Об этом прекрасном фреймворке')
        menu_file.addAction(action_exit)
        menu_neural.addAction(action_teach)
        menu_neural.addAction(action_clear)
        menu_queue.addAction(action_queue_clear)
        menu_help.addAction(action_about_qt)

        self.addAction(menu_file.menuAction())
        self.addAction(menu_neural.menuAction())
        self.addAction(menu_queue.menuAction())
        self.addAction(menu_help.menuAction())


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(800, 500)
        self.setWindowTitle('TimeManager')
        self.setMinimumWidth(700)
        self.setCentralWidget(_MainWindowContents(self))
        self.setStatusBar(QStatusBar(self))
        self.setMenuBar(_MenuBar(self))
