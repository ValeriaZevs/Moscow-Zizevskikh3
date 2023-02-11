import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt
import random


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('circles.ui', self)
        self.setWindowTitle('Yellow circles')
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)
        painter = QPainter(self.label.pixmap())
        for i in range(3):
            painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.drawEllipse(random.randrange(400), random.randrange(400), 80, 80)



if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())