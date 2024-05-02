# импорты
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit, QInputDialog
import json
import system
 
# окно
app = QApplication([])
window = QWidget()
window.setWindowTitle('Система отбора')
window.move(100, 100)
window.resize(800, 450)
 
# функции

 
# основ. лайоуты
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
v_line_list = QVBoxLayout()
v_line_1 = QVBoxLayout()
v_line_2 = QVBoxLayout()
v_line_3 = QVBoxLayout()
v_line_4 = QVBoxLayout()
v_line_5 = QVBoxLayout()
v_line_6 = QVBoxLayout()
line = QHBoxLayout()
line.addLayout(h_line1)
 

# виджеты
criterion1 = QTextEdit()
criterion2 = QTextEdit()
criterion3 = QTextEdit()
criterion4 = QTextEdit()
criterion5 = QTextEdit()
criterion6 = QTextEdit()
criterion7 = QTextEdit()
criterion8 = QTextEdit()
criterion9 = QTextEdit()
criterion10 = QTextEdit()
criterion11 = QTextEdit()
criterion12 = QTextEdit()

# лайоуты
window.setLayout(line)

# привязки

# ниже не трогать!
window.show()
app.exec_()
 