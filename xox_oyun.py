from PyQt5 import QtWidgets
from sympy import rad
from xox_tahta import Ui_MainWindow

class Oynama(QtWidgets.QMainWindow,Ui_MainWindow):
    global sıra
    global skor_x
    global skor_o
    sıra="X"
    skor_x=0
    skor_o=0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_1.clicked.connect(self.tiklama)
        self.pushButton_2.clicked.connect(self.tiklama)
        self.pushButton_3.clicked.connect(self.tiklama)
        self.pushButton_4.clicked.connect(self.tiklama)
        self.pushButton_5.clicked.connect(self.tiklama)
        self.pushButton_6.clicked.connect(self.tiklama)
        self.pushButton_7.clicked.connect(self.tiklama)
        self.pushButton_8.clicked.connect(self.tiklama)
        self.pushButton_9.clicked.connect(self.tiklama)
        self.pushButton_yeni_oyun.clicked.connect(self.yenile)
        self.pushButton_devam.clicked.connect(self.yenile)

    def tiklama(self):
        global sıra
        buton=self.sender()
        if buton.text() != "":
            pass
        elif sıra=="X":
            buton.setText("X")
            sıra="O"
        elif sıra=="O":
            buton.setText("O")   
            sıra="X" 
        self.kontrol()

    def yenile(self):
        buton=self.sender()
        global skor_o
        global skor_x
        global sıra

        self.pushButton_1.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        if buton.text()=="yeni oyun":
            sıra="X"
            skor_o=0
            skor_x=0
        elif buton.text()=="devam":
            self.label.setText(f"skor_x:{skor_x}---skor_o:{skor_o}")
            sıra="X"
        self.tiklama()

    def kontrol(self):
            global skor_x
            global skor_o
            butonlar=[self.pushButton_1.text(),self.pushButton_2.text(),self.pushButton_3.text(),self.pushButton_4.text(),self.pushButton_5.text(),self.pushButton_6.text(),self.pushButton_7.text(),self.pushButton_8.text(),self.pushButton_9.text()]

            if self.pushButton_1.text()==self.pushButton_2.text()==self.pushButton_3.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_4.text()==self.pushButton_5.text()==self.pushButton_6.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_7.text()==self.pushButton_8.text()==self.pushButton_9.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_1.text()==self.pushButton_4.text()==self.pushButton_7.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_2.text()==self.pushButton_5.text()==self.pushButton_8.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_3.text()==self.pushButton_6.text()==self.pushButton_9.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_1.text()==self.pushButton_5.text()==self.pushButton_9.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_3.text()==self.pushButton_5.text()==self.pushButton_7.text()=="X":
                self.label.setText("kazanan X")
                skor_x=skor_x+1
                self.yenile()
            elif self.pushButton_1.text()==self.pushButton_2.text()==self.pushButton_3.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_4.text()==self.pushButton_5.text()==self.pushButton_6.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_7.text()==self.pushButton_8.text()==self.pushButton_9.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_1.text()==self.pushButton_4.text()==self.pushButton_7.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_2.text()==self.pushButton_5.text()==self.pushButton_8.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_3.text()==self.pushButton_6.text()==self.pushButton_9.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif self.pushButton_1.text()==self.pushButton_5.text()==self.pushButton_9.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile
            elif self.pushButton_3.text()==self.pushButton_5.text()==self.pushButton_7.text()=="O":
                self.label.setText("kazanan O")
                skor_o=skor_o+1
                self.yenile()
            elif "" not in butonlar :
                self.label.setText("berabere")
                self.yenile()

        