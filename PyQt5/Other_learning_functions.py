import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMessageBox, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        # Метод super() возвращает объект родителя класса Example
        # и мы вызываем его конструктор.
        # Метод __init__() – это конструктор класса в языке Python.

        super().__init__()
        self.initUI()

    def initUI(self):
        # Размер и шрифт всплывающих подсказок
        QToolTip.setFont(QFont('SansSerif', 10))
        # Всплывающая подсказка 1
        self.setToolTip('This is a <b>QWidget</b> widget')
        # Кнопка и ее размеры
        btn = QPushButton("Button", self)
        btn.resize(btn.sizeHint())  # Рекомендуемый размер кнопки
        # btn.resize(320, 320) # Любой размер кнопки
        btn.move(50, 50)

        # Всплывающая подсказка 2
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # Окно!!! setGeometry() по факту заменяет move() и resize()  в одном
        self.setGeometry(300, 300, 280, 250)
        self.setWindowTitle('Icon')
        # не работает почему-то
        self.setWindowIcon(QIcon('web.png'))


        # Кнопка выхода
        qbtn = QPushButton('Quit', self)
        # Что будет, если нажать на кнопку - .clicked
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # Кнопка выхода - внешний вид
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 180)

        self.show()

    # Если закрывать через красный крестик
    def closeEvent(self, event):
        # Пооследний параметр - кнопка по умолчанию, предпоследний - кнопки
        reply = QMessageBox.question(self, 'Message', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def center(self):
        # Получаем прямоугольник, точно определяющий форму главного окна
        qr = self.frameGeometry()
        # Выясняем разрешение экрана нашего монитора и из него центральную точку.
        cp = QDesktopWidget().availableGeometry().center()
        # Наш прямоугольник уже имеет высоту и ширину. Теперь мы устанавливаем центр прямоугольника в центр экрана. Размер прямоугольника не изменяется.
        qr.moveCenter(cp)
        # перемещаем верхнюю левую точку окна приложения в верхнюю левую точку прямоугольника qr, таким образом центрируя окно на нашем экране.
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())