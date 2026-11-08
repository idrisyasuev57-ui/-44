from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton,QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Испытай удачу')
main_win.move(900, 70)
main_win.resize(400,200)
main_win.show()


btn_answer1 = QPushButton('1')
btn_answer2 = QPushButton('2')
btn_answer3 = QPushButton('3')
btn_answer4 = QPushButton('4')
btn_answer5 = QPushButton('5')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer5, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)

main_win.show()
app.exec_()



