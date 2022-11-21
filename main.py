import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False

        self.pushButton.clicked.connect(self.do_something)

    def do_something(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
            self.do_paint = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        size = randint(0, 50)
        qp.drawEllipse(100, 100, size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())