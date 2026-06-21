# 4-masala. Rang almashtiruvchi dastur
# Oynaga bitta Label va bitta Button joylashtiring. Button bosilganda Labelning matn rangi tasodifiy rangga o'zgaradigan dastur yozing.
# Misol ranglar: qizil, ko'k, yashil, sariq.
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class RanglarApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self):
        self.setWindowTitle("Super App - Ranglar")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 26)

    def vidjetlarni_yaratish(self):
        self.text1 = QLabel("Salom Dunyo!", self)
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 80, 355, 80)
        self.text1.setStyleSheet("color: black; font-weight: bold;")
        self.text1.setProperty("alignment", 0x0004 | 0x0080)

        self.btn1 = QPushButton("Rangni o'zgartirish", self)
        self.btn1.setGeometry(100, 280, 205, 50)
        self.btn1.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            background-color: #22c70c;
            border-radius: 25px;
            border: 2px solid black;
        """)
        self.btn1.clicked.connect(self.rang_almashtir)

        self.ranglar = ["red", "blue", "green", "yellow", "purple", "orange", "white", "magenta"]

    def rang_almashtir(self):
        tasodifiy_rang = random.choice(self.ranglar)
        self.text1.setStyleSheet(f"color: {tasodifiy_rang}; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication([])
    dastur = RanglarApp()
    dastur.show()
    app.exec_()