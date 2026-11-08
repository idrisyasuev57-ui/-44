from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Мое первое приложение')
main_win.show()
winner = QLabel('Hello world')
winner.setText('34')
winner.text()
app.exec_()
