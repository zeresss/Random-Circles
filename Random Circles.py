import sys
from random import randint
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class RandomCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 600, 600)

        self.button = QPushButton('Создать окружность', self)
        self.button.resize(150, 50)
        self.button.move(225, 250)

        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        diameter = randint(50, 250)
        qp.drawEllipse(QRect(randint(0, 600), randint(0, 600), diameter, diameter))


app = QApplication(sys.argv)
ex = RandomCircles()
ex.show()
sys.exit(app.exec())
