# 3-masala. 2 ta LineEdit orqali ikkita sonni oling. Oynaga to'rtta tugmacha qo'shing ("Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish"). 
# Shu tugmachalar bosilganda, kiritilgan ikkita son o'rtasida mos amalni bajarib javobini labelga chiqaruvchi dastur tuzib.
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class KalkulyatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self): 
        self.setWindowTitle("Super App - Kalkulyator")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 24)

    def vidjetlarni_yaratish(self):
        self.line1 = QLineEdit(self)
        self.line1.setGeometry(25, 40, 355, 50)
        self.line1.setPlaceholderText("1-sonni kiriting...")
        self.line1.setFont(QFont("Arial", 16))
        self.line1.setStyleSheet("background-color: white; border: 2px solid black;")

        self.line2 = QLineEdit(self)
        self.line2.setGeometry(25, 110, 355, 50)
        self.line2.setPlaceholderText("2-sonni kiriting...")
        self.line2.setFont(QFont("Arial", 16))
        self.line2.setStyleSheet("background-color: white; border: 2px solid black;")

        self.text1 = QLabel("Javob: ", self)
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 180, 355, 60)
        self.text1.setStyleSheet("color: red; font-weight: bold;")

        self.btn_plus = QPushButton("Qo'shish", self)
        self.btn_plus.setGeometry(25, 270, 160, 50)
        self.btn_plus.setStyleSheet(self.tugma_stili())
        self.btn_plus.clicked.connect(self.qoshish)

        self.btn_minus = QPushButton("Ayirish", self)
        self.btn_minus.setGeometry(220, 270, 160, 50)
        self.btn_minus.setStyleSheet(self.tugma_stili())
        self.btn_minus.clicked.connect(self.ayirish)

        self.btn_mult = QPushButton("Ko'paytirish", self)
        self.btn_mult.setGeometry(25, 340, 160, 50)
        self.btn_mult.setStyleSheet(self.tugma_stili())
        self.btn_mult.clicked.connect(self.kopaytirish)

        self.btn_div = QPushButton("Bo'lish", self)
        self.btn_div.setGeometry(220, 340, 160, 50)
        self.btn_div.setStyleSheet(self.tugma_stili())
        self.btn_div.clicked.connect(self.bolish)

    def tugma_stili(self):
        return "font-size: 18px; font-weight: bold; background-color: #22c70c; border-radius: 20px; border: 2px solid black;"

    def qoshish(self):
        try:
            son1 = float(self.line1.text())
            son2 = float(self.line2.text())
            self.text1.setText(f"Javob: {son1 + son2}")
        except ValueError:
            self.text1.setText("  Son kiriting!")

    def ayirish(self):
        try:
            son1 = float(self.line1.text())
            son2 = float(self.line2.text())
            self.text1.setText(f"Javob: {son1 - son2}")
        except ValueError:
            self.text1.setText("Xatolik: Son kiriting!")

    def kopaytirish(self):
        try:
            son1 = float(self.line1.text())
            son2 = float(self.line2.text())
            self.text1.setText(f"Javob: {son1 * son2}")
        except ValueError:
            self.text1.setText("Xatolik: Son kiriting!")

    def bolish(self):
        try:
            son1 = float(self.line1.text())
            son2 = float(self.line2.text())
            if son2 == 0:
                self.text1.setText("Xatolik: Nolga bo'linmaydi!")
            else:
                self.text1.setText(f"Javob: {son1 / son2}")
        except ValueError:
            self.text1.setText("Xatolik: Son kiriting!")

if __name__ == "__main__":
    app = QApplication([])
    dastur = KalkulyatorApp()
    dastur.show()
    app.exec_()
