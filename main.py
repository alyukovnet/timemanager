from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from ui import MainWindow


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    data = window.centralWidget().head_widget
    window.show()
    window.statusBar().showMessage('Готов')
    status = app.exec()
    exit(status)
