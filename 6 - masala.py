# 6-masala. Hisoblagich
# Oynaga bir Label va ikkita Button joylashtiring: "+1" va "-1". Label dastlab 0 bo'ladi.
# +1 bosilganda qiymat oshadi, -1 bosilganda kamayadi.
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class HisoblagichApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self):
        self.setWindowTitle("Super App - Hisoblagich")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 36)

    def vidjetlarni_yaratish(self):
        self.hisob = 0

        self.text1 = QLabel(str(self.hisob), self)
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 80, 355, 80)
        self.text1.setStyleSheet("color: red; font-weight: bold;")
        self.text1.setProperty("alignment", 0x0004 | 0x0080)

        self.btn_plus = QPushButton("+1", self)
        self.btn_plus.setGeometry(50, 240, 130, 60)
        self.btn_plus.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            background-color: #22c70c;
            border-radius: 20px;
            border: 2px solid black;
        """)
        self.btn_plus.clicked.connect(self.oshir)

        self.btn_minus = QPushButton("-1", self)
        self.btn_minus.setGeometry(225, 240, 130, 60)
        self.btn_minus.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            background-color: #cf3a0c;
            border-radius: 20px;
            border: 2px solid black;
        """)
        self.btn_minus.clicked.connect(self.kamaytir)

    def oshir(self):
        self.hisob += 1
        self.text1.setText(str(self.hisob))

    def kamaytir(self):
        self.hisob -= 1
        self.text1.setText(str(self.hisob))

if __name__ == "__main__":
    app = QApplication([])
    dastur = HisoblagichApp()
    dastur.show()
    app.exec_()